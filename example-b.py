import os
from smolagents import CodeAgent, LiteLLMModel
from dotenv import load_dotenv

load_dotenv()

# Setup local model
model = LiteLLMModel(
    model_id=f"ollama_chat/{os.getenv('OLLAMA_MODEL')}",
    api_base="http://localhost:11434", 
    api_key="ollama" 
)

# Set add_base_tools to False if you want to avoid extra dependencies
# The agent can still do math/logic because it uses its own Python Interpreter!
agent = CodeAgent(tools=[], model=model, add_base_tools=False)

print("\n-- Smolagents + Ollama ---")
agent.run("calculate 144 * 2 and tell me if it's greater than 250.")
