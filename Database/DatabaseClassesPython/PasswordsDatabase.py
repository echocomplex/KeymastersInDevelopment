"""

Passwords Database for Keymaster's Project
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

"""


""" IMPORTS """
import jpype
from os import getcwd


class PasswordsDatabase:
    def __init__ (self, username: str) -> None:
        self.__class = jpype.JClass("PasswordDatabase");  # Get Java Class
        self.__Database = self.__class(username, ('%s/Database/DatabaseFiles/Passwords.db' % getcwd()));  # Init class

    def __del__(self) -> None:
        self.__Database.closeConnection();

    def addUser (self) -> None:
        self.__Database.addUser();

    def addPassword (self, serviceName: str, servicePassword: str) -> None:
        self.__Database.addPassword(serviceName, servicePassword);

    def getAll (self) -> tuple:
        allData: tuple = self.__Database.getAll();
        result: list = [];
        for row in allData:
            string_row = [str(cell) for cell in row];
            result.append(tuple(string_row));
        return tuple(result);

    def deletePassword (self, serviceName: str, password: str) -> None:
        self.__Database.deletePassword(serviceName, password);
