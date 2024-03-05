"""

Passwords Database for Keymaster's Project
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

"""



""" IMPORTS """
from sqlite3 import Connection



class PasswordsDatabase:
    def __init__ (self, username: str) -> None:
        self.__connection = Connection("Passwords.db");
        self.__cursor = self.__connection.cursor();
        self.__username: str = username;

    def __del__ (self) -> None:
        self.__connection.close();

    def addUser (self) -> None:
        self.__cursor.execute(
            """ 
            CREATE TABLE %s (service_name TEXT PRIMARY KEY, password TEXT NOT NULL) 
            """ % (self.__username)
        );
        self.__connection.commit();

    def addPassword (self, serviceName: str, servicePassword: str) -> None:
        self.__cursor.execute(
            """
            INSERT INTO %s (service_name, password)
            VALUES (?, ?)
            """ % (self.__username), (serviceName, servicePassword)
        );
        self.__connection.commit();

    def getAll (self) -> tuple:
        self.__cursor.execute(
            """
            SELECT * FROM %s
            """ % (self.__username,)
        )
        all: tuple = tuple(self.__cursor.fetchall());
        return all;

    def deletePassword (self, serviceName) -> None:
        self.__cursor.execute(
            """
            DELETE FROM %s 
            WHERE service_name = ?
            """ % (self.__username), (serviceName,)
        );
        self.__connection.commit();


if (__name__ == "__main__"):
    unit = PasswordsDatabase("mrKalMamba");
    # unit.addUser();
    # unit.addPassword("Yandex", "KirillAndrianov2005");
    # `unit.deletePassword("Yandex");
    print(unit.getAll());

    # con = Connection("Passwords.db");
    # cur = con.cursor();
    # cur.execute(""" SELECT * FROM users """);
    # print(cur.fetchall());

    # con = Connection("Passwords.db");
    # cur = con.cursor();
    # cur.execute(""" CREATE TABLE mrPenis (service_name TEXT, password TEXT NOT NULL) """);
    # con.commit();
