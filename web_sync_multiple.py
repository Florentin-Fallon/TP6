from sys import argv
import os
import requests
from urllib.parse import urlparse
import time

def get_content(url):
    response = requests.get(url)
    return response.content

def write_content(content, file):
    print(f"Writing content to file: {file}")
    with open(file, 'wb') as f:
        f.write(content)
        print("Write complete")

def process_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()
            if url:
                file_name = generate_file_name(url)
                print(f"Processing URL: {url}")
                content = get_content(url)
                print(f"Writing content to: {file_name}")
                write_content(content, file_name)
                print("Done")

def generate_file_name(url):
    parsed_url = urlparse(url)
    file_name = os.path.join('./tmp', 'web_' + parsed_url.netloc.replace('/', '_') + '.html')
    return file_name

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python web_sync.py <file_path>")
    else:
        file_path = argv[1]
        process_urls_from_file(file_path)

        # Mesure du temps d'exécution pour la version synchrone
        start_time_sync = time.time()
        process_urls_from_file(file_path)
        end_time_sync = time.time()
        print(f"Temps d'exécution (synchrone): {end_time_sync - start_time_sync} secondes")