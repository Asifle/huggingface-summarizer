import requests
from bs4 import BeautifulSoup


def scrape_blog(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None, "Failed to fetch the blog content."

        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        blog_text = ' '.join([para.get_text().strip() for para in paragraphs if para.get_text().strip()])

        if not blog_text:
            return None, "No text content found on the page."

        return blog_text, None
    except Exception as e:
        return None, f"Error occurred during scraping: {e}"
