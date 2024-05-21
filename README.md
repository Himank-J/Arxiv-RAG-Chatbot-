# Chatbot for research paper study using Chainlit, Literal AI and LangChain

This project demonstrates how to create an observable research paper engine using the arXiv API to retrieve the most similar papers to a user query. The retrieved papers are embedded into a Chroma vector database, based on Retrieval Augmented Generation (RAG). The user can then ask questions from the retrieved papers. The application provides a chat interface via Chainlit, allowing for a more interactive and friendly user experience. To track performance and observe the application's behavior, the application is integrated with Literal AI, an observability framework.

## Key Features

- Retrieve relevant papers based on user query using the LangChain wrapper for `arXiv` API
- Embed retrieved papers in a Chroma database to initiate a RAG pipeline
- Create optimized prompts for the RAG pipeline using Literal AI
- Develop a Chainlit application for the above
- Integrate observability features to track app performance and generations using Literal

## Tech Stack

This project leverages the following technologies:

- [Chainlit](https://github.com/Chainlit/chainlit): Used for deploying a frontend application for the chatbot.
- [Literal AI](https://docs.getliteral.ai/get-started/overview): For creating, optimizing and testing prompts for the RAG pipeline, and for integrating observability features in the app.
- [LangChain](https://github.com/langchain-ai/langchain): For retrieving arXiv queries, and managing the app's language understanding and generation.
- [OpenAI](https://openai.com/): Ensures high-speed computations utilizing the GPT-3.5 models.
- [Chroma](https://github.com/chroma-core/chroma): For creating the vector store to be used  in retrieval.

## Prerequisites

- Python 3.8 or later
- An OpenAI API key
- A Literal AI API Key

## Project Structure

- `llmClient.py`: Contain open ai client connection for llm calls
- `main.py`: Main script to run the semantic research paper engine with a Chainlit frontend application.
- 
### Running the Chatbot with Chainlit Frontend
The application can be run by first deploying the Chainlit web app. To do this, run:
```bash
chainlit run main.py -w
```
This command will start a local web server at [https:/localhost:8000](https:/localhost:8000). It is important to do this first before hosting the web application.

## DEMO

### Chatbot App
https://github.com/Himank-J/Arxiv-RAG-Chatbot-/assets/55919214/f45cd7d6-4ac0-4f7d-ba23-a5b8f7a44111

### Threads

A thread represents a conversation session between an assistant and a user. You should be able to see all the conversations a user has had in the application.

<img width="1440" alt="Screenshot 2024-05-21 at 12 55 50 AM" src="https://github.com/Himank-J/Arxiv-RAG-Chatbot-/assets/55919214/e99d8735-be13-4c30-943a-4fd0988fdb97">

### Runs

A run is a sequence of steps taken by an agent or a chain. This gives details of all steps taken each time a chain or agent is executed. With this tab, we get both the input and the output for each user query.

<img width="1440" alt="Screenshot 2024-05-21 at 12 55 22 AM" src="https://github.com/Himank-J/Arxiv-RAG-Chatbot-/assets/55919214/f37e9f62-be58-461a-905f-110291251863">


### Generations

A generation contains both the input sent to an LLM and its completion. This gives key details including the model used for a completion, the token count, as well as the user requesting the completion, if you have configured multiple user sessions.

<img width="1440" alt="Screenshot 2024-05-21 at 12 56 29 AM" src="https://github.com/Himank-J/Arxiv-RAG-Chatbot-/assets/55919214/e091d26d-db45-4759-bd2c-5c6628c08637">




