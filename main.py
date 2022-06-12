import telebot


bot = telebot.Telebot('')     # for token


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Здравствуйте, чем могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я не понимаю о чем ты. Напиши /help.')


bot.polling(none_stop=True, interval=0)
