from telegram.ext import Updater, MessageHandler, filters, ContextTypes, Application, CommandHandler
from telegram import Update, File
from hashlib import md5

USERNAME = "@imcyberat_bot"
TOKEN = "7056541263:AAFRZLU5TMNRicql-urv0EEPzSxkWMB42G0"

def hash_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        md5_hash = md5(data).hexdigest()
        return md5_hash

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Download file
    fileName = update.message.document.file_name
    new_file = await update.message.effective_attachment.get_file()
    
    await new_file.download_to_drive(fileName)
    await update.message.reply_text("You send file!")

async def start_command(update, context):
    await update.message.reply_text("Welcome to the CybeRat image convertor to hash!")

def main():
    print("starts bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.Document.MimeType('image/jpeg'), handle_file))
    app.add_handler(MessageHandler(filters.Document.MimeType('image/jpg'), handle_file))
    print("starts polling...")
    app.run_polling()

if __name__ == '__main__':
    main()
