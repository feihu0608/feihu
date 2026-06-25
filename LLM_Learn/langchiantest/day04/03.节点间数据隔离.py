# 状态  考虑所有的节点功能当中输入和输出的数据，本质是一个字典,定义状态定义的是状态的结构
# 节点  每一步的功能，节点都有可能有输入和输出
# 边    连接节点
# from pydantic import BaseModel
# class Star
from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph
from pydantic import BaseModel


class MyState(TypedDict):
    query: str
    rag_search_result: str
    web_search_result: str
    final_result: str

#     节点间的状态隔离，了解
class QueryState(TypedDict):
    query: str

class RagSearchState(TypedDict):
    query: str
    rag_search_result: str

class WebSearchState(TypedDict):
    query: str
    web_search_result: str

class FinalState(TypedDict):
    query: str
    rag_search_result: str
    web_search_result: str
    final_result: str


def query_node(state:QueryState):
    print(state)
#     节点输出是return
#     state接受的就是状态的字典，这个字典会在创建graph的构建器时候去创建
#     每个节点return就是在修改状态，我们虽然返回的是一个字典，里面只有整个状态的部分内容
#     但是langgraph底层会把我们这个字典和之前的状态字典进行合并，然后再传递给下一个节点
#     以后我们在return时候，返回增量字典即可

    # state['query'] = state['query']
    # return state  这个写法没错，但是不建议这样写
    return {"query":state["query"]}


def rag_search_node(state:RagSearchState):
    query = state["query"]
    return {"rag_search_result":f"{query}的rag搜索结果"}



def web_search_node(state:WebSearchState):
    query = state["query"]
    return {"web_search_result":f"{query}的web搜索结果"}


def final_node(state:FinalState):
    query = state["query"]
    rag_search_result = state["rag_search_result"]
    web_search_result = state["web_search_result"]
    return {"final_result": f"{query}最终结果是:{rag_search_result}和{web_search_result}的合并"}


# 创建langgraph的构建器
builder = StateGraph(state_schema=MyState)  # 创建一个状态图的构建器,内部会创建状态的字典吗，就是节点的第一个形参state接受的值

# 把每个节点添加到构建器
builder.add_node('query_node',query_node)
builder.add_node(rag_search_node)
builder.add_node(web_search_node)
builder.add_node(final_node)

# 再去添加边
builder.add_edge(START,'query_node')
builder.add_edge('query_node','rag_search_node')
builder.add_edge('query_node','web_search_node')
builder.add_edge('rag_search_node','final_node')
builder.add_edge('web_search_node','final_node')
builder.add_edge('final_node',END)

# langgraph去做编译生成图
graph = builder.compile()
# 图去做执行
# invoke传递的字典其实本质就是初始的状态，会把初始状态的字典和state合并
res = graph.invoke({"query":"用户问的问题"})
print(res)  #返回的就是最终的state结果



