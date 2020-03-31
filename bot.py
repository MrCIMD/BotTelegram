from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pymysql

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text('Bienvenido a BotMysql, ¿En que te puedo ayudar? Para ver mis comandos usa: /help')

def help(bot, update):
    update.message.reply_text('estos son mis comandos:\n'\
                                'Tablas de Cargo: /cargo\n'\
                                'Tablas de Almacenes: /almacenes\n'\
                                'Tablas de Autores: /autores\n'\
                                'Tablas de Clientes: /clientes\n'\
                                'Tablas de Detalles Nota: /detalles\n')
def cargo(bot, update):
    conexion = pymysql.connect('localhost:3306','root','12345678','ut')
    cur = conexion.cursor()
    consulta = "SELECT * FROM cargo"
    cur.execute(consulta)
    for row in cur.fetchall():
        resultado = row [0], row[1]
        update.message.reply_text(resultado)
    print ("tu resultado de cargo")

def echo(bot, update):
    update.message.reply_text(update.message.text)

def error(bot, update, error):
    logger.warn('update "%s" caused error "%s"' % (update, error))

def main():
    print("Preparando el bot")
    updater = Updater("1148408397:AAEcxp4T0wzH55Le00lz0ecHdM5NKS1R_fc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()