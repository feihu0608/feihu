from typing import TypedDict
import time

from langgraph.constants import START
from langgraph.graph import StateGraph
from langgraph.runtime import Runtime
from openai import base_url, api_key


class MyState(TypedDict):
    query: str
    result: str
    current_step: str

def query_node(state: MyState):
    return {"query":state["query"],"current_step":"处理问题阶段"}

def think_node(state:MyState,runtime:Runtime):
    steps = ["正在思考","正在分析","正在评估"]
    for step in steps:
        time.sleep(2)
        # print(step)
        # 我们节点当中的数据,后期都是通过手段去写出去,而不是通过print去打印日志
        runtime.stream_writer(step)
    return {'current_step':'思考分析阶段'}

def answer_node(state:MyState):
    from langchain.chat_models import init_chat_model
    import os
    from dotenv import load_dotenv
    load_dotenv()
    llm = init_chat_model(
        model='deepseek-ai/DeepSeek-V4-Flash',
        model_provider='openai',
        base_url=os.getenv('OPENAI_BASE_URL'),
        api_key=os.getenv('OPENAI_API_KEY'),
        temperature=0
    )

    messages = [
        {'role':'user','content':state['query']},
    ]

    res = llm.invoke(input=messages)

    return {'result':res.content,'current_step':'生成结果阶段'}

builder = StateGraph(state_schema=MyState)

builder.add_node(query_node)
builder.add_node(think_node)
builder.add_node(answer_node)


builder.add_edge(START,"query_node")
builder.add_edge("query_node","think_node")
builder.add_edge("think_node","answer_node")

graph = builder.compile()
# res = graph.invoke({"query":"用户问题"}) #这样输出是不能看到内部往外面写的数据

# 演示不同的流式输出模式
# stream_mode = "values":每执行完一个节点，输出当前的完整 State
# stream_mode = "updates":每执行完一个节点，输出该节点返回的增量数据
# stream_mode = "custom":就是runtime.stream_writer中传入的数据
# stream_mode = "messages":输出 LLM（真实要创LLM，不支持智能体） 生成的消息片段(Token) 不支持智能体（Agent）场景，因为智能体的响应可能包含工具调用、多轮推理等复杂结构
# stream_mode = "debug ":输出所有详细的执行信息，包括任务调度、输入输出等
# stream_mode = ["updates", "custom"]: 混合模式（同时获取updates和custom数据）

res = graph.stream({'query':'用户问题'},stream_mode = ["updates", "custom"])
for r in res:
    print(r)
    # print(r[0].content,end='')