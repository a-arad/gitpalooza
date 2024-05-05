import asyncio
from bot import start_bot
from server import start_web_server

async def main():
    await asyncio.gather(
        start_bot(),
        start_web_server(),
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
