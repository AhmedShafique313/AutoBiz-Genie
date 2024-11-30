from firecrawl import FirecrawlApp

def scrapping_function(website_url):
    app = FirecrawlApp(api_key=firecrawl_api_key)
    specific_pages = [
        website_url,  # Main page
        f"{website_url}/about-us",
        f"{website_url}/services",
        f"{website_url}/careers",
        f"{website_url}/portfolio",
        f"{website_url}/contact"
    ]
    scraped_data = {}
    for page in specific_pages:
        scrape_result = app.scrape_url(page, params={'formats': ['markdown']})
        scraped_data[page] = scrape_result.get('markdown', 'No content available')
    with open('scraped_data.json', 'w', encoding='utf-8') as md_file:
        json.dump(scraped_data, md_file, ensure_ascii=False, indent=4)
    return scraped_data