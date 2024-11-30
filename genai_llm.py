from crewai import Process, Agent, Task, Crew
from firecrawl_tool import scrapping_function
from langchain_google_genai import ChatGoogleGenerativeAI
from loading_env import google_api_key

file_path = scrapping_function('designgaga.ca')

GenAI = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    google_api_key=google_api_key
)

file_reader = Agent(
    role='Senior JavaScript Object Notation Data Reader',
    goal=f'Effectively the entire read json data from {file_path} and extract important information',
    backstory="""You are a expert json data reader.""",
    llm = GenAI
)

file_reader_task = Task(
    description='Read the scraped data JSON data and extract important information.',
    expected_output='Must add all these details Business Name, Industry, Services, Location, Contact Info, etc and save the entire data in the output file',
    agent=file_reader,
    output_file='basic_info.md'
)

crew = Crew(
    agents=[file_reader],
    tasks=[file_reader_task],
    verbose=1,
    process=Process.sequential
)

result = crew.kickoff()
print(result)