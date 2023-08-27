from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


chrome_driver = "files\chromedriver.exe"
driver = None

try:
    print("Trying to open the driver with inbuilt chrome driver")
    driver = webdriver.Chrome(chrome_driver)
except Exception as e:
    from mail import send_email
    print("Mission 1 Failed")
    subject = "Driver Opening"
    message = "Driver opening via inbuilt chrome driver failed due to : " + str(e)
    send_email(subject, message)

    try:
        print("Trying to open the driver with online chrome driver")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    except Exception as e:
        print("Mission 2 Failed")
        subject = "Driver Opening"
        message = "Driver opening via online chrome driver failed due to : " + str(e)
        send_email(subject, message)

if driver:
    print("Driver initiated")
    driver.get("https://www.google.com")
    driver.quit()
else:
    print("Driver Failed")