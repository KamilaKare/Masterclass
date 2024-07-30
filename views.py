from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key")

class ChatPDF:
    vector_store = None
    retriever = None
    chain = None

    def __init__(self):
        #self.model = ChatOllama(model="llama3")
        self.model = ChatOpenAI(model="gpt-4o-mini")
        #self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
        self.text_splitter  = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100)
        self.prompt = PromptTemplate.from_template(
            """
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
              If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
              \nQuestion: {question} 
              \nContext: {context} 
              \nAnswer:
            """
        )


    def ingest(self, pdf_file_path: str):
        docs = PyPDFLoader(file_path=pdf_file_path).load()
        chunks = self.text_splitter.split_documents(docs)
        
        chunks = filter_complex_metadata(chunks)
       
        # using openai 
        
        vector_store = FAISS.from_documents(documents=chunks, embedding=OpenAIEmbeddings())
        print("hu")
       

        #using ollama
        #vector_store = FAISS.from_documents(
        #documents=chunks,
        #embedding=FastEmbedEmbeddings())
        self.retriever = vector_store.as_retriever()

        self.chain = (
            {"context": self.retriever , "question": RunnablePassthrough()}
                      | self.prompt
                      | self.model
                      | StrOutputParser()
                      )
        
    def ask(self, query: str):
        if not self.chain:
            return "Please, add a PDF document first."

        return self.chain.invoke(query)

    def clear(self):
        self.vector_store = None
        self.retriever = None
        self.chain = None
