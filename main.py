#import telebot
#import sqlite3

#bot = telebot.TeleBot('5209932574:AAFJpNe9bt1fhMma-jwGNP5YSoGJqWjcrh8')

import qrcode
data = "Салоп Максим/7а/05.02.22/2334"
filename = "qrcode14"
img = qrcode.make(data)
img.save(filename)

