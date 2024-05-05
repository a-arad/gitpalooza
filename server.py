from aiohttp import web

async def handle_github_webhook(request):
    data = await request.json()
    print("Received GitHub data:", data)
    return web.Response(text="Webhook processed", status=200)

async def start_web_server():
    app = web.Application()
    app.router.add_post('/github-webhook', handle_github_webhook)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080) # use ngrok for now
    await site.start()
