from typing import TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.runtime import Runtime


class MyState(TypedDict):
    query: str
    answer: str

class UserInfoSearch:
    def get_user_by_id(self, user_id):
        return {'id': user_id, 'name': '刘学', 'age': 1000, 'is_vip': True}

class GenerateAgent:
    def get_agent(self):
        import os
        from dotenv import load_dotenv
        from langchain.agents import create_agent
        from langchain.chat_models import init_chat_model
        load_dotenv()
        llm = init_chat_model(
            model='deepseek-ai/DeepSeek-V4-Flash',
            model_provider='openai',
            base_url=os.getenv('OPENAI_BASE_URL'),
            api_key=os.getenv('OPENAI_API_KEY'),
            temperature=0,
        )
        agent = create_agent(
            model=llm,
        )
        return agent

def query_node(state,config: RunnableConfig,runtime: Runtime):
    query = state["query"] #原始问题
    user_id = config['configurable']['user_id']
#     从数据库找

    # 执行图的时候传递的是context，context最终在底层会把值付给runtime当中的context属性
    user_info_search_obj = runtime.context['user_info_search_obj']
    user = user_info_search_obj.get_user_by_id(user_id)

    user_info =f"用户的名字叫{user['name']},年龄是{user['age']},她是vip用户"\
        if user['is_vip']\
        else f"用户的名字叫{user['name']},年龄是{user['age']},她是普通用户"

    query = user_info + '问的问题是:' + query
    return {"query":query}



def answer_node(state,config: RunnableConfig,runtime: Runtime):
    agent = runtime.context['agent']
    res = agent.invoke({
        "messages":[
            {"role":"user","content":state["query"]}
        ]
    })
    return {"answer":res["messages"][-1].content}


builder = StateGraph(state_schema=MyState)
builder.add_node(query_node)
builder.add_node(answer_node)

builder.add_edge(START,"query_node")
builder.add_edge("query_node","answer_node")
builder.add_edge("answer_node",END)


graph = builder.compile()
res = graph.invoke({"query":"我有vip特权吗"},config={
    "configurable":{
        "user_id":1000
    }
},context={
    "user_info_search_obj":UserInfoSearch(),
    "agent":GenerateAgent().get_agent()
})
print(res)