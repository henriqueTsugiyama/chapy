import os
import warnings
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from langchain_pinecone import PineconeVectorStore

os.environ.pop('OPENAI_API_KEY', None)  # Remove if it exists

warnings.filterwarnings("ignore")

load_dotenv()

chat_history = []
exit_commands = ['sair', 'quit', 'exit']

def make_exit(reply):
    for exit_command in exit_commands:
        if exit_command in reply:
            print("Ok, tenha um ótimo dia!")
            return True

def chat():
    if __name__ == "__main__":
        embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))
        vectorstore = PineconeVectorStore(
            index_name=os.environ["INDEX_NAME"], embedding=embeddings
        )

        chat = ChatOpenAI(verbose=True, temperature=0, model_name="gpt-3.5-turbo")

        qa = ConversationalRetrievalChain.from_llm(
            llm=chat, chain_type="stuff", retriever=vectorstore.as_retriever()
        )

        question = input("Olá! Você está conversando com o chatty, faça uma pergunta que ele responderá.\n")

        while not make_exit(question):
            res = qa({"question": question, "chat_history": chat_history})
            print('\n')
            print(res['answer'])
            print('\n')

            history = (res["question"], res["answer"])
            chat_history.append(history)
            question = input("Posso ajudar com algo mais?\n")

        print('Até mais!!')


def ask(question=''):
        embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))
        vectorstore = PineconeVectorStore(
            index_name=os.environ["INDEX_NAME_PRODUCTS"], embedding=embeddings
        )

        chat = ChatOpenAI(verbose=True, temperature=0, model_name="gpt-3.5-turbo")

        qa = ConversationalRetrievalChain.from_llm(
            llm=chat, chain_type="stuff", retriever=vectorstore.as_retriever()
        )


        res = qa({"question": question, "chat_history": chat_history})
        print('Digitando ...\n')
        print(res['answer'])
        print('\n')

        history = (res["question"], res["answer"])
        chat_history.append(history)

        return res['answer']
