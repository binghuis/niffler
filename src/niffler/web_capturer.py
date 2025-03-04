from os import path
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebpageCapturer:
    DEFAULT_DELAY = 5
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    OUTPUT_PATH = "screenshots"

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(f"user-agent={self.USER_AGENT}")
        options.add_argument("--disable-gpu")
        prefs = {
            # "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.images": 2,
        }
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options)
        self.driver.maximize_window()

    def capture(self, url):
        [is_x_url, account_name] = self.is_x_account_url(url)
        if not is_x_url:
            return

        self.driver.get(url)
        WebDriverWait(self.driver, self.DEFAULT_DELAY).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
            )
        )
        bottom_bar_element = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="BottomBar"]'
        )
        self.driver.execute_script(
            """
            arguments[0].style.display = 'none';
            """,
            bottom_bar_element,
        )
        user_element = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="UserName"]'
        )
        self.driver.execute_script(
            """
            arguments[0].style.scrollMarginTop = '52px';
            arguments[0].scrollIntoView();
            """,
            user_element,
        )
        main_element = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="primaryColumn"]'
        )
        main_element.screenshot(f"{path.join(self.OUTPUT_PATH, account_name)}.png")

    def close(self):
        self.driver.quit()

    @staticmethod
    def is_x_account_url(url):
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        is_valid = (
            parsed.netloc.lower() == "x.com" and len(path) > 0 and "/" not in path
        )
        return [is_valid, path]


if __name__ == "__main__":
    capturer = WebpageCapturer()

    capturer.capture("https://x.com/10Ronaldinho")
    capturer.capture("https://x.com/elonmusk")

    capturer.close()
