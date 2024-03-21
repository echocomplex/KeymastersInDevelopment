"""

Passwords Database for Keymaster's Project
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.


ИЗМЕНИТЬ БАЗУ ДАННЫХ!!!!!!!!!!!!! ТАМ PRIMARY_KEY!!!!!!!!!!!!!

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

    def deletePassword (self, serviceName: str) -> None:
        self.__Database.deletePassword(serviceName);


if (__name__ == "__main__"):
    unit = PasswordsDatabase("mrKalMamba");
    # unit.addUser();
    # unit.addPassword("Yandex", "KirillAndrianov2005");
    # unit.deletePassword("Yandex");
    print(unit.getAll());

    # con = Connection("Passwords.db");
    # cur = con.cursor();
    # cur.execute(""" SELECT * FROM users """);
    # print(cur.fetchall());

    # con = Connection("Passwords.db");
    # cur = con.cursor();
    # cur.execute(""" CREATE TABLE mrPenis (service_name TEXT, password TEXT NOT NULL) """);
    # con.commit();
