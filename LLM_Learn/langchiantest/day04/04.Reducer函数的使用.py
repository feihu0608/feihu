import operator
from typing import TypedDict, Annotated

from langgraph.constants import START, END
from langgraph.graph import StateGraph

# 自己定义的函数作为reducer
def add(s1,s2):
    return s1 + s2 + "哈哈"

class MyState(TypedDict):
    # result:str # 没有设置reducer
    result:Annotated[str,add] # 设置自己定义的reducer
    # result:Annotated[str, operator.add] # 设置系统包reducer

def handler_nodel1(state:MyState):
    result = '第一个节点处理的result结果'
    return {'result':result}

def handler_nodel2(state:MyState):
    result = '第二个节点处理的result结果'
    return {'result':result}

builder = StateGraph(state_schema=MyState)

builder.add_node(handler_nodel1)
builder.add_node(handler_nodel2)


# 添加边实现串行
builder.add_edge(START,"handler_nodel1")
builder.add_edge("handler_nodel1","handler_nodel2")
builder.add_edge("handler_nodel2",END)

# 添加边实现并行
# builder.add_edge(START,"handler_nodel1")
# builder.add_edge(START,"handler_nodel2")
# builder.add_edge("handler_nodel1",END)
# builder.add_edge("handler_nodel2",END)

# 串行节点在给同一个状态赋值,默认是替换
# 并行节点在给统一个状态赋值,炸(不能再同一个超步当中给一个状态多次赋值)



graph = builder.compile()
res = graph.invoke(input={})
print(res)
