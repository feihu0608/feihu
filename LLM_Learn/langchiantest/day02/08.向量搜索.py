from pymilvus import MilvusClient,AnnSearchRequest

def connect_to_milvus():
    from pymilvus import MilvusClient
    client = MilvusClient(
        uri='http://localhost:19530',
        db_name='test'
    )
    return client
# 对用户传入数据进行向量化处理
def embedding_query(query):
    from FlagEmbedding import BGEM3FlagModel
    embed_model = BGEM3FlagModel(
        model_name_or_path='../assets/models/bge-m3'
    )
    return embed_model.encode(sentences=[query],return_dense=True,return_sparse=True)
# 只用稠密向量进行进行数据查询
def search_for_vector(query,client,topk):
    # 1.需要把用户的查询问题拿到也要对应的向量化
    query_vector = embedding_query(query)['dense_vecs']

    # 2.在milvus中搜索
    res = client.search(
        collection_name='test_collection',
        data=query_vector,
        limit=topk,
        output_fields=["id","text","metadata"],
        anns_field='vector'
    )
    print(res)
    print(len(res[0]))
    return res

# 只用稀疏向量进行进行数据查询
def search_for_sparse(query,client,topk):
    # 1.需要把用户的查询问题拿到也要对应的向量化
    query_vector = embedding_query(query)['lexical_weights']

    # 2.在milvus中搜索
    res = client.search(
        collection_name='test_collection',
        data=query_vector,
        limit=topk,
        output_fields=["id","text","metadata"],
        anns_field='sparse'
    )
    print(res)
    print(len(res[0]))
    return res

# 混合向量搜素
def mixed_search(query,client,topk):
    from pymilvus import AnnSearchRequest,RRFRanker
    query_vector = embedding_query(query)

    # 把稠密向量和稀疏向量搜索分别做成一个请求
    vector_req = AnnSearchRequest(
        data=query_vector['dense_vecs'],
        anns_field='vector',
        param={"metric_type":"L2",},
        limit=topk,
    )

    sparse_req = AnnSearchRequest(
        data=query_vector['lexical_weights'],
        anns_field='sparse',
        param={"metric_type":"IP",},
        limit=topk,
    )
    
    res = client.hybrid_search(
        collection_name='test_collection',
        reqs=[vector_req,sparse_req],
        ranker=RRFRanker(),
        limit=topk,
        output_fields=["id","text","metadata"],
    )
    print(res)
    print(len(res[0]))
    return res

if __name__ == '__main__':
    mixed_search("监护人",connect_to_milvus(),3)

