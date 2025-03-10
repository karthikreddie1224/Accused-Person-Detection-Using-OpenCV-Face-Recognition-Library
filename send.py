import telepot

def sendpicture(message,image):
    bot = telepot.Bot('8106359425:AAF69mPYvb1Dnv6XtMUVHBoiSssZYvf6D34')
    bot.sendPhoto(1141677520, photo=open(image, 'rb'))
    bot.sendMessage(1141677520, message)