from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse 
from json import loads

app = FastAPI()
with open("main.html", "r") as f:
	html = f.read()


@app.get("/")
async def root():
	return HTMLResponse(html)


@app.websocket("/messages")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	while True:
		data = await websocket.receive_text()
		data = loads(data)
		await websocket.send_text(f"{data['number']} : {data['content']}")
		