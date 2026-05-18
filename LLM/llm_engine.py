from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def generate_response(prompt):

    response = llm.invoke(prompt)

    return response