from dotenv import load_dotenv

# Load environment variables from .env
# returns True if .env file was loaded
load_dotenv()

import os
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Get values from .env (or fall back to defaults)
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
model_name = os.getenv("OLLAMA_MODEL", "llama3")

# Initialize ChatOllama with Docker-hosted Ollama
model = ChatOllama(
    model=model_name,
    base_url=base_url)

human_message_1 = HumanMessage(content="Hi, my name is John.")
human_message_2 = HumanMessage(content="What is my name?")
print(f"Question: {human_message_1.content}")
result = model.invoke(input=[human_message_1])
print(f"Answer from AI: {result.content}")
print(f"Question: {human_message_2.content}")
result = model.invoke(input=[human_message_2])
print(f"Answer from AI: {result.content}")