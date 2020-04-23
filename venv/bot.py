import telebot

bot = telebot.TeleBot("1087840610:AAEvS6L0gZyceHy4YZBcfPFiDoAJ-2aWMH4");


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "anime");


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'шо хоч':
        bot.send_message(message.chat.id, 'нiчо')
    elif message.text == 'пака':
        bot.send_message(message.chat.id, 'оцтань')
    elif message.text == "привет":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIBF16h8OOMMHNxN4s6i-MlK1BYYf66AAIQAQACtvArFHZJx3GhcdFYGAQ")
    elif message.text == "френдзона":
        bot.send_message(message.chat.id,
                         "ти очень крутая я просто не хочу обманювать ні себе ні тебе бо чуства пропали но ти в цьом не винна я дурак щастя тобі")
    else:
        bot.send_message(message.chat.id,"не пон...")

bot.polling();
