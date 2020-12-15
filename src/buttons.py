from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import id_osh, id_bishkek, id_talas

main_markup = ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add('Погода на сегодня')

city_choice = InlineKeyboardMarkup()
buttons = [
    InlineKeyboardButton("Ош", callback_data=id_osh),
    InlineKeyboardButton("Бишкек", callback_data=id_bishkek),
    InlineKeyboardButton("Талас", callback_data=id_talas)
    ]
city_choice.add(*buttons)

