import re
text = "aabbaabb"
print(re.search(r"a.*?b", text).group())  # 输出：aab



text = "邮箱：1a@test.com，邮箱2：b@test.com"
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)  # 输出：['a@test.com', 'b@test.com']



def extract_domain(url):
    # 匹配 http:// 或 https:// 后的域名
    pattern = r"https?://([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    result = re.search(pattern, url)
    return result.group(1) if result else None

print(extract_domain("https://www.python.org"))  # 输出：www.python.org
print(extract_domain("http://baidu.com"))