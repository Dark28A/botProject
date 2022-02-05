import telebot
import sqlite3

bot = telebot.TeleBot('5209932574:AAFJpNe9bt1fhMma-jwGNP5YSoGJqWjcrh8')


@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id()""")


@bot.message_handler(commands=['delete'])
def delete(message):
    pass