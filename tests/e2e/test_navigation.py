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

def test_navigation_to_doctors(browser):
    browser.get("http://localhost:3000/")
    browser.find_element(By.LINK_TEXT, "Manage Doctors").click()
    assert browser.current_url == "http://localhost:3000/doctors"
    assert browser.find_element(By.XPATH, "//h2[text()='Create Doctor']").is_displayed()

def test_navigation_to_patients(browser):
    browser.get("http://localhost:3000/")
    browser.find_element(By.LINK_TEXT, "Manage Patients").click()
    assert browser.current_url == "http://localhost:3000/patients"
    assert browser.find_element(By.XPATH, "//h2[text()='Create Patient']").is_displayed()

def test_navigation_to_appointments(browser):
    browser.get("http://localhost:3000/")
    browser.find_element(By.LINK_TEXT, "Manage Appointments").click()
    assert browser.current_url == "http://localhost:3000/appointments"
    assert browser.find_element(By.XPATH, "//h2[text()='Create Appointment']").is_displayed()