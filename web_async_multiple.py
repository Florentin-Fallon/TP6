import aiohttp
import asyncio
from sys import argv
import os
from urllib.parse import urlparse
import time

async def get_content(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.read()

async def write_content(content, file):
    print(f"Writing content to file: {file}")
    with open(file, 'wb') as f:
        f.write(content)
        print("Write complete")

async def process_url(session, url):
    url = url.strip()
    if url:
        file_name = generate_file_name(url)
        print(f"Processing URL: {url}")
        content = await get_content(session, url)
        print(f"Writing content to: {file_name}")
        await write_content(content, file_name)
        print("Done")

def generate_file_name(url):
    parsed_url = urlparse(url)
    file_name = os.path.join('./tmp', 'web_' + parsed_url.netloc.replace('/', '_') + '.html')
    return file_name

async def process_urls_from_file(file_path):
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            tasks = [process_url(session, url) for url in urls]
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python web_sync.py <file_path>")
    else:
        file_path = argv[1]
        asyncio.run(process_urls_from_file(file_path))

        # Mesure du temps d'exécution pour la version asynchrone
        start_time_async = time.time()
        asyncio.run(process_urls_from_file(file_path))
        end_time_async = time.time()
        print(f"Temps d'exécution (asynchrone): {end_time_async - start_time_async} secondes")