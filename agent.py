import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools import tools

#Load environment variables
load_dotenv()

#Initialize Groq LLM

llm = ChatGroq(
    model = "openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)
# Define system instructions
system_prompt = """
You are a helpful Smart Task Productivity Assistant.

Your responsibilities:
1. Create tasks using create_task.
2. List tasks using list_tasks.
3. Update tasks using update_task_status.

Always use tools for actual database operations.
Never claim a task was created or updated without successful tool execution.
Ask the user for missing information.
Use task IDs when updating tasks.
Keep responses short and friendly.
"""

# Create LangChain agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)