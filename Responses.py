from datetime import datetime


def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in (
        "안녕",
        "반가워",
        "안녕?",
        "안녕하세요",
        "ㅎㅇ",
    ):
        return "안녕하세요, 반갑습니다. 저는 대저 캠핑장 알리미에요~ o((>ω< ))o"

    if user_message in ("누구", "뭐야"):
        return "난 대저캠핑장 알리미야"

    if user_message in ("time", "시간"):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d, %H:%M:%S")

        return str(date_time)

    return "I don't understand you"
