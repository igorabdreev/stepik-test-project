from selenium.webdriver.common.by import By
# py -m pytest -v --tb=line --language=en test_main_page.py

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser): # путест вызывает только эту функцию, т.к. она
   browser.get(link)                          # она начинается на TEST...
   go_to_login_page(browser)

