import telebot

bot = telebot.TeleBot('1208698339:AAEoBDvVlhttJGe0gde5HSUlDlJ7AFOP12w')


def Result(text_):
    result = 0
    if "+" in text_:
        text_ = text_.split("+")
        result = float(text_[0]) + float(text_[1])
    elif "*" in text_:
        text_ = text_.split("*")
        result = float(text_[0]) * float(text_[1])
    elif "/" in text_:
        text_ = text_.split("/")
        if float(text_[1]) == 0:
            result = "Ошибка: деление на 0"
        else:
            result = float(text_[0]) / float(text_[1])
    elif "-" in text_:
        text_ = text_.split("-")
        a = 0
        b = 0
        if text_[0] == "":
            a = - float(text_[1])
        else:
            a = float(text_[0])
        if text_[-2] == "":
            b = - float(text_[-1])
        else:
            b = float(text_[-1])
        result = a - b
    return result


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Начинаю вычисления')


@bot.message_handler(content_types=['text'])
def send_text(message):
    text_ = message.text

    bot.send_message(message.chat.id, str(Result(text_)))


bot.polling()
