BEGIN;

CREATE TABLE Users (
    id SERIAL NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
);

ALTER TABLE ONLY Users 
    ADD CONSTRAINT user_pk PRIMARY KEY (id);

CREATE TABLE UsersInGame (
    id SERIAL NOT NULL,
    userid TEXT NOT NULL,
    gameid INT NOT NULL,
);

ALTER TABLE ONLY UsersInGame
    ADD CONSTRAINT usersInGame_pk PRIMARY KEY (id);

CREATE TABLE GameLog (
    id TEXT NOT NULL,
    joinid INT NOT NULL,
    mapid INT NOT NULL,
    host TEXT NOT NULL,
    timestamp_utc TIMESTAMP WITH TIME ZONE,
    winner TEXT,
    gametime INT,
);

ALTER TABLE ONLY GameLog
    ADD CONSTRAINT gameLog_pk PRIMARY KEY (id);

CREATE TABLE Games (
    id SERIAL NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
);

ALTER TABLE ONLY Games
    ADD CONSTRAINT game_pk PRIMARY KEY (id);

CREATE TABLE GameAnswers (
    id SERIAL NOT NULL,
    answer TEXT NOT NULL,
    gameid int NOT NULL,
)

ALTER TABLE ONLY GameAnswers
    ADD CONSTRAINT gameAnswers_pk PRIMARY KEY (id);

ALTER TABLE ONLY UsersInGame
    ADD CONSTRAINT game_usergame_fk FOREIGN KEY (gameid) REFERENCES GameLog(id);

ALTER TABLE ONLY UsersInGame
    ADD CONSTRAINT user_usergame_fk FOREIGN KEY (userid) REFERENCES Users(id);

ALTER TABLE ONLY GameLog
    ADD CONSTRAINT game_mapid_fk FOREIGN KEY (mapid) REFERENCES Games(id);

ALTER TABLE ONLY GameAnswers
    ADD CONSTRAINT answer_game_fk FOREIGN KEY (gameid) REFERENCES Games(id);