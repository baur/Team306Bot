# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'команда start')

@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#    bot.send_message(message.chat.id, message.text)
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - АСУТП')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    elif text == "бауыржан":
        bot.send_message(chat_id, '87051110181')		
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')

	
	
if __name__ == '__main__':
     bot.polling(none_stop=True)