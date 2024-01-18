import os
import pandas as pd
from langchain_community.llms import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import openai


def get_response_output(api_key,st,df):
    os.environ['OPENAI_API_KEY'] = api_key
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-1106"),
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    return agent.run(st)


def check_api(api_key):
    client = openai.OpenAI(api_key=api_key)
    response = client.completions.create(
    prompt="Hello world",
    model="gpt-3.5-turbo-instruct")
    return True