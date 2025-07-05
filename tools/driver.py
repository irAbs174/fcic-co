'''
Web Driver functions based on Chrome by default
by: Unique174
github: https://github.com/irAbs174/post_tracker
________________________________________________________
Scripts objects include classes & functions docs:
1. class DriverFunctions {
    =>  0. '__init__': Initializes the WebDriver based on the production status 
                ('dev' for GUI mode, or headless mode for production).
                Sets up the WebDriver, assigns the tracking code, and loads 
                the specified portal page.
    =>  1. 'screenshot': Captures a screenshot of the current page, which can be 
                stored and saved for verification.
    =>  2. 'submit_tracking_form': Submits the tracking form by locating input 
                elements and sending the tracking code.
    =>  3. 'quit': Closes the WebDriver session gracefully, handling any errors 
                if they occur.
    =>  4. 'run': Executes the complete task flow by submitting the tracking 
                form, taking a screenshot, and closing the session. Returns a 
                dictionary with task success status and captured image.
    }
________________________________________________________
Please visit Computer Science NFT Collection:
NFT Market: https://getgems.io/unique-nft

BE HAPPY         :)
'''


from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from colorama import Fore
from pathlib import Path
from time import sleep
from core.SEC import (
    tracking_url as portal,
    production_status
)

class Driver:
    def __init__(self, tracking_code):
        # inital driver with given address and tracking_code
        print(
            Fore.WHITE,
            f"\n-> ++>> {portal} for tacking {tracking_code} \n"
        )
        
        try:
            # Look att production_status variable to define web driver '''
            if production_status == 'dev':
                ''' GUI (such as local host) driver '''
                self.driver = Chrome()
                
            else:
                ''' With CLI (such as production server) : '''
                from webdriver_manager.chrome import ChromeDriverManager
                from selenium.webdriver.chrome.service import Service
                from selenium.webdriver.chrome.options import Options
                options = Options()
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument("--window-size=1100,850")
                self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
                 
            # Set required variable tracking_code in self
            self.tracking_code = tracking_code
            
            # Load self.address from driver
            self.driver.get(portal)
            
            print(
                Fore.GREEN,
                f"\n ++>> Site {portal} initial successfuly! \n"
            )
        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
            )
        
    def screenshot(self):
        output = None
        # save page screen shot and store with tracking_code name
        try:
            output = self.driver.get_screenshot_as_png()
            
        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
            )
            
        return output

    def submit_tracking_form(self):
        # post index page elements for tracking sended package
        input = self.driver.find_element(By.ID, "txtbSearch")
        btn = self.driver.find_element(By.ID, "btnSearch")
        # send keys to post index page html input and click button element
        input.send_keys(self.tracking_code)
        btn.click()
          
    def quit(self):
        try:
            self.driver.close()
            print(
                Fore.MAGENTA,
                "\n -----------Chrome WebDriver Closed successfuly-----------\n"
            )
             
        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
                )
        
    def run(self):
        output = {
            'success': False
        }
        try:
            print(
                Fore.BLUE,
                f"\n => => Full Detail for {portal} with code {self.tracking_code}\n"
            )
            #Set input data to tracking form and submit
            self.submit_tracking_form()
            output['img'] = self.screenshot()
            output['success'] = True
            print(
                Fore.GREEN,
                f"=> Note: Seccessfuly generate image and return for retore! <="
            )

        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
                )
                 
        self.quit()
        return output
        
        