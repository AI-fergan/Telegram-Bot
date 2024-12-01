from telegram.ext import ContextTypes, Application, CommandHandler

import config
import excel_update

# Help message
commands_help = """
/help - print commands usage & examples

/add - add new profit for exists shop.
usage: /add <shop name> <profit>
example: /add bakery_12 984

/new - create new shop name and insert its todays profit.
usage: /new <shop name> <profit>
example: /new bakery_23 753

/get - send the bot .xslx data file.
usage: /get
"""

async def start_command(update, context: ContextTypes.DEFAULT_TYPE):
    # Send welcome message to user
    await update.message.reply_text(("%s says: Welcome to the Excel managment bot!\nNote: use /help for commands usage") % config.BOT_NAME)

async def help(update, context: ContextTypes.DEFAULT_TYPE):
    # Send help message to user
    await update.message.reply_text(commands_help)

async def new_command(update, context: ContextTypes.DEFAULT_TYPE):
    # This command create new shop by shop name and set its daily profit
    command = ["new"]

    # New command args
    command += context.args

    # Run new command using excel helper
    try:
        excel_update.run(command)
        await update.message.reply_text("profit added to the new shop. anything else?")
    except:
        #send error message
        await update.message.reply_text(("%s ERROR: Missing shop profit or shop name.") % config.BOT_NAME)

async def add_command(update, context: ContextTypes.DEFAULT_TYPE):
    # This command add profit to exists shop
    command = ["add"]

    # Add command args
    command += context.args
    try:
        excel_update.run(command)
        await update.message.reply_text("profit added. anything else?")
    except:
        #send error message
        await update.message.reply_text(("%s ERROR: Shop name not found or missing shop profit.") % config.BOT_NAME)

async def send_data(update, context: ContextTypes.DEFAULT_TYPE):
    # This function send the bot server `data.xslx` file from the server to the user

    # Get user chat id
    chat_id = update.message.chat_id

    try:
        # Send the file
        await context.bot.send_document(chat_id=chat_id, document=open(config.EXCEL_FILE, 'rb'))
        await update.message.reply_text("File sent successfully!")
    except Exception as e:
        #send error message
        await update.message.reply_text("File is empty, please insert data with `/new` command")

def main():
    # Starting the bot app
    print("[*] starts bot...")
    app = Application.builder().token(config.TOKEN).build()

    # Setting the handler functions
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('new', new_command))
    app.add_handler(CommandHandler('add', add_command))
    app.add_handler(CommandHandler('get', send_data))

    # Start polling the bot
    print("[*] starts polling...")
    app.run_polling()

if __name__ == '__main__':
    main()
