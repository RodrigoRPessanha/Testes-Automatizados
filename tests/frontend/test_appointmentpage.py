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

def test_appointment_page(browser):
    browser.get("http://localhost:3000/appointments")
    assert browser.find_element(By.XPATH, "//h2[text()='Create Appointment']").is_displayed()
    
    date_input = browser.find_element(By.XPATH, "//input[@name='date']")
    date_input.send_keys("31100020240031")
    assert date_input.get_attribute("value") == "2024-10-31T00:31"
    
    patient_id_input = browser.find_element(By.XPATH, "//input[@name='patientId']")
    patient_id_input.send_keys("1")
    assert patient_id_input.get_attribute("value") == "1"
    
    doctor_id_input = browser.find_element(By.XPATH, "//input[@name='doctorId']")
    doctor_id_input.send_keys("1")
    assert doctor_id_input.get_attribute("value") == "1"
    
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    assert submit_button.is_enabled()