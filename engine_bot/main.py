import telebot
import time

bot = telebot.TeleBot('6963248781:AAHN_K4yVMJ2kgcx-1G4MI-u-GazgeTQzNI')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую тебя!')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, 'Запрос обрабатывается...')
    time.sleep(5)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Сделано!')

bot.polling()