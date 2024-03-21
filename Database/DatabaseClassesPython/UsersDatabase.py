"""

Users Database for Keymaster's Project
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

"""



""" IMPORTS """
from sqlite3 import Connection
from hashlib import sha256



class UsersDatabase:
    def __init__ (self, username: str) -> None:
        self.__connection = Connection("Database/Users.db");
        self.__cursor = self.__connection.cursor();
        self.__username: str = username;

    def __del__ (self) -> None:
        self.__connection.close();

    @staticmethod
    def __hashPassword (password: str) -> str:
        return sha256(password.encode('utf-8')).hexdigest();

    @staticmethod
    def findUsernameByChatId (self, chat_id: int) -> str:
        connection = Connection("Users.db");
        cursor = connection.cursor();
        cursor.execute(
            """
            SELECT username
            FROM users
            WHERE chat_id = ?
            """, (chat_id,));
        username: str = self.__cursor.fetchone()[0];
        connection.close();
        if (len(username) == 0):
            raise Exception("NO USERNAME BY THIS CHAT_ID IN DATABASE");
        return username;

    def addUser (self, language: str, email, password) -> None:
        hashPassword: str = self.__hashPassword(password);
        self.__cursor.execute(
            """
            INSERT OR IGNORE INTO users (username, language, email, password) 
            VALUES (?, ?, ?, ?)
            """,
            (self.__username, language, email, hashPassword));
        self.__connection.commit();

    def setLanguage (self, language: str) -> None:
        self.__cursor.execute(
            """
            UPDATE users
            SET language = ?
            WHERE username = ?
            """, (language, self.__username));
        self.__connection.commit();

    def getLanguage (self) -> str:
        self.__cursor.execute(
            """
            SELECT language
            FROM users
            WHERE username = ?
            """, (self.__username,));
        language: str = self.__cursor.fetchone()[0];
        return language;

    def setEmail (self, email: str) -> None:
        self.__cursor.execute(
            """
            UPDATE users
            SET email = ?
            WHERE username = ?
            """, (email, self.__username));
        self.__connection.commit();

    def getEmail (self) -> str:
        self.__cursor.execute(
            """
            SELECT email
            FROM users
            WHERE username = ?
            """, (self.__username,));
        email: str = self.__cursor.fetchone()[0];
        return email;

    def setPassword (self, password: str) -> None:
        hashPassword: str = self.__hashPassword(password);
        self.__cursor.execute(
            """
            UPDATE users
            SET password = ?
            WHERE username = ?
            """, (hashPassword, self.__username));
        self.__connection.commit();

    def authenticate (self, password: str) -> bool:
        self.__cursor.execute(
            """
            SELECT password
            FROM users
            WHERE username = ?
            """, (self.__username,));
        hashPasswordInDatabase: str = self.__cursor.fetchone()[0];
        hashPasswordToCheck: str = self.__hashPassword(password);
        return hashPasswordInDatabase == hashPasswordToCheck;





if (__name__ == "__main__"):
    unit = UsersDatabase("mrPenis");
    # unit.addUser("RUR", None, "NNIIGIGIIG");
    print(unit.authenticate("NNIIGIGIIG"));

    # con = Connection("users.db");
    # cur = con.cursor();
    # cur.execute(""" SELECT * FROM users """);
    # print(cur.fetchall());

    # con = Connection("users.db");
    # cur = con.cursor();
    # cur.execute(""" CREATE TABLE users (username TEXT PRIMARY KEY, language VARCHAR(2) NOT NULL, chat_id INTEGER, email TEXT, password TEXT NOT NULL) """);
    # con.commit();
