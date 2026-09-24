from agents import Agent, WebSearchTool, ModelSettings
from dotenv import load_dotenv
import os

load_dotenv(override=True)
MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")

INSTRUCTIONS = """
You are a search agent's assistant, and before starting the search, you need to ask the client three clarifying questions.
"""

settings = ModelSettings(tool_choice="required")

clarify_agent = Agent(name="Search Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, model_settings=settings)