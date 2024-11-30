from crewai import Process, Agent, Task, Crew
from icp_maker import icp_reader
from firecrawl_tool import url
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.environ.get('GOOGLE_API_KEY')
GenAI = ChatGoogleGenerativeAI(
    model='gemini-1.5-pro',
    google_api_key=google_api_key
)

icp_info = icp_reader()

file_reader = Agent(
    role='Senior JavaScript Object Notation Data Reader',
    goal=f'Effectively the entire read json data from {url} and extract important information',
    backstory="""You are a expert json data reader.""",
    # verbose=True,
    llm = GenAI
)

icp_generator_agent = Agent(
    role='Senior ICP Generator Agent',
    goal = f'Give me the target audience for {icp_info} industry for Ideal customer profile',
    backstory="""You are an expert icp generator that can generate detailed Ideal customer profile""",
    # verbose=True,
    llm=GenAI
)