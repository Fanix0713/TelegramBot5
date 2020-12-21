import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, dotetime, pymysql

API_TOKEN = "1377889366:AAGGKKdLl3GbKJgkAHiJ3T9Vl2x7-oSBY4Q"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def statistics(user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimeter=';')
        wr.writerow([data, user_id, command])

    
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Привет!")
    statistics(message.chat.id, message.text)
    stat(message.chat.id, message.text)

def stat(user id, comand):
    connection = pymysql.connect('194.58.103.48', 'bot', 'bot2020', 'bot')
    cursor = connection.cursor()
    data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES ('%s', '$s', '%s')" % (user_id, command, data))
    connection.comit()
    cursor.close()
    
