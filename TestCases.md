# Test Cases – DemoQA Alerts

## 1. Simple Alert Test
**Test Case ID:** TC_ALERT_001  
**Description:** Verify that clicking the "Click Me" button shows a simple alert with correct message.  
**Steps:**
1. Navigate to https://demoqa.com/alerts
2. Click the "Click Me" button under Simple Alert section
3. Capture the alert text
4. Accept the alert
**Expected Result:** Alert appears with text "You clicked a button" and can be accepted.

## 2. Timer Alert Test
**Test Case ID:** TC_ALERT_002  
**Description:** Verify that clicking the "Timer Alert" button shows an alert after 5 seconds.
**Steps:**
1. Navigate to https://demoqa.com/alerts
2. Click the "Timer Alert" button
3. Wait for 5 seconds for the alert to appear
4. Capture the alert text
5. Accept the alert
**Expected Result:** Alert appears after ~5 seconds with text "This alert appeared after 5 seconds" and can be accepted.

## 3. Confirm Alert Test
**Test Case ID:** TC_ALERT_003  
**Description:** Verify that clicking the "Confirm" button shows a confirm alert and the Cancel action works.
**Steps:**
1. Navigate to https://demoqa.com/alerts
2. Click the "Confirm" button
3. Dismiss (Cancel) the alert
4. Verify the result text displayed on page
**Expected Result:** The confirm alert appears, and dismissing it shows "Cancel" in the result text.

## 4. Prompt Alert Test
**Test Case ID:** TC_ALERT_004  
**Description:** Verify that the prompt alert accepts input text and displays it correctly.
**Steps:**
1. Navigate to https://demoqa.com/alerts
2. Click the "Prompt" button
3. Enter text "Pramod QA" in the alert input box
4. Accept the alert
5. Verify the result text displayed on page
**Expected Result:** Prompt alert appears, accepts input "Pramod QA", and the result text contains "Pramod QA".
