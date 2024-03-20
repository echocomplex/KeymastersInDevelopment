import telebot
from telebot import types
from TelegramBot.privacy import TOKEN
from Database.TelegramBotDatabase import TelegramBotDatabase
from TelegramBot.buttons import *
from TelegramBot.messages import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "language"])
def start(message):
    database = TelegramBotDatabase(message.chat.id)
    database.addUser()
    del database
    markup = types.InlineKeyboardMarkup()
    for text, callback in languages.items():
        btn = types.InlineKeyboardButton(text=text, callback_data=callback)
        markup.add(btn)
    bot.send_message(message.chat.id, text=start_message, parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=["info"])
def info(message):
    chat_id = message.chat.id
    database = TelegramBotDatabase(message.chat.id)
    database.addUser()
    language = database.getLanguage()
    del database
    bot.send_message(chat_id=chat_id, text=information[language], parse_mode="html")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    database = TelegramBotDatabase(call.message.chat.id)
    database.addUser()
    language = database.getLanguage()

    if call.data in languages.values():
        database.setLanguage(call.data)
        language = call.data
        markup = types.InlineKeyboardMarkup()
        toMenuBtn = types.InlineKeyboardButton(text=to_the_main_menu[language], callback_data="mainmenu")
        markup.add(toMenuBtn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=language_choose[language], parse_mode="html", reply_markup=markup)
    del database

    if call.data == "mainmenu":
        markup = types.InlineKeyboardMarkup()
        for text, callback in main_menu_buttons[language].items():
            btn = types.InlineKeyboardButton(text=text, callback_data=callback)
            markup.add(btn)
        messageToUser = "%s%s%s" % (main_menu[language][0], call.message.chat.first_name, main_menu[language][1])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=messageToUser, parse_mode="html", reply_markup=markup)

    elif call.data == "Passwords":
        markup = types.InlineKeyboardMarkup()
        for text, callback in passwords_buttons[language].items():
            btn = types.InlineKeyboardButton(text=text, callback_data=callback)
            markup.add(btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=passwords_ms[language], parse_mode="html", reply_markup=markup)

    elif call.data == "generation":
        markup = types.InlineKeyboardMarkup()
        for text, callback in generation_buttons[language].items():
            btn = types.InlineKeyboardButton(text=text, callback_data=callback)
            markup.add(btn)
        bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id,
                              text=passwords_ms[language], parse_mode="html", reply_markup=markup)

def startBot():
    print("Keymaster's Bot is started and ready to work.")
    bot.polling(none_stop=True, interval=0)