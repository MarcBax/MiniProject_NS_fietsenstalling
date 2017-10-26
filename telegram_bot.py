import requests
from telegram.ext import Updater, CommandHandler

telegram_api = "458958945:AAENUyVr_1PGmhmL_T4mV356-UzIihx4yrg"


updater = Updater(token="458958945:AAENUyVr_1PGmhmL_T4mV356-UzIihx4yrg")
dispatcher=updater.dispatcher

def start(bot, update):
    update.message.reply_text(
        'Hello, your tracking ID is : {} \n\nFor more information about Telegram notifications type'
        ' \"/eng_info\"\nVoor meer informatie over Telegram notificaties type \"/info\".'
        '\nOm uw telegram ID nog een keer weer te geven type \"/id\".'.format(update.message.from_user.id))

def info(bot, update):
    update.message.reply_text(
        "Deze bot zal uw automatisch een bericht versturen wanneer u uw fiets ophaalt."
        " U zou dan wel een tracking ID moeten invoeren.\nAls u niet gebruik wilt maken van deze functie type dan niets voor uw tracking ID")

def eng_info(bot, update):
    update.message.reply_text(
        "This bot will send you messages when you collect your bike, you will have to provide the tracking number."
        "\nIf you don't want this function activated simply put nothing for your tracking number.")

def id(bot, update):
    update.message.reply_text(
        'Your tracking ID is : {}'.format(update.message.from_user.id))

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('eng_info', eng_info))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('id', id))

updater.start_polling()
updater.idle()



