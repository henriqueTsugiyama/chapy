from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

# Initialize the CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator=".",  # Using a period as a separator
    chunk_size=50,  # Maximum characters per chunk
    chunk_overlap=10  # Overlap of 10 characters
)

text = """LangChain is a framework for developing applications powered by language models. 
It enables users to connect their models with external data sources. 
This framework provides tools to build intelligent agents."""

# Perform the splitting
chunks = text_splitter.split_text(text)

# # Output the chunks
# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i + 1}:")
#     print(chunk)
#     print("\n---\n")
# 


# Create documents with metadata
texts_with_metadata = [
    Document(page_content=chunk, metadata={"source": f"chunk_{i + 1}"})
    for i, chunk in enumerate(chunks)
]
print(texts_with_metadata)
# Output documents with metadata
for doc in texts_with_metadata:
    print(doc)
    print(f"Document Source: {doc.metadata}")
    print(doc.page_content)
    print("\n---\n")