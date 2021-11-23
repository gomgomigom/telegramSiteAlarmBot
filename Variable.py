from selenium import webdriver

driver = webdriver.Chrome("C:/Users/gomigom/Desktop/shortcut/chromedriver.exe")

year = 2021  # 몇 년
month = 12  # 몇 월
day = 18  # 몇 일
stayDay = 1  # 몇 박 1~2
url = f"https://www.daejeocamping.com/reservation/real_time?user_id=&site_id=&site_type=&dis_rate=0&user_dis_rate=&resdate={year}-{month}-{day}&schGugun={stayDay}&price=0&bagprice=2000&allprice=0"
