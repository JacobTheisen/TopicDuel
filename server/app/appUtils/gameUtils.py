from fastapi import WebSocket
from typing import List, Dict
from models.models import GameSettings, PlayerScore, GameState
from uuid import uuid4
from datetime import datetime
from logger.logger import logger
import random

class TopicDuel:
    def __init__(self, username, gameID):
        self.gameUUID: str = str(uuid4())
        self.date = datetime
        self.host: str = username
        self.gameID: int = gameID
        self.clients: Dict[str, WebSocket] = None
        self.settings: GameSettings = None
        self.score: Dict[str, PlayerScore] = None
        self.topicID: int = None
        self.topicElements: List[str] = None
        self.gameState: GameState = "pre"
    
    def add_player(self, username: str, websocket:WebSocket):
        '''adds player to game with websocket con'''
        self.clients[username] = websocket

    def remove_player(self, username:str):
        '''removes player from game'''
        if username in self.clients:
            self.clients.pop(username) 
        
    

class ConnectionManager:
    def __init__(self):
        self.active_games: Dict[str, TopicDuel] = {} #all active games with reletad users and webscket cons 
        self.clients: Dict[str, str] = {} #mapping to where all connected users are

    async def connect(self, username:str, websocket: WebSocket, game_id:str):

        '''Accept and join/create game returns game'''

        #accept websocket request
        await websocket.accept()
        
        #if not gameid means user wants to create a game, else just join active game
        if not game_id:
            game = await self.create_game(username)
            game.add_player(username, websocket)
            self.active_games[game.gameUUID] = game
            self.clients[username] = game.gameUUID

            logger.debug(username, " created game ", game.gameUUID)

        
        else:
            self.active_games[game_id].add_player(username, websocket)
            self.clients[username] = self.active_games[game_id].gameUUID
            game = self.active_games[game_id]

        logger.debug(username, " joined game ", game.gameUUID)

        return game


    def disconnect(self, username: str):
        '''Disconect user by username'''
        if username in self.clients:
            gameid = self.clients[username]
            self.active_games[gameid].remove_player(username)
            self.clients.pop(username)
            logger.debug(username, " disconnected")

    async def broadcastToGame(self, gameid, message: str):
        '''broadcast msg to all players in game by gameid'''
        for connection in self.active_games[gameid].clients.values():
            await connection.send_text(message)

    async def create_game(self, host):
        '''Create new active game with host'''
        while True:
            game_id = random.randint(1111,9999)
            if game_id in self.active_games:
                continue
            break 
        
        game = TopicDuel(host,game_id)
        return game

    
connectionManager = ConnectionManager()