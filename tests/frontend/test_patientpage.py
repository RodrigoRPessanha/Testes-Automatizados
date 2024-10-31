import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_patient_page(browser):
    browser.get("http://localhost:3000/patients")
    assert browser.find_element(By.XPATH, "//h2[text()='Create Patient']").is_displayed()
    
    name_input = browser.find_element(By.XPATH, "//input[@name='name']")
    name_input.send_keys("Jane Doe")
    assert name_input.get_attribute("value") == "Jane Doe"
    
    age_input = browser.find_element(By.XPATH, "//input[@name='age']")
    age_input.send_keys("28")
    assert age_input.get_attribute("value") == "28"
    
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    assert submit_button.is_enabled()