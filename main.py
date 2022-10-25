from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from model_2 import *


app = ApplicationBuilder().token("5783069909:AAHJNWvWSA8mnZw-QvK4SCxZQdqWI1NwSD0").build()

app.add_handler(CommandHandler("enter", enter))
app.add_handler(CommandHandler("w_txt", w_txt))
app.add_handler(CommandHandler("w_csv", w_csv))
app.add_handler(CommandHandler("r_txt", r_txt))
app.add_handler(CommandHandler("r_csv", r_csv))

app.run_polling()