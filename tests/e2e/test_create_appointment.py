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

def test_create_appointment(browser):
    try:
        browser.get("http://localhost:3000/appointments")
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Create Appointment']"))
        )
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='date']"))
        ).send_keys("31100020240031")
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='patientId']"))
        ).send_keys("1")
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='doctorId']"))
        ).send_keys("1")
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()
        
        # Lidar com o alerta
        WebDriverWait(browser, 20).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert alert_text == "Appointment created successfully!"
        
        # Verificar se o compromisso aparece na lista
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), '2024-10-31T00:31')]"))
        )
        assert browser.find_element(By.XPATH, "//td[contains(text(), '2024-10-31T00:31')]").is_displayed()
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise