from firecrawl_tool import scrapping_function
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
   if request.method== 'POST':
      url = request.form['url']
      scraped_data = scrapping_function(url)
      return render_template('index.html', scraped_data=scraped_data)
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)