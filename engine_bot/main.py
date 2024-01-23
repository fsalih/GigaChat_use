import telebot
import time

bot = telebot.TeleBot('bot_id')

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
