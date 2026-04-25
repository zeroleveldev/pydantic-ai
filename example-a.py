import asyncio
import os
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from dotenv import load_dotenv

load_dotenv()

# 1. The Schema
class MovieReview(BaseModel):
    title: str
    rating: int
    sentiment: str

# 2. The Model (Native Ollama)
model = OllamaModel(model_name=os.getenv("OLLAMA_MODEL"))

# 3. The Agent 
agent = Agent(model, output_type=MovieReview)

async def main():
    print("--- Pydantic-AI + Ollama ---")
    # result.output is the new standard
    result = await agent.run("Inception was alright, 5/10.")
    
    print(f"Movie: {result.output.title}")
    print(f"Rating: {result.output.rating}/10")
    print(f"Sentiment: {result.output.sentiment}")

if __name__ == "__main__":
    asyncio.run(main())