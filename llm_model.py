from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import TextLoader
from langchain.llms import OpenAI

@app.post("/chat/")
def chat_with_document(query: str, document_path: str):
    loader = TextLoader(document_path)
    retriever = loader.as_retriever()
    chain = ConversationalRetrievalChain.from_llm(llm=OpenAI(), retriever=retriever)
    response = chain.run(query)
    return {"response": response}
