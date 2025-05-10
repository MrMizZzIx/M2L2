import telebot
import os
import random
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7935342009:AAFQL-hK9l9YGK3JbVCjPYiKGZRcjEN4BEA")
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['ecology'])
def send_ecology(message):
    bot.reply_to(message, f'Я тебе сейчас расскажу какие этапы нужны для экологии в быту!')
    bot.reply_to(message, '''Как можно улучшить экологичность в быту:
                Сортировать мусор.
                Перерабатывать пластик.
                Использовать вещи повторно.
                Экономия воды и электричества.
                Всегда убирать за собой.
                Учавствовать в экологических движениях.''')
@bot.message_handler(commands=['time'])
def send_ecology(message):
    bot.reply_to(message, f'Какое время ты уже используешь экологию в быту?')
    bot.reply_to(message, f'Советую начать уже сейчать а если ты уже используешь экологию в быту то отлично! Продолжай дальше!')
bot.polling()
