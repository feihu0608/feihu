from openai import base_url
from torch._C._return_types import topk


def connect_to_milvus():
    from pymilvus import MilvusClient
    client = MilvusClient(
        uri='http://localhost:19530',
        db_name='test',
    )
    return client

def embedding_query(query):
    from FlagEmbedding import BGEM3FlagModel
    embed_model = BGEM3FlagModel(
        model_name_or_path='../assets/models/bge-m3'
    )
    return embed_model.encode(sentences=[query],return_dense=True,return_sparse=True)

def mixed_search(query,client,topk):
    from pymilvus import AnnSearchRequest,RRFRanker
    query_res = embedding_query(query)
    vector_req = AnnSearchRequest(
        data=query_res['dense_vecs'],
        anns_field='vector',
        param={'metric_type':'L2',},
        limit=topk,
    )

    spare_req = AnnSearchRequest(
        data=query_res['lexical_weights'],
        anns_field='sparse',
        param={'metric_type':'IP',},
        limit=topk,
    )

    res = client.hybrid_search(
        collection_name='test_collection',
        reqs=[vector_req,spare_req],
        ranker=RRFRanker(),
        limit=topk,
        output_fields=['id','text','metadata'],
    )

    return res

# 生成答案
def generate_answer(query,client,topk):
    # 1.混合搜素
    search_res = mixed_search(query,client,topk)
    # print("search_res:",search_res)
    # 我们从向量数据库当中找到的参考答案（上下文）
    # 2、把搜索到的相似度高的答案字符串，拼接成一个大的字符串作为后期大模型查找的参考
    context = '\n'.join([item['entity']['text'] for search in search_res for item in search])
    #3.构造大模型,把原本的问题和上下文拼接起来,然后进行大模型查询
    from langchain.chat_models import init_chat_model
    import os
    from dotenv import load_dotenv
    load_dotenv()
    llm = init_chat_model(
        model='deepseek-ai/DeepSeeK-V4-Flash',
        model_provider='openai',
        base_url=os.getenv('OPENAI_BASE_URL'),
        api_key=os.getenv('OPENAI_API_KEY'),
        temperature=0,
    )

    messages = [
        {'role':'system','content':'你是一个专业的法律咨询师'},
        {'role':'user','content':f'请帮我解答一下问题,可以参考我给你的答案,问题是{query},参考答案是{context}'}
    ]

    res=llm.invoke(input=messages,)
    print(res.content)

if __name__ == '__main__':
    client=connect_to_milvus()
    generate_answer("请问法人代表什么,有什么责任",client,10)