import asyncio
from dotenv import load_dotenv
load_dotenv()
import os

print("KEY:", os.getenv("OPENAI_API_KEY"))
print("BASE:", os.getenv("OPENAI_BASE_URL"))
from src.agents.my_agent import ipl_agent

async def analyze(text: str):
    
    """Run agent and return parsed result."""
    result = await ipl_agent.run(text)

    return result.output  


async def display(result):
    print("\nAnalysis Result:")
    print(f"Team: {result.team}")
    print(f"Summary:\n{result.summary}")
    print("-" * 50)


async def main():
    print("Welcome to IPL Team Analyzer!")

    while True:
        text = input("\nEnter IPL Team name (or 'exit'): ").strip()

        if text.lower() == "exit":
            print("Goodbye!")
            break

        if not text:
            print("Please enter a team name.")
            continue

        try:
            result = await analyze(text)
            await display(result)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
    