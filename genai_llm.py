from crewai import Process, Agent, Task, Crew
from firecrawl_tool import url
from langchain_google_genai import ChatGoogleGenerativeAI
from loading_env import google_api_key


def icp_reader():
    with open('basic_info.md', 'r', encoding='utf-8') as file:
        icp_info = file.read()
    return icp_info

GenAI = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
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

file_reader_task = Task(
    description='Read the scraped data JSON data and extract important information.',
    expected_output='Must add all these details Business Name, Industry, Services, Location, Contact Info, etc and save the entire data in the output file',
    agent=file_reader,
    output_file='basic_info.md'
)

icp_generator_task = Task(
    description="""Give me the target audience for industry for Ideal customer profile also add goegraphic loaction, pain points etc. 
    """,
    expected_output='Generate the Ideal Customer Profile from the data and only save the ICP data in the output file',
    agent=icp_generator_agent,
    output_file='icp_data.md',
)

crew = Crew(
    agents=[file_reader],
    tasks=[file_reader_task],
    verbose=1,
    process=Process.sequential
)

result = crew.kickoff()
print(result)