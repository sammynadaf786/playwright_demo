class about:

    def __init__(self,page):
        self.page = page
        self.about = page.locator('(//a[text()="About us"])[1]')

    def click_about_us(self):
        self.about.click()
        self.page.wait_for_load_state('load')
        self.page.go_back()     
