import asyncio

async def p1():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(p1())
    task2 = asyncio.create_task(p1())

    await asyncio.gather(task1, task2)

asyncio.run(main())