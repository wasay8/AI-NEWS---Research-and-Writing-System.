from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import os
from langchain_groq import ChatGroq
from tools import tool
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["OPEN_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatGroq(model="groq/llama3-70b-8192", temperature=0.9, groq_api_key = groq_api_key, verbose=True)



# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

