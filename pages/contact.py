class contacts:
    def __init__(self,page):
        self.page = page
        self.contact = page.locator('(//a[text()="Contact us"])[1]')
        self.name = page.locator('(//input[@name="name"])[2]')
        self.email = page.locator('(//input[@type="email"])[2]')
        self.btn = page.locator('//button[@class="send-otp-btn"]')
        self.otp = page.locator('(//input[@name="otp"])[2]')
        self.company = page.locator('(//input[@name="company"])[2]')
        self.phone = page.locator('(//input[@name="phone"])[2]')
        self.service = page.locator('(//select[@name="service"])[2]')
        self.message = page.locator('(//textarea[@name="message"])[2]')

        # social media 
        self.fb = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/facebook.png"]')
        self.linkdin = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/linkedin.png"]')
        self.insta = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')  

    def fill_data_verify(self):
        self.contact.click()
        self.name.fill('salman')
        self.email.fill('nadaf.salman29@gmail.com')
        self.btn.click()
        self.page.wait_for_timeout(8000)
        self.page.on("dialog", lambda dialog: dialog.accept())        
        self.otp.fill('12345')
        self.company.fill('xyz')
        self.phone.fill('9904588788')
        self.service.select_option('Web Development')
