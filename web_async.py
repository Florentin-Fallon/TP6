import aiohttp
import aiofiles
import asyncio
from sys import argv

async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            return await response.read()

async def write_content(content, file):
    async with aiofiles.open(file, 'wb') as f:
        await f.write(content)

async def main():
    if len(argv) != 2:
        print("Usage: python script.py <url>")
        return

    url = argv[1]
    content = await get_content(url)
    tasks = [get_content(url), write_content(content, './tmp/web_page_async.html')]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
