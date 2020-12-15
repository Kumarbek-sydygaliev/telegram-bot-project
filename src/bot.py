import os

import telebot
import requests
from flask import Flask, request
from telebot.types import InlineKeyboardButton

import config
from req import get_weather
from messages import hello_message, weather_message
from buttons import main_markup, city_choice


server = Flask(__name__)
bot = telebot.TeleBot(config.token)

@server.route("/", methods=['POST'])
def recieve_update():
    bot.process_new_updates(
        [telebot.types.Update.de_json(
            request.stream.read().decode("utf-8"))])
    return {"ok": True}



@bot.message_handler(commands=['start', 'help', 'restart'])
def answer_start(message):
    bot.send_message(message.chat.id, hello_message(message.from_user.first_name), reply_markup=main_markup)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Погода на сегодня':
        bot.send_message(message.chat.id, 'Выберите один из городов', reply_markup=city_choice)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, weather_message(get_weather(call.data)))
    except Exception as e:
        print(repr(e))



@server.route('/' + config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    s = bot.set_webhook(url='https://03cf5b5587ef.ngrok.io' + config.token)
    if s:
        return print("webhook setup ok")
    else:
        return print("webhook setup failed")


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
