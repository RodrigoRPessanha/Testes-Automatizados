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

def test_doctor_page(browser):
    browser.get("http://localhost:3000/doctors")
    assert browser.find_element(By.XPATH, "//h2[text()='Create Doctor']").is_displayed()
    
    name_input = browser.find_element(By.XPATH, "//input[@name='name']")
    name_input.send_keys("Dr. John Doe")
    assert name_input.get_attribute("value") == "Dr. John Doe"
    
    specialty_input = browser.find_element(By.XPATH, "//input[@name='specialty']")
    specialty_input.send_keys("Neurology")
    assert specialty_input.get_attribute("value") == "Neurology"
    
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    assert submit_button.is_enabled()