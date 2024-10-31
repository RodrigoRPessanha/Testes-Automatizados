import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get("http://localhost:3000/")
    assert browser.title == "React App"
    assert browser.find_element(By.XPATH, "//h2[text()='Welcome to the Medical Management System']").is_displayed()