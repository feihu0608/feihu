from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = UnstructuredWordDocumentLoader(
    file_path="../assets/sample.docx",
    mode="single"
)

# 加载文档
load_docs = loader.load()
# print(load_docs)

# 获取切割器
spliter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", "。", "！", "？", "……", "，", ""],
    chunk_size= 500,
    chunk_overlap= 50,
    length_function= len,
    add_start_index=True
)

splite_docs = spliter.split_documents(load_docs)
print(splite_docs)
print(len(splite_docs))
print(type(splite_docs),type(splite_docs[0]))

