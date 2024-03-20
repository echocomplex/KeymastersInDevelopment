from Database.TelegramBotDatabase2 import TelegramBotDatabase

database = TelegramBotDatabase(1234567890);
database.addUser();
print(database.getLanguage());
print(database.getLoginStatus());
database.setLanguage("EN");
database.setLoginStatus(True);
print(database.getLanguage());
print(database.getLoginStatus());
del database;
