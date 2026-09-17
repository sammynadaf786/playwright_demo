class verticals:
    def __init__(self,page):
        self.page = page

        self.vertical = page.locator('(//a[text()="Verticals"])[1]')

        #trading validation
        self.trading = page.locator('(//strong[text()="Trading"])')

        # trading option
        self.st = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.pt = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.ct = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.ta = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.at = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.cst = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.wt = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        #trading list
        self.trading_list=[self.st,self.pt,self.ct,self.ta,self.at,self.cst,self.wt]

        # Retail and Ecommerce
        self.RT = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.link1 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.link2 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        #retail_list
        self.retail_list = [self.link1,self.link2]
     
        # Healthcare
        self.HC = page.locator('//strong[text()="Healthcare"]')
        self.link1 = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.link2 = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        # healthcare list 
        self.healthcare_list = [self.link1,self.link2]   
           
        # Fintech
        self.FT = page.locator('//strong[text()="Fintech"]')
        self.link1 = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.link2 = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        # fintect list
        self.fintect_list = [self.link1,self.link2]
    
        # Custom App
        self.CA = page.locator('//strong[text()="Custom App"]')   
        self.link1 = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.link2 = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]') 
        self.link3 = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.link4 = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.link5 = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.link6 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.link7 = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.link8 = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.link9 = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')

        # custom_app list
        self.custom_list = [self.link1,self.link2,self.link3,self.link4,self.link5,self.link6,self.link7,self.link8,self.link9]
    def click_verify_trading(self):
        for i in self.trading_list:
            self.vertical.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def click_verify_retail(self):
        for i in self.retail_list:
            self.vertical.hover()
            self.RT.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def click_verify_healthcare(self):
        for i in self.healthcare_list:
            self.vertical.hover()  
            self.HC.hover()
            i.click()            
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def click_verify_fintech(self):
        for i in self.fintect_list:
            self.vertical.hover()
            self.FT.hover()
            i.click()    
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def click_verify_custom_app(self):
        for i in self.custom_list:
            self.vertical.hover() 
            self.CA.hover()
            i.click()    
            self.page.wait_for_load_state('load')
            self.page.go_back()
                               

