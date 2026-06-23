from langchain_text_splitters import RecursiveCharacterTextSplitter
from pymilvus import MilvusClient

def connect_to_milvus():
    client = MilvusClient(
        uri="http://localhost:19530",
        db_name='test'
    )
    return client

# 整个插入流程
def insert_data_to_milvus(client:MilvusClient):
    #1.加载文档
    from langchain_community.document_loaders import UnstructuredWordDocumentLoader
    loader = UnstructuredWordDocumentLoader(
        file_path='../assets/sample.docx',
    )
    load_docx = loader.load()

    #2.切分文档
    spliter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", "。", "！", "？", "……", "，", ""],
        chunk_size=500,
        chunk_overlap=50,
        add_start_index=True,
        length_function=len,
    )

    splite_docs = spliter.split_documents(load_docx)[0:20]

    #3.通过bgem3对切割出来的文档内容进行向量化
    from FlagEmbedding import BGEM3FlagModel
    embed_model = BGEM3FlagModel(
        model_name_or_path='../assets/models/bge-m3'
    )

    embed_res = embed_model.encode(
        sentences=[doc.page_content for doc in splite_docs],
        return_dense=True,
        return_sparse=True
    )

    print(embed_res)

    #4.存库,milvus存储的数据需要是一个字典列表,我们需要整理这个数据,然后再去插入
    data_list = []
    for doc,vector,sparse in zip(splite_docs,embed_res['dense_vecs'],embed_res['lexical_weights']):
        data_list.append({
            "text":doc.page_content,
            "metadata":doc.metadata,
            "vector":vector,
            "sparse":sparse,
        }
        )

    res = client.insert(
        collection_name='test_collection',
        data=data_list,
    )
    print(res)

if __name__ == '__main__':
    insert_data_to_milvus(connect_to_milvus())