import logging
import serial
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


com = ""
Arduino_Serial = serial.Serial(com,9600)  


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Select /state for Temperature and Humidity')


def state(update: Update, context: CallbackContext) -> None:
    Arduino_Serial.write(str.encode('1'))
    read=Arduino_Serial.readline()
    str_rn = read.decode()
    a = str_rn.rstrip()
    result = a.split()
    clk = result[0]
    temp = result[1]
    humd = result[2]
    update.message.reply_text("Temperature is : " + temp)
    update.message.reply_text("Humidity is : " + humd)
    update.message.reply_text("clk is : " + clk)
    

def no(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Select /state for Temperature and Humidity')


def main():

    updater = Updater("Token", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("state", state))

    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, no))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
