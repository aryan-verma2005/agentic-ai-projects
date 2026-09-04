from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.models.google import GeminiInteractions
from agno.team import Team

load_dotenv()

eng_agent = Agent(name='English Agent',role='you answer questions in engish')
chi_agent = Agent(name='Chinese Agent',role='you answer questions in chinese')
hindi_agent = Agent(name='Hindi Agent',role='you answer questions in hindi')

team_leader = Team(
    name='Answer and translation Team',
    members=[eng_agent,chi_agent,hindi_agent],
    model=GeminiInteractions(id="gemini-3.7-flash"),
    markdown=True,
    show_members_responses=True,
    instructions=""" All member agents must respond to answer the query in their specific language. 
                        Do not route to just one agent.
                        Output the response of all agents.
                """
)

team_leader.print_response("What is the capital of India?")