import telebot
from telebot.types import InputFile
from datetime import datetime

Admin=
token=""
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
   wellcome="Привет это бот _ присылай _ "
   bot.send_message(message.chat.id,wellcome)
   bot.set_my_commands(
   commands=[
      telebot.types.BotCommand('start', 'старт!'),
      telebot.types.BotCommand('send_meme', 'скинуть _'),
      telebot.types.BotCommand('report', 'ошибки')
   ],
   scope=telebot.types.BotCommandScopeChat(message.chat.id)
   )

@bot.message_handler(commands=['send_meme'])
def send_meme(message):
   bot.send_message(message.chat.id, "жду _")
   @bot.message_handler(content_types=['photo'])
   def photo(message):
       bot.send_message(Admin, "sender_id: "+str(message.from_user.id)+" sender_name: "+str(message.from_user.username))
       print("message.photo = " + str( message.photo ) )
       fileID = message.photo[-1].file_id
       print("fileID = " + str( fileID))
       file_info = bot.get_file(fileID)
       print('file.file_path = '+ str(file_info.file_path))
       downloaded_file = bot.download_file(file_info.file_path)
       file_name = str(datetime.today().strftime('H%HM%MS%S')) + "_" + str(message.from_user.id) + "_" + str(file_info.file_path).replace("photos/","")
       print(file_name)
       with open(file_name, 'wb') as new_file:
          new_file.write(downloaded_file)
       bot.send_photo(Admin, InputFile('./' + file_name))
       bot.send_message(message.chat.id, " _ ")
 
@bot.message_handler(commands=['report'])
def report(message):
   bot.send_message(message.chat.id, "ваше сообщение с ! в начале доставят _")

@bot.message_handler(regexp='^!..')
def report_by_regexp(message):  
    print("report from " + "sender_id: "+str(message.from_user.id)+" sender_name: "+str(message.from_user.username))
    print("message: "+message.text)
    bot.send_message(Admin, str(message.from_user.username)+ ": " + message.text)
    bot.send_message(message.chat.id, "Отправлено!")

bot.infinity_polling()

#@bot.message_handler(commands=[''], content_types=['photo'])
#def photo_without_command(message):
#    bot.send_message(message.chat.id, "используй send_meme!")
#@bot.message_handler(commands=['img'])
#def img_message(message):
#   bot.send_photo(message.chat.id, InputFile('./test.jpg'))
