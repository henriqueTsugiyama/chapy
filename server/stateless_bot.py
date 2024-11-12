import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
os.environ.pop('OPENAI_API_KEY', None)  # Remove if it exists
load_dotenv()

embeddings = OpenAIEmbeddings()
vectorstore = PineconeVectorStore(
        index_name=os.environ.get("INDEX_NAME"), embedding=embeddings
)

chat = ChatOpenAI(verbose=True, temperature=0, model_name="gpt-3.5-turbo")

qa = RetrievalQA.from_chain_type(
    llm=chat, chain_type="stuff", retriever=vectorstore.as_retriever()
)    

res = qa.invoke("Como verificar se o remote está UTC-3?")
print(res)

res = qa.invoke("Como atualizar o firmware?")
print(res)

res = qa.invoke("Como colocar o id no módulo do firetek 48?")
print(res) 

