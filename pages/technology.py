class technologies:
    def __init__(self,page):
    
        self.page = page
        self.tech = page.locator('(//a[text()="Technologies"])[1]')

        
        self.CD = page.locator('//strong[text()="eCommerce Development"]')
        self.link1 = page.locator('//a[text()="Magento Development"]')
        self.link2 = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.link3 = page.locator('(//a[text()="Big Commerce"])[1]')
        self.link4 = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.link5 = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.link6 = page.locator('(//a[text()="Laravel Development"])[1]')
        self.link7 = page.locator('(//a[text()="Drupal Development"])[1]') 
        self.link8 = page.locator('(//a[text()="Joomla Development"])[1]')
        self.link9 = page.locator('(//a[text()="Express JS Development"])[1]')
        self.link10 = page.locator('(//a[text()="Opencart Development"])[1]')                           
        self.link11 = page.locator('(//a[text()="WordPress Development"])[1]')    
        self.link12 = page.locator('(//a[text()="Shopify Development"])[1]')    
        self.link13 = page.locator('(//a[text()="Node JS Development"])[1]')    
        self.link13 = page.locator('(//a[text()="Woo Commerce"])[1]')    
        self.link14 = page.locator('(//a[text()="Prestashop Development"])[1]')
        self.CD_list = [self.link1,self.link2,self.link3,self.link4,self.link5,self.link6,self.link7,self.link8,
                   self.link9,self.link10,self.link11,self.link12,self.link13,self.link14]

        # Mobile App Development
        self.MD = page.locator('//strong[text()="Mobile App Development"]')    
        self.link1 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.link2 = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.link3 = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.link4 = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.link5 = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.link6 = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')  
        self.link7 = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.link8 = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.link9 = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.MD_list = [self.link1,self.link2,self.link3,self.link4,self.link5,self.link6,self.link7,self.link8
                        ,self.link9]

    def verify_and_check_commerce(self):
        for i in self.CD_list:
            self.tech.hover()
            self.CD.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def verify_and_check_mobile(self):
        for i in self.MD_list:
            self.tech.hover()
            self.MD.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()       
            
    