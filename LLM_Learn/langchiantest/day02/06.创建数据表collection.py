# 1.创建milvus链接
from pymilvus import DataType,MilvusClient

def connect_to_milvus():
    from pymilvus import MilvusClient
    client = MilvusClient(
        uri='http://localhost:19530',
        db_name='test',
    )
    return client

def create_collection_schema():
    from pymilvus import MilvusClient
    # 创建自动递增ID的schema
    schema = MilvusClient.create_schema(
        auto_id=True,
    )
    # 添加主键id字段,使用INT64类型
    schema.add_field(
        field_name="id",
        datatype=DataType.INT64,
        is_primary=True,
    # 添加文本字段,最大长度设置为2000
    ).add_field(
        field_name='text',
        datatype=DataType.VARCHAR,
        max_length=2000,
    # 添加元数据字段,使用JSON类型存储结构化信息
    ).add_field(
        field_name='metadata',
        datatype=DataType.JSON,
    # 添加稠密向量字段,用于语义检索,维度1024
    ).add_field(
        field_name='vector',
        datatype=DataType.FLOAT_VECTOR,
        dim=1024,
    # 添加稀疏向量字段,支持关键字匹配
    ).add_field(
        field_name='sparse',
        datatype=DataType.SPARSE_FLOAT_VECTOR,
    )
    return schema

# 3. 创建表索引
def create_collection_index():
    from pymilvus import MilvusClient

    index_params = MilvusClient.prepare_index_params()
    index_params.add_index(
        field_name='vector',
        index_type='HNSW', #索引类型为分层导航小世界
        metric_type='L2', #求相似度的算法
    )

    index_params.add_index(
        field_name='sparse',
        index_type='SPARSE_INVERTED_INDEX',#索引类型为稀疏倒序索引
        metric_type='IP' #求内积作为相似度的算法
    )

    return index_params

# 4.创建表
def create_collection(client:MilvusClient):
    collection_name = 'test_collection'
    if collection_name in client.list_collections():
        client.drop_collection(collection_name)
    client.create_collection(
        collection_name=collection_name,
        schema=create_collection_schema(),
        index_params=create_collection_index(),
    )

    res = client.list_collections()
    print(res)

if __name__ == '__main__':
    create_collection(connect_to_milvus())