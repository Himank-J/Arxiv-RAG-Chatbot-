import os
import chainlit as cl
from dotenv import load_dotenv
from literalai import LiteralClient
from llmClient import GPT35
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import ArxivLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
deployment_name = os.getenv('DEPLOYMENT_NAME')
openai_key = os.getenv('OPENAI_KEY')
openai_endpoint = os.getenv('OPENAI_ENDPOINT')

client = LiteralClient()
prompt = client.api.get_prompt(name="Arxhiv")
prompt = prompt.to_langchain_chat_prompt_template()
prompt.input_variables = ["context", "question"]

gptmodel = GPT35(openai_key,openai_endpoint)
llm = gptmodel.getGPTModel(deployment_name)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

@cl.on_chat_start
async def on_chat_start():
    await cl.Avatar(
        name="ArXivAide",
        url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d1553023f8ea0921fba0debbe92a8c5f840dd9&v=4",
    ).send()

    query = None
    while query == None:
        query = await cl.AskUserMessage(content="Hi 😄, I am ArXivAide! an intelligent assistant for navigating the vast world of academic research. Powered by advanced AI, I specialize in providing insightful answers and summaries based on research papers from the arXiv repository. Whether you're a student, researcher, or enthusiast, I am here to help you access, understand, and utilize cutting-edge scientific knowledge with ease. \n\n What do you want to know about today?", author="ArXivAide", timeout=180).send()

    topic = query['output']
    arxiv_docs = ArxivLoader(query=topic,load_max_docs=3).load()

    if len(arxiv_docs) > 0:
        elements = []
        for doc in arxiv_docs:
            title = doc.metadata['Title']
            published = doc.metadata['Published']
            authors = doc.metadata['Authors']
            text_content = f"By: {authors}\n\nPublished on: {published}"
            text_card = cl.Text(name=title, content=text_content, display="inline")
            elements.append(text_card)

        await cl.Message(content=f"While I study on {topic} to further answer your questions, please find most relevant articles I have found for you: \n\n", author="ArXivAide", elements=elements).send()
        
        pdf_data = []
        for doc in arxiv_docs:
            texts = text_splitter.create_documents([doc.page_content])
            pdf_data.append(texts)
    
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-l6-v2")
        docsearch = Chroma.from_documents(pdf_data[0], embeddings)

        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=docsearch.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={
                "verbose": True,
                "prompt": prompt
            }
        )
        cl.user_session.set("chain", chain)
        cl.user_session.set("docsearch", docsearch)

        await cl.Message(content=f"All set! What do you want to know about `{topic}`?", author="ArXivAide").send()
    else:
        await cl.Message(content=f"No relevant research articles found on `{topic}`", author="ArXivAide").send()

@cl.on_message
async def main(message: cl.Message):
    question = message.content
    chain = cl.user_session.get("chain") 
    docsearch = cl.user_session.get("docsearch")
    cb = client.langchain_callback()

    variables = {
        "context": docsearch.as_retriever(search_kwargs={"k": 1}), 
        "query": question
    }
    results = await chain.ainvoke(variables,callbacks=[cb])
    answer = results["result"]

    await cl.Message(content=answer, author="ArXivAide").send()

