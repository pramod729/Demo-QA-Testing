import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission(driver):
    url = "https://demoqa.com/automation-practice-form"
    driver.get(url)

    # Fill text fields
    driver.find_element(By.ID, "firstName").send_keys("Pramod")
    driver.find_element(By.ID, "lastName").send_keys("Shrestha")
    driver.find_element(By.ID, "userEmail").send_keys("pramod@example.com")

    # Select gender
    driver.find_element(By.XPATH, "//label[text()='Male']").click()

    # Mobile number
    driver.find_element(By.ID, "userNumber").send_keys("9812345678")

    # Date of Birth (clear & send new date)
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.click()
    dob.clear()
    dob.send_keys("10 May 2000")
    dob.send_keys("\n")

    # Subjects
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    driver.find_element(By.ID, "subjectsInput").send_keys("\n")

    # Hobbies
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()

    # Upload picture
    file_path = os.path.join(os.getcwd(), "sample.jpg")  # include a sample.jpg in repo
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    # Current address
    driver.find_element(By.ID, "currentAddress").send_keys("Kathmandu, Nepal")

    # Select state
    driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
    driver.find_element(By.ID, "react-select-3-input").send_keys("\n")

    # Select city
    driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
    driver.find_element(By.ID, "react-select-4-input").send_keys("\n")

    # Submit
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    # Validate success dialog
    success_text = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
    assert "Thanks for submitting the form" in success_text

    # Close
    driver.find_element(By.ID, "closeLargeModal").click()
