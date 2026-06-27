import time
from typing import TypedDict

from langgraph.cache.memory import InMemoryCache
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import CachePolicy


class MyState(TypedDict):
    query:str
    result:str

def query_node(state:MyState):
    return {'query':state['query']}

def request_node(state:MyState):
    print("开始请求网络...")
    time.sleep(5)
    return {"result":f"{state['query']}网络请求的结果"}

builder = StateGraph(state_schema=MyState)

builder.add_node(query_node)
# builder.add_node(request_node,cache_policy=CachePolicy(ttl=10)) # 使用节点缓存保存状态 ttl生命周期两次调用之间的间隔不能超过10S
builder.add_node(request_node,cache_policy=CachePolicy(ttl=10)) #使用节点缓存保存状态
# builder.add_node(request_node) #不用节点缓存改用记忆

builder.add_edge(START,'query_node')
builder.add_edge('query_node','request_node')
builder.add_edge('request_node',END)

# graph = builder.compile(cache=InMemoryCache())
# res = graph.invoke(input={'query':'用户的问题'}
#                    )
# print(res)
#
#
# res = graph.invoke(input={'query':'用户的问题'}
#                    )
#
#   print(res)

graph = builder.compile(checkpointer=InMemorySaver()) # 只使用节点缓存保存状态
# graph = builder.compile(checkpointer=InMemorySaver(),cache=InMemoryCache())
res = graph.invoke(
    input={'query':'用户的问题'},
    config={
        "configurable":{
            "thread_id":1
        }
    }
)

print(res)

res = graph.invoke(
    input={'query':'用户的问题'}, # 如果只使用记忆状态作为实现缓存的功能的话,输入要为None才是读取缓存,否则为重新执行全流程
    config={
        "configurable":{
            "thread_id":1
        }
    }
)

print(res)

