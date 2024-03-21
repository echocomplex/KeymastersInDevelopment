from Database.DatabaseClassesPython.TelegramBotDatabase import TelegramBotDatabase
from Database.DatabaseClassesPython.PasswordsDatabase import PasswordsDatabase
from Database.DatabaseClassesPython.Necessary import startDatabase, shutdownDatabase


startDatabase();

# database = TelegramBotDatabase(1234567890);
# database.addUser();
# print(database.getLanguage());
# print(database.getLoginStatus());
# database.setLanguage("EN");
# database.setLoginStatus(True);
# print(database.getLanguage());
# print(database.getLoginStatus());
# del database;
#
# database = TelegramBotDatabase(1234567890);
# database.addUser();
# print(database.getLanguage());
# print(database.getLoginStatus());
# database.setLanguage("EN");
# database.setLoginStatus(True);
# print(database.getLanguage());
# print(database.getLoginStatus());
# del database;

database = PasswordsDatabase("kekpop");
database.addUser();
database.addPassword("pipi", "kaka");
database.addPassword("pipi", "kaka");
database.addPassword("pipi", "kaka");
database.addPassword("pipi", "kaka");
print(database.getAll());
database.deletePassword("pipi")
del database;

shutdownDatabase();