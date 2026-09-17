class portfolios:
    def __init__(self,page):
        self.page = page
        self.porturl = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        self.ics = page.locator('//a[@href="https://www.icshomework.in/"]')
        