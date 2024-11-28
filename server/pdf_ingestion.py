import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

os.environ.pop('OPENAI_API_KEY', None)  # Remove if it exists
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))

# create documents from pdfs file
doc1 = PyPDFLoader("./data/pdf/Firetek/FTQ_System_64.pdf").load()
doc2 = PyPDFLoader("./data/pdf/Firetek/FTM_System_48.pdf").load()

for doc in doc2:
    doc1.append(doc)

document = doc1
print('Documents =>', document)
#split documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(document)
print(f"created {len(texts)} chunks")
print('\nSplitted texts=>', texts)
#create embeddings and upload them to pinecone
embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))
PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ.get("INDEX_NAME"))