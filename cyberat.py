from telegram.ext import Updater, MessageHandler, filters, ContextTypes, Application, CommandHandler
from telegram import Update, File
from hashlib import md5
from os import remove

#bot settings
TOKEN = "7056541263:AAFRZLU5TMNRicql-urv0EEPzSxkWMB42G0"
DOWNLOADS = "Files\\"

def hash_image(file_path):
    #calc the md5 of the image
    with open(file_path, "rb") as file:
        data = file.read()
        md5_hash = md5(data).hexdigest()
        return md5_hash

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #check the type of the file
    if update.message.document.mime_type in ['image/jpeg', 'image/jpg']:
        #download file
        fileName = update.message.document.file_name
        new_file = await update.message.effective_attachment.get_file()
        await new_file.download_to_drive(DOWNLOADS + fileName)

        #send the md5
        await update.message.reply_text("md5: " + hash_image(DOWNLOADS + fileName))

        #delete the user file
        remove(DOWNLOADS + fileName)
    else:
        await update.message.reply_text("Invalid file type, only jpeg / jpg.")

async def start_command(update, context):
    #send welcome message to the user
    await update.message.reply_text("Welcome to the CybeRat image convertor to hash!")

async def text_error(update, contex):
    #send the text error message
    await update.message.reply_text("Please send only images in types jpeg / jpg.")

def main():
    #starting the bot app
    print("starts bot...")
    app = Application.builder().token(TOKEN).build()

    #setting the handler functions
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, text_error))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    #statring the poll
    print("starts polling...")
    app.run_polling()

if __name__ == '__main__':
    main()
