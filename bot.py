from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pymysql

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text('Bienvenido a BotMysql, ¿En que te puedo ayudar? Para ver mis comandos usa: /help')

def help(bot, update):
    update.message.reply_text('Estos son mis comandos:\n'\
                                'Tablas de Comisiones: /comisiones\n')

def comisiones(bot, update):
    update.message.reply_text("Preparando la consulta")
    conexion = pymysql.connect('mysql.apexhosting.gdn','apexMC267066','8a18b699e0','apexMC267066')
    cur = conexion.cursor()
    consulta = "SELECT * FROM Comisiones"
    cur.execute(consulta)
    update.message.reply_text('[Servicio, Costo, Comision]')
    for row in cur.fetchall():
        resultado = str(row [0]), str(row[1]), str(row[2])
        update.message.reply_text(resultado)
    print ("Tu resultado de Comisiones")

def echo(bot, update):
    update.message.reply_text(update.message.text)

def error(bot, update, error):
    logger.warn('update "%s" caused error "%s"' % (update, error))

def main():
    updater = Updater("1148408397:AAEcxp4T0wzH55Le00lz0ecHdM5NKS1R_fc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("comisiones", comisiones))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()