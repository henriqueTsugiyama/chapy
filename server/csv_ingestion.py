import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document
from flask import jsonify
import csv

os.environ.pop('OPENAI_API_KEY', None)  # Remove if it exists
load_dotenv()

file_path = './data/csv/tabela_produtos_dezembro_2023.csv'
documents = []
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader) 
    print(f"Header: {header}")

    for row in csv_reader:
       doc = Document(metadata= {
            "produto": row[0],
            "origem": row[1],
            "unidade": row[2],
            "preço": row[3],
            "preço peça": row[4],
        },page_content=f"O nome do produto é {row[0]}, com origem da fábrica {row[1]}. Sua unidade é considerada por {row[2]}, sendo seu preço de venda R${row[3]} e de cada unidade podemos vender a R$ {row[4]} a peça. Caso o preço da peça seja R$ 0,00 significa que a venda por peça não está disponível.")
       
       documents.append(doc)

print('Documents =>', documents)
#different from pdf documents, i don`t think there is a reason to split these csv documents because they are a lot smaller. Therefore, not needing to create smaller chunks of datas from the documents

#create embeddings and upload them to pinecone
embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))

PineconeVectorStore.from_documents(documents, embeddings, index_name=os.environ.get("INDEX_NAME_PRODUCTS"))
