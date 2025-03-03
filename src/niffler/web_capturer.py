import time
from urllib.parse import urlparse

from selenium import webdriver


class WebpageCapturer:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        options.add_argument(f"user-agent={user_agent}")

        self.driver = webdriver.Chrome(options)
        self.driver.maximize_window()

    def capture(self, url):
        [is_x_url, account_name] = self.is_x_account_url(url)
        if not is_x_url:
            return

        self.driver.get(url)
        time.sleep(3)

        self.driver.save_screenshot(f"{account_name}.png")

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


capturer = WebpageCapturer()

capturer.capture("https://x.com/10Ronaldinho")
capturer.capture("https://x.com/elonmusk")

capturer.close()
