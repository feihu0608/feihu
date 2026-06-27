from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph


class MyState(TypedDict):
    num:int
    result:str

def query_node(state:MyState):
#     query_node是我们要对输入的数字有操作，如果没有操作，可以不要这个节点
    num = state["num"] + 1
    return {"num":num}


# 先不做条件，先把奇数和偶数的节点先写完，最后再考虑这个条件边的路由

def odd_node(state:MyState):
    print(f"{state["num"]}是一个奇数")
    return {"result":"我爱你杨幂"}

def even_node(state:MyState):
    print(f"{state["num"]}是一个偶数")
    return {"result":"我爱你迪丽热巴"}

# 条件路由,添加边的时候需要使用条件边来添加条件路由
# 不是节点,所以不需要添加节点
def condition_route(state:MyState):
    if state['num'] % 2 == 0:
        return "even_node"
    else:
        return "odd_node"

builder = StateGraph(state_schema=MyState)
builder.add_node(query_node)
builder.add_node(odd_node)
builder.add_node(even_node)

builder.add_edge(START,'query_node')
# 考虑做条件边,必须要写条件路由,看起来像一个节点,但是不能把它当节点对待
builder.add_conditional_edges('query_node',condition_route)
# builder.add_edge('odd_node',END)
# builder.add_edge('even_node',END)

# 1、条件边的实现 是用条件路由和边实现的
# 2、条件路由也是一个函数，看起来像节点，但不是节点
# 3、一个节点出来后需要做条件判断，我们可以使用条件边，让这个节点连接条件路由
# 4、条件路由当中会自动根据判断的结果决定连接那个节点，所以我们不需要写条件边后面的连接
# 5、条件边最终选择连接的节点，我们直接去连接下一个即可


graph = builder.compile()
res = graph.invoke({"num":99})
print(res)
