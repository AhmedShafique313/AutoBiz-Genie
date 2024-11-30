import os
from dotenv import load_dotenv
load_dotenv()

firecrawl_api_key = os.environ.get('FIRECRAWL_API_KEY')
google_api_key = os.environ.get('GOOGLE_API_KEY')