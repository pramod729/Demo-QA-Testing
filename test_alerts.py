import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_alerts(driver):
    url = "https://demoqa.com/alerts"
    driver.get(url)

    # ===== SIMPLE ALERT =====
    driver.find_element(By.ID, "alertButton").click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "You clicked a button" in alert_text
    alert.accept()

    # ===== TIMER ALERT =====
    driver.find_element(By.ID, "timerAlertButton").click()
    time.sleep(6)  # wait for alert
    alert2 = driver.switch_to.alert
    alert2_text = alert2.text
    assert "This alert appeared after 5 seconds" in alert2_text
    alert2.accept()

    # ===== CONFIRM ALERT =====
    driver.find_element(By.ID, "confirmButton").click()
    alert3 = driver.switch_to.alert
    alert3.dismiss()  # Cancel alert
    result_confirm = driver.find_element(By.ID, "confirmResult").text
    assert "Cancel" in result_confirm or "cancel" in result_confirm.lower()

    # ===== PROMPT ALERT =====
    driver.find_element(By.ID, "promptButton").click()
    prompt_alert = driver.switch_to.alert
    prompt_alert.send_keys("Pramod QA")
    prompt_alert.accept()
    result_prompt = driver.find_element(By.ID, "promptResult").text
    assert "Pramod QA" in result_prompt
