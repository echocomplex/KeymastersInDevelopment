"""

Database for Keymaster's Telegram Bot
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

"""


""" IMPORTS """
import jpype
from os import getcwd


class TelegramBotDatabase:
    def __init__ (self, chatID: int) -> None:
        self.__class = jpype.JClass("TelegramBotDatabase");  # Get Java Class
        self.__Database = self.__class(chatID, ('%s/Database/DatabaseFiles/TelegramBotUsers.db' % getcwd()));  # Init class

    def __del__ (self) -> None:
        self.__Database.closeConnection();

    def addUser (self) -> None:
        self.__Database.addUser();

    def setLanguage (self, language: str) -> None:
        self.__Database.setLanguage(language);

    def getLanguage (self) -> str:
        language: str = self.__Database.getLanguage();
        return language;

    def getLoginStatus (self) -> bool:
        loginStatus: bool = self.__Database.getLoginStatus();
        return loginStatus;

    def setLoginStatus (self, status: bool) -> None:
        self.__Database.setLoginStatus(status);