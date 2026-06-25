from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph


class MyState(TypedDict):
    key1:str
    key2:str
    key3:str


def node_1(state:MyState):
    print("node1执行了")
    return {"key1":"value1"}


def node_2(state:MyState):
    print("node2执行了")

    # raise Exception("node2执行失败")

    return {"key2":"value2"}

def node_3(state:MyState):
    print("node3执行了")
    return {"key3":"value3"}



builder = StateGraph(state_schema=MyState)
builder.add_node(node_1)
builder.add_node(node_2)
builder.add_node(node_3)

builder.add_edge(START, "node_1")
builder.add_edge( "node_1", "node_2")
builder.add_edge( "node_2", "node_3")
builder.add_edge( "node_3", END)


import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
conn = sqlite3.connect(database="./test1.db",check_same_thread=False)

graph = builder.compile(checkpointer=SqliteSaver(conn=conn))

res = graph.invoke(None,config={
    "configurable":{
        "thread_id":1
    }
})


print(res)


