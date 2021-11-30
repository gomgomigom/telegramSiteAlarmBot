import Variable as V
from selenium.webdriver.common.by import By


def close_web(driver):
    driver.close()


def wait(driver, second):
    driver.implicitly_wait(second)


def open_web(driver):
    driver.get(V.url)
    driver.maximize_window()
    driver.implicitly_wait(10)


def check_site_A(driver):
    site_list_A = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_a.cbtn_on"
    )
    return len(site_list_A)


def check_site_B(driver):
    site_list_B = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_b.cbtn_on"
    )
    return len(site_list_B)


def check_site_C(driver):
    site_list_C = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_c.cbtn_on"
    )
    return len(site_list_C)


def check_site_D(driver):
    site_list_D = driver.find_elements(
        By.CSS_SELECTOR, "#res_click_map > div .area_d.cbtn_on"
    )
    return len(site_list_D) - 1


def refresh_site(driver):
    driver.refresh()


def create_site_list(driver):
    site_list = []
    site_list.append(check_site_A(driver))
    site_list.append(check_site_B(driver))
    site_list.append(check_site_C(driver))
    site_list.append(check_site_D(driver))
    return site_list
