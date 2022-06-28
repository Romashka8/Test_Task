from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
with open("main.html", "r") as f:
	html = f.read()


@app.get("/")
async def root():
	return HTMLResponse(html)


@app.websocket("/messages")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	count = 1
	while True:
		data = await websocket.receive_json()
		data["count"] = count
		count += 1
		await websocket.send_json(data)
		