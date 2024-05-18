from langchain.llms.base import BaseLanguageModel
from azure.identity import DefaultAzureCredential
from langchain_core.messages import HumanMessage
from langchain_community.chat_models import AzureChatOpenAI, ChatAnthropic, ChatOpenAI, ChatVertexAI


import os


TEMPERATURE = 0.7
MAX_TOKENS = 100


model = AzureChatOpenAI(
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
)


message = HumanMessage(
    content="What does DataStax do ? tell me all the cool things I can build with langflow on Azure"
)
response = model.invoke([message])
print(response.content)
