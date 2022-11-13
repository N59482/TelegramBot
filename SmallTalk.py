def smalltalk(text):
    if (text == "Привет" or text == "привет" or text == "Привет!" or text == "привет!"):
        return ("🐟👋")
    elif (text == "как дела?" or text == "Как дела?" or text== "как дела" or text == "Как дела"):
        return ("🐟🤙")
    elif (text == "что делаешь?" or text == "Что делаешь?" or text== "что делаешь" or text == "Что делаешь"):
        return ("🌊")
    else :
        return("🐟") 
    #     def get_user_text(message):
    # elif message.text == "user info":
    #     bot.send_message(message.chat.id, message)
    # elif (message.text == "Привет" or message.text == "привет" or message.text == "Привет!" or message.text == "привет!"):
    #     bot.send_message(message.chat.id, "🐟👋")
    # elif (message.text == "как дела?" or message.text == "Как дела?" or message.text== "как дела" or message.text == "Как дела"):
    #     bot.send_message(message.chat.id, "🐟🤙")
    # elif (message.text == "что делаешь?" or message.text == "Что делаешь?" or message.text== "что делаешь" or message.text == "Что делаешь"):
    #     bot.send_message(message.chat.id, "🌊")
    # else :
    #     bot.send_message(message.chat.id, "🐟") 