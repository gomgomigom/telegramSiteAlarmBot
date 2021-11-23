import Variable as V
from selenium.webdriver.common.by import By


driver = V.driver


def wait(second):
    driver.implicitly_wait(second)


def open_web():
    driver.get(V.url)
    driver.maximize_window()
    driver.implicitly_wait(10)


def check_site_A():
    site_list_A = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_a.cbtn_on"
    )
    return len(site_list_A)


def check_site_B():
    site_list_B = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_b.cbtn_on"
    )
    return len(site_list_B)


def check_site_C():
    site_list_C = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_c.cbtn_on"
    )
    return len(site_list_C)


def check_site_D():
    site_list_D = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_d.cbtn_on"
    )
    return len(site_list_D) - 1


def remain_site(a, b, c, d):
    return a + b + c + d


def refresh_site():
    driver.refresh()


def create_list():
    site_list = []
    site_list.append(check_site_A())
    site_list.append(check_site_B())
    site_list.append(check_site_C())
    site_list.append(check_site_D())
    return site_list
