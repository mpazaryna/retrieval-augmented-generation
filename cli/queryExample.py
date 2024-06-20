#!/usr/bin/env python
# coding: utf-8

import os
from pinecone import Pinecone as PineconeClient
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

# Environment variables
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_ENVIRONMENT = "aws"
PINECONE_INDEX_NAME = "test001"

# Initialize Pinecone client
pinecone = PineconeClient(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

# Set up embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Pinecone.from_existing_index(index_name=PINECONE_INDEX_NAME, embedding=embeddings)
retriever = vectorstore.as_retriever()

# Define RAG prompt template
template = """Answer the question based only on the following context:
{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Initialize language model
model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")

# Define chain of runnables
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
)

# Invoke the chain with questions
response1 = chain.invoke("what are minimum viable products?")
response2 = chain.invoke("what is the product company gap and how can it be solved?")

# Print responses
print("Response to 'what are minimum viable products?':", response1)
print("Response to 'what is the product company gap and how can it be solved?':", response2)
