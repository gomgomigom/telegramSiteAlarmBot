import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started...")


def start_command(update, context):
    update.message.reply_text("대저 캠핑장 잔여 사이트 확인을 시작합니다..")


def help_command(update, context):
    update.message.reply_text("지정된 날짜와 숙박기간의 잔여 사이트를 알려줍니다..")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
