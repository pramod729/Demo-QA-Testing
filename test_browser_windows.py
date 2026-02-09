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


def test_browser_windows(driver):
    url = "https://demoqa.com/browser-windows"
    driver.get(url)
    
    main_window = driver.current_window_handle

    # Open New Tab
    driver.find_element(By.ID, "tabButton").click()
    time.sleep(1)

    # Switch to new tab
    all_windows = driver.window_handles
    for handle in all_windows:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    # Verify new tab by checking heading
    heading = driver.find_element(By.ID, "sampleHeading").text
    assert "This is a sample page" in heading

    # Close new tab
    driver.close()
    driver.switch_to.window(main_window)

    # Open New Window
    driver.find_element(By.ID, "windowButton").click()
    time.sleep(1)

    # Switch to window
    all_windows = driver.window_handles
    for handle in all_windows:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    # Verify new window by heading
    heading2 = driver.find_element(By.ID, "sampleHeading").text
    assert "This is a sample page" in heading2

    # Close new window
    driver.close()
    driver.switch_to.window(main_window)
