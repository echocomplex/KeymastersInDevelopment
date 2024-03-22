"""

Users Database for Keymaster's Project
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

P.S. Command to create Database: CREATE TABLE users (username TEXT PRIMARY KEY, language VARCHAR(2) NOT NULL, chat_id INTEGER,  password TEXT NOT NULL)

"""



""" IMPORTS """
import jpype
from os import getcwd


class UsersDatabase:
    def __init__ (self, username: str) -> None:
        self.__class = jpype.JClass("UsersDatabase");  # Get Java Class
        self.__Database = self.__class(username, ('%s/Database/DatabaseFiles/Users.db' % getcwd()));  # Init class

    def __del__ (self) -> None:
        self.__Database.closeConnection();

    @staticmethod
    def findUsernameByChatID (chat_id: int) -> str:
        Class = jpype.JClass("UsersDatabase");  # Get Java Class
        username: str = Class.findUsernameByChatID(chat_id, ('%s/Database/DatabaseFiles/Users.db' % getcwd()));
        if (username == ""):
            raise Exception("NO USERNAME BY THIS CHAT_ID IN DATABASE");
        return username;

    @staticmethod
    def checkChatID(chat_id: int) -> bool:
        Class = jpype.JClass("UsersDatabase");  # Get Java Class
        username: str = Class.findUsernameByChatID(chat_id, ('%s/Database/DatabaseFiles/Users.db' % getcwd()));
        return username == "";

    def addUser (self, language: str, password) -> None:
        self.__Database.addUser(language, password);

    def setLanguage (self, language: str) -> None:
        self.__Database.setLanguage(language);

    def getLanguage (self) -> str:
        language: str = self.__Database.getLanguage();
        return language;

    def setPassword (self, password: str) -> None:
        self.__Database.setPassword(password);

    def authenticate (self, password: str) -> bool:
        return self.__Database.authenticate(password);

    def setChatID (self, chatID: int) -> None:
        self.__Database.setChatID(chatID);

    def getChatID (self) -> int:
        chat_id: int = self.__Database.setChatID();
        return chat_id;
