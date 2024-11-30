from crewai_tools import ScrapeWebsiteTool

tool = ScrapeWebsiteTool(website_url='https://designgaga.ca/')
text = tool.run()
print(text)
