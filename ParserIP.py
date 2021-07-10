import telebot
import os
import ipaddress
from urllib.request import urlopen
from json import load
from time import sleep
bot = telebot.TeleBot('1653997244:AAG4NS6YZY8LYiqFzXdziihPPU4LPaY5Yd4');
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши нужный IP')

@bot.message_handler(content_types=['text'])
def send_text(message):
	ip = message.text
	if check_ip(ip) == True:
		url2 = 'http://check.getipintel.net/check.php?ip=' + ip + '&contact=jugerror@gmail.com&format=json'
		url = 'https://ipqualityscore.com/api/json/ip/JrSxH8klStuqb92GEp3k3RWdDrznnidi/' + ip + '?strictness=0&allow_public_access_points=true&fast=true&lighter_penalties=true&mobile=true'
		try:
			res = urlopen(url)
			data = load(res)
			res1 = urlopen(url2)
			data1 = load(res1)
			str2 = '------------------------------------------\n'
			str2 = str2 + 'ipqualityscore:' + '\n' * 2
			for i in data.keys():
				str1 = i  + ' : '  +  str(data[i])
				str1 = str1 + '\n' * 2
				str2 = str2 + str1
			str1 = ''
			str2 = str2 + 'getipintel:' + '\n' *2

			for i in data1.keys():
				if(i == 'result'):
					str2 = str2 + 'Fraud Score' + ' : ' + str(data1[i]) + '\n' 
				else:
					continue
			str2 =str2 + '------------------------------------------'
			bot.send_message(message.chat.id,'Connecting...')
			sleep(1)
			bot.send_message(message.chat.id,'Successfully')
			sleep(1)
			bot.send_message(message.chat.id,str2)
		except:
			bot.send_message(message.chat.id,'Что - то определенно не то с вашим IP')	   	
	else:
		bot.send_message(message.chat.id,'Неверный IP address')
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True
bot.polling()