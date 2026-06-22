from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model='Qwen/Qwen3-8B',
    model_provider='openai',
    # 从系统环境变量获取
    # base_url=os.getenv('OPENAI_API_URL'),
    # api_key=os.getenv('OPENAI_API_KEY'),
    # 从env文件获取
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0
)

res = llm.invoke(input="hello")
print(res.content)