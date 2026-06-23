# 本质是将pdf转换为markdown
import time

from dotenv import load_dotenv
load_dotenv()
import os
import requests

token = os.getenv("MINERU_TOKEN")
def upload_pdf():

    url = "https://mineru.net/api/v4/file-urls/batch"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "files": [
            {"name": "demo.pdf", "data_id": "abcd"}
        ],
        "model_version": "vlm"
    }
    file_path = ["../assets/sample.pdf"]
    try:
        response = requests.post(url, headers=header, json=data)
        if response.status_code == 200:
            result = response.json()
            print('response success. result:{}'.format(result))
            if result["code"] == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                print('batch_id:{},urls:{}'.format(batch_id, urls))
                for i in range(0, len(urls)):
                    with open(file_path[i], 'rb') as f:
                        res_upload = requests.put(urls[i], data=f)
                        if res_upload.status_code == 200:
                            print(f"{urls[i]} upload success")
                        else:
                            print(f"{urls[i]} upload failed")
            else:
                print('apply upload url failed,reason:{}'.format(result["msg"]))
            return batch_id
        else:
            print('response not success. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)

def transformer_markdown(batch_id):
    url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    res = requests.get(url, headers=header)
    while res.json()["data"]["extract_result"][0]["state"] != "done":
        time.sleep(0.5)
        res = requests.get(url, headers=header)
    print(res.status_code)
    print(res.json())
    print(res.json()["data"])
    return res.json()["data"]["extract_result"][0]["full_zip_url"]

if __name__ == '__main__':
    batch_id = upload_pdf()
    res = transformer_markdown(batch_id)
    print(res)