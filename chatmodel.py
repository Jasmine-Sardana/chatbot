from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama

# Load environment variables from .env
load_dotenv()

# Get values from .env (or fall back to defaults)
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
model_name = os.getenv("OLLAMA_MODEL", "llama3")

# Initialize ChatOllama with Docker-hosted Ollama
model = ChatOllama(
    model=model_name,
    base_url=base_url
)

# Invoke the model
result = model.invoke(
    input="Assuming a right-angled triangle where one side is 3, the hypotenuse is 5, what is the size of the other side?"
)

print("Full result:")
print(result)
print("Content only:")
print(result.content)
