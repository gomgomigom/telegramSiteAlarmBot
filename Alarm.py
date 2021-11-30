from datetime import datetime
import telegram
import Constants as C
import Variable as V


bot = telegram.Bot(C.API_KEY)
chat_id = V.CHAT_ID


def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def print_state(a, b, c, d, time_interval, repeat, detected):
    print("------------------------------")
    print(
        f"현재시간 = {current_time()},  경과시간: {time_interval},  반복횟수: {repeat},  발견: {detected}"
    )
    print(f"남은 자리  A site: {a},  B site: {b},  C site: {c},  D site: {d}")


def telegram_send_link(a, b, c, d):
    bot.sendMessage(
        chat_id,
        text=f"✨{V.year}년 {V.month}월 {V.day}일 {V.stayDay}박{V.stayDay+1}일✨\n대저캠핑장 남은 자리\nA site: {a},  ✨B site: {b}✨,\nC site: {c},  D site: {d},\n\n{V.url}",
    )
