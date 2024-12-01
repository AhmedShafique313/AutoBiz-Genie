from crewai import Process, Agent, Task, Crew
from firecrawl_tool import scrapping_function
from langchain_google_genai import ChatGoogleGenerativeAI
from loading_env import google_api_key

def run_crewai_system(input_url):
    scraped_data = scrapping_function(input_url)

    GenAI = ChatGoogleGenerativeAI(
        model='gemini-1.5-flash',
        google_api_key=google_api_key
    )

    file_reader = Agent(
        role='Senior JavaScript Object Notation Data Reader',
        goal=f'Effectively read the entire JSON data from {scraped_data} and extract important information',
        backstory="""You are an expert JSON data reader.""",
        llm=GenAI
    )

    file_reader_task = Task(
        description='Read the scraped data JSON data and extract important information.',
        expected_output='Must add all these details: Business Name, Industry, Services, Location, Contact Info, etc., and save the entire data in the output file',
        agent=file_reader,
        output_file='basic_info.md'
    )

    crew = Crew(
        agents=[file_reader],
        tasks=[file_reader_task],
        # verbose=1,
        # process=Process.sequential
    )

    crew.kickoff()

    icp_info = icp_reader()

    icp_generator_agent = Agent(
        role='Senior ICP Generator Agent',
        goal=f'Give me the target audience for {icp_info} industry for Ideal customer profile',
        backstory="""You are an expert ICP generator that can generate a detailed Ideal customer profile.""",
        llm=GenAI
    )

    icp_generator_task = Task(
        description="""Give me the target audience for the industry for Ideal customer profile. Also add geographic location, pain points, etc.""",
        expected_output='Generate the Ideal Customer Profile from the data and only save the ICP data in the output file. Make some bullet points and create a clear document.',
        agent=icp_generator_agent,
        output_file='icp_data.md',
    )

    crew = Crew(
        agents=[icp_generator_agent],
        tasks=[icp_generator_task],
        # verbose=1,
        # process=Process.sequential
    )

    crew.kickoff() 

def icp_reader():
    with open('basic_info.md', 'r', encoding='utf-8') as file:
        icp_info = file.read()
    return icp_info

run_crewai_system('designgaga.ca')