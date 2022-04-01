
url =   "http://selenium1py.pythonanywhere.com/catalogue/category/books_2/"

class BasePage():            # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
