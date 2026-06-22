# # 1.通过项目的.env文件去管理
# from dotenv import load_dotenv
# load_dotenv() # 加载.env文件
# # 2.调用的时候,可以通过os模块去拿到相关的环境变量
# import os
# baseUrl = os.getenv('OPENAI_BASE_URL')
# apiKey = os.getenv('OPENAI_API_KEY')
# print(baseUrl)
# print(apiKey)

# 二
# 只需要把相关的环境变量配置到系统环境变量中即可直接使用os
import os
print(os.getenv('OPENAI_BASE_URL'))
print(os.getenv('OPENAI_API_KEY'))