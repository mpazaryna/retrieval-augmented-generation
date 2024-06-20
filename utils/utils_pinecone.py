import os
from pinecone import Pinecone as PineconeClient
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

def initialize_pinecone(api_key, environment, index_name):
    pinecone = PineconeClient(api_key=api_key, environment=environment)
    embeddings = OpenAIEmbeddings()
    vectorstore = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    retriever = vectorstore.as_retriever()
    return retriever

def create_chain(retriever):
    template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")
    chain = (
        RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
        | prompt
        | model
        | StrOutputParser()
    )
    return chain

def get_response(chain, question):
    return chain.invoke(question)

def initialize_chain():
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = "aws"
    PINECONE_INDEX_NAME = "test001"

    retriever = initialize_pinecone(PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX_NAME)
    chain = create_chain(retriever)
    return chain
