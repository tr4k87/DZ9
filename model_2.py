from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import emoji

async def enter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global id
    global name
    global phone
    global status
    msg = update.message.text
    items = msg.split()
    id = items[1]
    name = items[2]
    phone = items[3]
    status = items[4]
    await update.message.reply_text(emoji.emojize(f'{update.effective_user.first_name} Все получилось :thumbs_up:'))
    return id, name, phone, status


async def w_txt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('adrbk.txt', "a") as file:
        file.writelines(f'id:{id} ;Name:{name} ;Phone:{phone} ;Status {status}\n')
    await update.message.reply_text(emoji.emojize(f'{update.effective_user.first_name} Все получилось :thumbs_up:'))

async def w_csv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('adrbk.csv', "a") as file:
        file.writelines(f'id:{id} ;Name:{name} ;Phone:{phone} ;Status {status}\n')
    await update.message.reply_text(emoji.emojize(f'{update.effective_user.first_name} Все получилось :thumbs_up:'))

async def r_txt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = open('adrbk.txt', 'r')
    for line in data:
        await update.message.reply_text(line) 
    data.close()

async def r_csv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = open('adrbk.csv', 'r')
    for line in data:
        await update.message.reply_text(line) 
    data.close()


