'''
Web Driver tests
by: Unique174
github: https://github.com/irAbs174/post_tracker
________________________________________________________
Scripts objects include classes & functions docs:
1. class Driver
    - Initializes the WebDriver, loads the target tracking URL, and includes essential Selenium functionality for tracking page navigation and interactions.

2. class Test (inherits from Driver)
    => The main test class, designed for initializing with a tracking code and executing various automated tests on the tracking site.

    Functions in Test:
      - __init__() : Initializes the Test instance with a tracking code (default code if empty input) and runs the test.
      - validate_tracking_code() : Checks if the tracking code is an 8-digit number to ensure valid input.
      - check_element_presence(by, value) : Verifies the presence of an element on the page by its locator type and value.
      - clear_cookies() : Clears all cookies stored by the WebDriver session.
      - refresh_page() : Refreshes the current page.
      - run_test_flow() : Executes a full test flow, including validation, form submission, screenshot capture, cookie clearance, and page refresh.
      - exit() : Closes the WebDriver session and exits the test safely.

Usage:
    To run the test, instantiate Test():
    > test_instance = Test()

________________________________________________________
Additional Resources:
- Visit Computer Science NFT Collection:
  NFT Market: https://getgems.io/unique-nft

BE HAPPY         :)
'''

from tools.driver import Driver
from selenium.common.exceptions import NoSuchElementException

class Test(Driver):
    def __init__(self):
        tracking_code = input("\nEnter Tracking code\nDefault (empty == '12345670') \n > ")
        tracking_code = "12345670" if tracking_code == '' else tracking_code
        super().__init__(tracking_code)
        self.run()
    
    def validate_tracking_code(self):
        """Validate tracking code format if needed."""
        if not self.tracking_code.isdigit() or len(self.tracking_code) != 8:
            print("Invalid tracking code. Must be an 8-digit number.")
            return False
        return True

    def check_element_presence(self, by, value):
        """Check if an element is present on the page."""
        try:
            self.driver.find_element(by, value)
            print(f"Element located: ({by}, {value})")
            return True
        except NoSuchElementException:
            print(f"Element not found: ({by}, {value})")
            return False

    def clear_cookies(self):
        """Clear all cookies in the browser."""
        try:
            self.driver.delete_all_cookies()
            print("Cookies cleared successfully.")
        except Exception as error:
            print(f"Error clearing cookies: {error}")

    def refresh_page(self):
        """Refresh the current page."""
        try:
            self.driver.refresh()
            print("Page refreshed successfully.")
        except Exception as error:
            print(f"Error refreshing page: {error}")

    def run_test_flow(self):
        """Run a full test flow including validation, submission, and screenshot."""
        if not self.validate_tracking_code():
            print("Test aborted due to invalid tracking code.")
            return
        
        # Check for presence of input field and submit button
        if self.check_element_presence(By.ID, "txtbSearch") and self.check_element_presence(By.ID, "btnSearch"):
            self.submit_tracking_form()
            screenshot_data = self.screenshot()
            if screenshot_data:
                print("Screenshot captured and saved.")
            else:
                print("Failed to capture screenshot.")
        else:
            print("Required elements for tracking form not found.")
        
        self.clear_cookies()
        self.refresh_page()

    def exit(self):
        """Close the driver and exit the test gracefully."""
        print("Closing test session.")
        self.quit()

# To execute, just call:
# test_instance = Test()
