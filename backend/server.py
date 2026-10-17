"""Educational hotel lamp WebSocket API behind nginx."""
import json
import sqlite3
from pathlib import Path
from aiohttp import web, WSMsgType

DB = Path(__file__).resolve().parent.parent / "lamp.sqlite3"
CLIENTS = set()

def connect():
    db = sqlite3.connect(DB)
    db.execute("CREATE TABLE IF NOT EXISTS lamp (id INTEGER PRIMARY KEY CHECK (id=1), state INTEGER NOT NULL CHECK (state IN (0,1)))")
    db.execute("INSERT OR IGNORE INTO lamp (id,state) VALUES (1,0)")
    db.commit()
    return db

def current():
    with connect() as db:
        return bool(db.execute("SELECT state FROM lamp WHERE id=1").fetchone()[0])

def update(state):
    with connect() as db:
        db.execute("UPDATE lamp SET state=? WHERE id=1", (int(state),))
        db.commit()

async def state_handler(request):
    return web.json_response({"on": current()})

async def socket_handler(request):
    ws = web.WebSocketResponse(heartbeat=30)
    await ws.prepare(request)
    CLIENTS.add(ws)
    await ws.send_json({"type": "state", "on": current()})
    try:
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                try:
                    payload = json.loads(msg.data)
                    if payload.get("type") != "set" or type(payload.get("on")) is not bool:
                        raise ValueError('expected {"type":"set","on":true/false}')
                    update(payload["on"])
                    for client in list(CLIENTS):
                        if not client.closed:
                            await client.send_json({"type": "state", "on": payload["on"]})
                except (ValueError, json.JSONDecodeError) as exc:
                    await ws.send_json({"type": "error", "message": str(exc)})
    finally:
        CLIENTS.discard(ws)
    return ws

app = web.Application()
app.router.add_get("/api/state", state_handler)
app.router.add_get("/ws", socket_handler)

if __name__ == "__main__":
    connect().close()
    # nginx exposes port 8080; backend only listens on loopback
    web.run_app(app, host="127.0.0.1", port=8765)
