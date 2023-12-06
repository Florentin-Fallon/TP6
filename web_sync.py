from sys import argv
import requests

def get_content(url):
    response = requests.get(url)
    return response.content

def write_content(content, file):
    with open(file, 'wb') as f:
        f.write(content)

write_content(get_content(argv[1]), './tmp/web_page.html')