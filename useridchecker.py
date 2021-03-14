import telebot
bot = telebot.TeleBot('1675564937:AAGj79bwYZjyZ2vTQ9EZMHtwz21ES8A7F0Y')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    print(message.from_user.id)

bot.polling(none_stop=True)