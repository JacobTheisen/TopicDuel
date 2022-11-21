from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect
from appUtils.authUtils import authUtils
from appUtils.gameUtils import connectionManager, TopicDuel
from models.models import User
from logger.logger import logger

app = FastAPI()

@app.get("/", tags=["root"])
async def hello_world():
    return {"Hello" : "World"}


@app.post("/signup", tags=["user"])
async def user(user: User):
    token = await authUtils.create_access_token(user.name)
    return token

@app.get("/protected", tags=["user","auth"])
async def protected(token : str = Depends(authUtils.validate_access_token)):
    return token

@app.get("/ws", tags=["topicDuel"])
async def websocket_ep(websocket: WebSocket, game_id:str = None, token : str = Depends(authUtils.validate_access_token)):
    username = token["sub"]
    game: TopicDuel = await connectionManager.connect(username, websocket, game_id)
    try:
        await game.
    except WebSocketDisconnect:
        connectionManager.disconnect(username)