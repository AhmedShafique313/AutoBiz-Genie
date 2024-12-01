from genai_llm import run_crewai_system
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
   if request.method== 'POST':
      url = request.form['url']
      run_crewai_system(url)
      icp_file_path = r'C:\Users\Ahmed Shafique\Documents\Projects\AutoBiz Genie\icp_data.md'
      try:
         with open(icp_file_path, 'r', encoding='utf-8') as file:
            icp_content = file.read()
      except FileNotFoundError:
         icp_content = "No ICP data found. Please check the URL and try again."
      return render_template('index.html', scraped_data = icp_content)
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)