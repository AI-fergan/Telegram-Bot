import tkinter
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "7056541263:AAFRZLU5TMNRicql-urv0EEPzSxkWMB42G0"
USERNAME = "@imcyberat_bot"

INVALID_INPUT = "This bot accepts only jpg / jpeg files."

def image_to_hash(image):
    pass

def message_handler(update: Update, context: ContextTypes):
    if update.message.photo:
        photo = update.message.photo[-1].get_file()
        
        manipulated_image = manipulate_image("temp.jpg")
        update.message.reply_photo(photo=manipulated_image)
    else 


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    handler = MessageHandler(Filters.photo, message_handler)
    dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()