from pydantic import BaseModel
from typing import List
from enum import Enum

class User(BaseModel):
    name: str
    password: str

class GameSettings(BaseModel):
    time: int
    topic: str

class PlayerScore(BaseModel):
    ptl: List[str]
    pts: int

class Choices(Enum):
    start = 'start'
    options = 'options'
    live = "live"
    ended = "ended"

class GameState(BaseModel):
    state: Choices
