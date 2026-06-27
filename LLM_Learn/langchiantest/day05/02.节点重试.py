from typing import TypedDict


from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import RetryPolicy
from urllib3.exceptions import HTTPError


class MyState(TypedDict):
    query:str
    result:str

def query_node(state:MyState):
    return {'query':state['query']}

count = 0
def request_node(state:MyState):
    global count
    count += 1
    print("开始请求网路....")
    if count < 4:
        # 后期异常抛的时候要么就是Exception,要么就是HTTPError,其他的用不到
        # raise Exception('网络异常') # 这里异常和重试有关联的
        raise HTTPError('网络异常')

        # 下面这些异常,是不会触发重试的
        # raise ValueError('网络异常')
        # raise ZeroDivisionError('除零异常')
    else:
        return {'result':f"{state['query']}网络请求的结果"}

builder = StateGraph(state_schema=MyState)

builder.add_node(query_node)
builder.add_node(request_node,retry_policy=RetryPolicy(max_attempts=4,initial_interval=1)) # max_attempts最大超步个数,initial_interval初始化开始间隔多少秒开始重试,默认每下一次间隔乘以2倍

builder.add_edge(START,'query_node')
builder.add_edge('query_node','request_node')
builder.add_edge('request_node',END)

graph = builder.compile()
res = graph.invoke(input={'query':'用户的问题'})
print(res)

