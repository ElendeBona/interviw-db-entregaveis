from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.postgres import PostgresTools
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host="localhost",
    port=5432,
    db_name="dbinterview",
    user="postgres",
    password="postgres",
    table_schema="public",
)

# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools],
              model=Groq(id="llama-3.3-70b-versatile"),
              description="Você é o melhor especialista em streaming de filmes!"
              )

agent.print_response("Fale todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Faça uma query para pegar as tabelas payment customer rental category store inventory no banco de dados
""")

agent.print_response("""
Faça uma análise super complexa sobre o mercado de filmes  
""")

agent.print_response("""
Faça uma análise com uma query para pegar os filmes mais assistidos no banco de dados  
""")
