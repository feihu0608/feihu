# 一.单个chain当中的串行
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',
    model_provider = 'openai',
    base_url = os.getenv('OPENAI_BASE_URL'),
    api_key = os.getenv('OPENAI_API_KEY'),
    temperature = 0,
)

messages = [
    {"role":'system',"content":'你是一个专业的{job}'},
    {"role":'human','content':'我想问{question}'},
]

cpt = ChatPromptTemplate.format_messages(messages=messages,)

sop = StrOutputParser()
# 单链里面组件一定是串行的
chain = cpt | llm | sop

res = chain.invoke({"job":"情感分析大师","question":"怎么让妹妹爱上我"})

print(res)

# 二.多个chain组成的并行方式
# from langchain.chat_models import init_chat_model
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
#
# import os
# from dotenv import load_dotenv
# from langchain_core.runnables import RunnableParallel
#
# load_dotenv()
#
# messages1 = [
#     {'role':'system','content':'你是一个优秀的翻译官'},
#     {"role":'user','content':'用英语帮我翻译一下我爱你{name},年龄是{age}'}
# ]
#
# cpt1 = ChatPromptTemplate.from_messages(messages1)
#
# llm1 = init_chat_model(
#     model = 'deepseek-ai/DeepSeek-V4-Flash',
#     model_provider='openai',
#     base_url = os.getenv('OPENAI_BASE_URL'),
#     api_key = os.getenv('OPENAI_API_KEY'),
#     temperature = 0,
# )
#
# sop1 = StrOutputParser()
#
# chain1 = cpt1 | llm1 | sop1
#
#
# messages2 = [
#     {'role':'system','content':'你是一个优秀的翻译官'},
#     {"role":'user','content':'用韩语帮我翻译一下我爱你{name},年龄是{age}'}
# ]
#
# cpt2 = ChatPromptTemplate.format_messages(messages2)
#
# llm2 = init_chat_model(
#     model = 'deepseek-ai/DeepSeek-V4-Flash',
#     model_provider='openai',
#     base_url = os.getenv('OPENAI_BASE_URL'),
#     api_key = os.getenv('OPENAI_API_KEY'),
#     temperature = 0,
# )
#
# sop2 = StrOutputParser()
# # 单链里面组件一定是串行的
# chain2 = cpt1 | llm1 | sop1
# # 多链并行,必须这么干
# final_chain = RunnableParallel(
#     aa = chain1,
#     bb = chain2,
# )
# # 这种方式不可行AttributeError: 'dict' object has no attribute 'invoke'
# # final_chain = {
# #     "aa":chain1,
# #     "bb":chain2,
# # }
# res = final_chain.invoke({'name':'赵丽颖','age':'18'})
# print(res)

# # 三.多个chain组成的混合方法
# from langchain.chat_models import init_chat_model
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
#
# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# messages1 = [
#     {'role':'system','content':'你是一个翻译官'},
#     {'role':'user','content':'请用英语给我翻译:我爱{name},年龄是{age}'},
# ]
#
# cpt1 = ChatPromptTemplate.from_messages(messages=messages1)
#
# llm1 = init_chat_model(
#     model = 'deepseek-ai/DeepSeek-V4-Flash',
#     model_provider = 'openai',
#     base_url = os.getenv('OPENAI_BASE_URL'),
#     api_key = os.getenv('OPENAI_API_KEY'),
#     temperature = 0,
# )
#
# sop1 = StrOutputParser()
#
# chain1 = cpt1 | llm1 | sop1
#
# messages2 = [
#     {'role':'system','content':'你是一个优秀的翻译官'},
#     {'role':'user','content':'请用德文给我翻译:我爱你{name},年龄是{age}'}
# ]
#
# cpt2 = ChatPromptTemplate.from_messages(messages=messages2)
#
# llm2 = init_chat_model(
#     model = 'deepseek-ai/DeepSeek-V4-Flash',
#     model_provider = 'openai',
#     base_url = os.getenv('OPENAI_BASE_URL'),
#     api_key = os.getenv('OPENAI_API_KEY'),
#     temperature = 0,
# )
#
# sop2 = StrOutputParser()
# chain2 = cpt2 | llm2 | sop2
#
# messages3 = [
#     {'role':'system','content':'你是一个优秀的分析大师'},
#     {'role':'user','content':'请帮我分析下上面两个翻译哪个更好?一个是{chain1},另一个是{chain2}'}
# ]
#
# cpt3 = ChatPromptTemplate.from_messages(messages=messages3)
# llm3 = init_chat_model(
#     model = 'deepseek-ai/DeepSeek-V4-Flash',
#     model_provider = 'openai',
#     base_url = os.getenv('OPENAI_BASE_URL'),
#     api_key = os.getenv('OPENAI_API_KEY'),
#     temperature = 0,
# )
# sop3 = StrOutputParser()
# chain3 = cpt3 | llm3 | sop3
#
# final_chain = {
#     "chain1": chain1,
#     "chain2": chain2,
# } | chain3
#
# res = final_chain.invoke({'name':'赵丽颖','age':'18'})
#
# print(res)

