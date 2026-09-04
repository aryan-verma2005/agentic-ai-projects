from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
from agno.models.google import GeminiInteractions

load_dotenv()

db = SqliteDb(db_file='agno.db')

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3.6-27b"),
        markdown=True,
        add_history_to_context=True,
        enable_agentic_memory=True  # Enable memory functionality
    )

agent = build_agent()
user_id = 'aryan@gmail.com'
agent.print_response('i am aryan and i am a data analyst', user_id=user_id)
agent.print_response('who am i ?', user_id=user_id)

# Retrieve memories from database
memories = db.get_user_memories(user_id=user_id)

print("MEMORIES: ")
pprint(memories)