"""

Database for Keymaster's Telegram Bot
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

"""



""" IMPORTS """
# from sqlite3 import Connection
from os import getcwd
from jnius import autoclass
JavaClass = autoclass("TelegramBotDatabase");
instance = JavaClass(78589458);
print(instance.addUser())

# class TelegramBotDatabase:
#     def __init__ (self, chatID: int) -> None:
#         self.__connection = Connection("Database/TelegramBotUsers.db");
#         self.__cursor = self.__connection.cursor();
#         self.__chatID: int = chatID;
#
#     def __del__ (self) -> None:
#         self.__connection.close();
#
#     def addUser (self) -> None:
#         self.__cursor.execute(
#             """
#             INSERT OR IGNORE INTO users (chat_id, language, login_status)
#             VALUES (?, ?, ?)
#             """,
#             (self.__chatID, "RU", False));
#         self.__connection.commit();
#
#     def setLanguage (self, language: str) -> None:
#         self.__cursor.execute(
#             """
#             UPDATE users
#             SET language = ?
#             WHERE chat_id = ?
#             """, (language, self.__chatID));
#         self.__connection.commit();
#
#     def getLanguage (self) -> str:
#         self.__cursor.execute(
#             """
#             SELECT language
#             FROM users
#             WHERE chat_id = ?
#             """, (self.__chatID,));
#         language: str = self.__cursor.fetchone()[0];
#         return language;
#
#     def getLoginStatus (self) -> bool:
#         self.__cursor.execute(
#             """
#             SELECT login_status
#             FROM users
#             WHERE chat_id = ?
#             """, (self.__chatID,));
#         loginStatus: str = self.__cursor.fetchone()[0];
#         return bool(loginStatus);
#
#     def setLoginStatus (self, status: bool) -> None:
#         self.__cursor.execute(
#             """
#             UPDATE users
#             SET login_status = ?
#             WHERE chat_id = ?
#             """, (status, self.__chatID));
#         self.__connection.commit();
#
#
# if (__name__ == "__main__"):
#     # unit = TelegramBotDatabase(7892457894);
#     # unit.addUser();
#
#     con = Connection("TelegramBotUsers.db");
#     cur = con.cursor();
#     cur.execute(""" SELECT * FROM users """);
#     print(cur.fetchall());
#
#     # con = Connection("TelegramBotUsers.db");
#     # cur = con.cursor();
#     # cur.execute(""" CREATE TABLE users (chat_id INTEGER PRIMARY KEY, language VARCHAR(2) NOT NULL, login_status BOOLEAN NOT NULL) """);
#     # con.commit();
