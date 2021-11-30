import Constants as keys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Responses as R
import Alarm as Alarm
from time import sleep
import Check_site as Check
from datetime import datetime
from selenium import webdriver
import Variable as V


print("Bot started...")
start_time = datetime.strptime(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
)


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


def camping_site_alarm():
    repeat = 0
    detected = 0
    while True:
        driver = webdriver.Chrome(keys.DRIVER_PATH)
        driver.get(V.url)
        Check.wait(driver, 10)
        driver.maximize_window()
        driver.implicitly_wait(10)
        i = 0
        f = 0
        while f < 500:
            f += 1
            repeat += 1
            Check.wait(driver, 3)
            sleep(1)
            site_list = Check.create_site_list(driver)
            current_time = datetime.strptime(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "%Y-%m-%d %H:%M:%S",
            )
            time_interval = current_time - start_time
            Alarm.print_state(
                site_list[0],
                site_list[1],
                site_list[2],
                site_list[3],
                time_interval,
                repeat,
                detected,
            )

            if i == 0:
                pre_site = 0
                i += 1
            else:
                pass

            current_site = (
                site_list[0] + site_list[1] + site_list[2] + site_list[3]
            )

            if pre_site != current_site:
                detected += 1
                pre_site = current_site
                Alarm.telegram_send_link(
                    site_list[0], site_list[1], site_list[2], site_list[3]
                )
            else:
                pass

            Check.refresh_site(driver)

        Check.close_web(driver)
        sleep(3)


# main()

if __name__ == "__main__":
    camping_site_alarm()

# driver = webdriver.Chrome()
