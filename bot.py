import requests
import telebot
import os
import string
from time import sleep
from telebot import types
import random
token = os.environ.get("BOT_TOKEN")
#trakos
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	
	bot.reply_to(message,f'**Hi ,Send /ss To Start Checker ˜ƒ\nBy @ttrakos | @trprogram**')
@bot.message_handler(commands=['ss'])
def send_tool(message):
    key = types.ReplyKeyboardMarkup(row_width=5)
    itembtn2 = types.KeyboardButton('- Start checker')
    
    key.add(itembtn2)
    send = bot.send_message(message.chat.id , "**Bot Working !!**" , reply_markup = key)

@bot.message_handler(func=lambda m: True)
def trakos(message):
    if message.text == "- Start checker":
    	while 1:
    		d = ('1234567890')
    		f = random.choice(d)
    		g = random.choice(d)
    		haa = random.choice(d)
    		has = random.choice(d)
    		ss = (f'48{f}{g}{haa}{has}')
    		url = f'https://bin-checker.net/api/{ss}'
    		s = requests.get(url).json()
    		hs = s['scheme']
    		hf = s['country']['code']
    		hr = s['country']['name']
    		bank = s['bank']['name']
    	
    		sleep(10)
    if 'BR' in hf:
    		bot.send_message(message.chat.id,f'New Bin âœ…\nBin : {ss}\nCountry : {hr}\nCountry Code : {hf}\nLevel : Bussines\nBank : {bank}\nBy : @trprogram')
    		sleep(8)
    		bot.send_message(message.chat.id,'My Channel : @trprogram')
    		q =1
    		
bot.polling(True)
