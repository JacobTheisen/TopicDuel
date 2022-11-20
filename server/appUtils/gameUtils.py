from fastapi import WebSocket
from typing import List, Dict
from models.models import GameSettings, PlayerScore
from uuid import uuid4
from datetime import datetime
from logger.logger import logger
import random

class TopicDuel:
    def __init__(self, username, gameID):
        self.gameUUID:str = str(uuid4())
        self.date = datetime
        self.host: str = username
        self.gameID: int = gameID
        self.clients: Dict[str, WebSocket] = None
        self.settings: GameSettings = None
        self.score: Dict[str, PlayerScore] = None
        self.topicID: int = None
        self.topicElements: List[str] = None
    
    def add_player(self, username: str, websocket:WebSocket):
        self.clients[username] = websocket


class ConnectionManager:
    def __init__(self):
        self.active_games: Dict[str, TopicDuel] = {}

    async def connect(self, username:str, websocket: WebSocket, game_id:str):
        await websocket.accept()
        if not game_id:
            game = await self.create_game(username)
            game.add_player(username, websocket)
            self.active_games[game.gameUUID] = game
        else:
            self.active_games[game_id].add_player(username, websocket)


    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def create_game(self, host):
        while True:
            game_id = random.randint(1111,9999)
            if game_id in self.active_games:
                continue
            break 
        
        game = TopicDuel(host,game_id)
        return game

    


connectionManager = ConnectionManager()