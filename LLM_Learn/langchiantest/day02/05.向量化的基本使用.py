# from langchain_community.embeddings import HuggingFaceEmbeddings
# # 使用它可以去制定模型生成稠密向量
# embed_model = HuggingFaceEmbeddings(
#     model_name='../assets/models/bge-base-zh-v1.5'
# )
# # 返回一维列表
# res = embed_model.embed_query("你好")
# print(res)
#
# # 返回二维列表
# res1 = embed_model.embed_documents(["你好","弟弟"])
# print(res1)


# 同时返回稠密和稀疏向量
from FlagEmbedding import BGEM3FlagModel
embed_model = BGEM3FlagModel(
    model_name_or_path='../assets/models/bge-m3',
)

# 用它的时候哪怕是一个字符串也用列表,方便后期好操作
res = embed_model.encode(["你好","弟弟"],return_dense=True,return_sparse=True)
print(res)

