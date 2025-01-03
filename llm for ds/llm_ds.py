from crewai import Crew, Agent, Task
from langchain_openai import ChatOpenAI
import pandas as pd

df = pd.read_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIVshort.csv')
selected_column = df['body']

llm = ChatOpenAI(
    model="llama3.2:1b",
    base_url="http://localhost:11434/v1"
)

file_reader = Agent(
    role='Senior DataScience Engineer',
    goal=f'Effectively read the entire data from {selected_column} and extract important information',
    backstory="""You're an expert data extractor for csv file.""",
    llm=llm
)

file_reader_task = Task(
    description="""Read the data from the body column of the csv file and extract information like
    Base table: Ardertisement id, Source, Manufacture of airplane, Model of airplane, Registration number, Price, TTAF, Paint Year, Interior Year.
    Engine table: Make of Engine, Model of Engine, Serial Number, TSN, CSN, TSO, TBO, Date of overhaul, Time to HSI, Date of HSI, Hours since HSI.
    """,
    expected_output='Extract the important details and save them in the json file according to each row of the body column.',
    agent=file_reader,
    output_file='basic_engine_info.json'
)

crew = Crew(
    agents=[file_reader],
    tasks=[file_reader_task],
)

crew.kickoff()