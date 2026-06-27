from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import interrupt, Command


class MyState(TypedDict):
    name:str
    money:int
    flag:bool

def transfer_money_node(state:MyState):
    # interrupt上面不要写业务代码.会走多次
    # 打断操作
    # 打断操作传递的参数,可以让外部调用的结果当中拿到
    result = interrupt(
        {
            'title':'转账审核',
            'description':"""
                这是一个人工审核转账信息的操作，后续需要再次调用传入command,来决定后续操作，这个command有三种情况：
                - approve: 通过，用户调用传递的命令如果 {"type":"approve"}
                - reject: 拒绝,用户调用传递的命令如果 {"type":"reject"}
                - edit: 修改 {"type":"edit","name":"new name"，"money":新的金额}
            """
        }
    )


    # 调用interrupt，传递的参数信息会在第一次invoke的时候外部获取到
    # 调用interrupt，节点内部，interrupt的返回值拿到的是外部第二次调用的command信息字典
    print(result)

    if result['type'] == "approve":
        return {"name":state["name"],"money":state["money"],"flag":True}
    elif result['type'] == "edit":
        return {"name":result['name'] if result.get('name',None) else state['name'],"money":result['money'] if result.get('money',None) else state['money'],"flag":True}
    else:
        return {"name": state["name"], "money": state["money"], "flag": False}

builder = StateGraph(state_schema=MyState)

builder.add_node(transfer_money_node)
builder.add_edge(START,"transfer_money_node")
builder.add_edge("transfer_money_node",END)


graph = builder.compile(checkpointer=InMemorySaver())
res = graph.invoke({"name":"杨幂","money":10000},config={
    "configurable":{
       "thread_id":1
    },
})
print(res)

if '__interrupt__' in res:
    print("操作被打断，要重新执行输入命令决定后续操作，接着上次打断的位置继续")
    command = Command(resume={"type":"edit","name":"赵丽颖"})
    res1 = graph.invoke(command,config={
        "configurable":{
           "thread_id":1
        },
    })
    print(res1)