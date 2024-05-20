from langchain_community.chat_models import AzureChatOpenAI

class GPT35():

    def __init__(self,key,base):
        self._key = key
        self._endpoint = base
    
    def getGPTModel(self, deployment_name):

        return AzureChatOpenAI(
            azure_deployment = deployment_name, 
            openai_api_version = "2023-09-15-preview",
            openai_api_key = self._key,
            azure_endpoint = self._endpoint,
            temperature = 0,
            max_tokens = 2000,
            request_timeout = 60
        )