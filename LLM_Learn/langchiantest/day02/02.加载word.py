from langchain_community.document_loaders import UnstructuredWordDocumentLoader

loader = UnstructuredWordDocumentLoader(
    file_path="../assets/sample.docx",
    mode = "elements"
)

# 加载器在加载文档的时候如果mode="elements"也会有一个切分的效果
# 如果不写或者写的是mode="single",默认不切分
res = loader.load()
print(res,len(res))
