from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(options=options)

def test_homepage():
    driver = get_driver()
    driver.get("http://example.com")  # replace later with your app URL

    assert "Example" in driver.title

    driver.quit()