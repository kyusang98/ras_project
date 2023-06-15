from telegram.ext import Application, CommandHandler, MessageHandler, filters
import asyncio
from stock_crawling import dictionary

bot_token = '6082136191:AAG35lMMeZnAxVUT9V-OrFn_aTILFvfGxys'

#크롤링한 내용 채팅
async def send_message(update, context):
    tdata1= str(dictionary)
    await context.bot.sendMessage(chat_id=update.message.chat.id,text=tdata1)

#하고 싶은 말 채팅
async def send_message2(update, context):
    tdata2= 'yeah yeah yeah'
    await context.bot.sendMessage(chat_id=update.message.chat.id,text=tdata2)

#이상한 말 할때 채팅
async def other_message(update, context):
    tdata3='/stock:등락률 출력, /yeah:yeah yeah yeah 출력'
    await context.bot.sendMessage(chat_id=update.message.chat.id,text=tdata3)


application = Application.builder().token(bot_token).build()
application.add_handler(CommandHandler('stock',
                                       send_message))
application.add_handler(CommandHandler('yeah',
                                       send_message2))

#telegram v13.7에서는 Filters.text였지만 telegram v20부터는 filters.TEXT가 되었다.
application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND),
                                       other_message))
application.run_polling()
