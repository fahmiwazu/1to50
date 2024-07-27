import time
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
logging.info('This is an info message.')
logging.error('This is an error message.')

# ChromeDriver directory
serv_obj = Service("D:\\Work\\webdriver\\chromedriver-win64\\chromedriver.exe")

# Opening Chrome Browser
driver = webdriver.Chrome(service=serv_obj)

# Maximize Windows
driver.maximize_window()

# Insert Puzzle URI
driver.get("https://zzzscore.com/1to50/en/")

# Automation Algorithm
a=1
while(a!=51):
    driver.find_element(By.XPATH, "//div[normalize-space()='"+str(a)+"']//span[@class='box']").click()
    print("number "+str(a)+" are clicked")
    if(a%6==0):
        time.sleep(1)

    a=a+1

# Complete Puzzle
print("Quiz are completed")

# Retrieve Time Record
time_record = driver.find_element(By.XPATH, "(//div[@id='time'])[1]")
record = time_record.text

# Display time Record
print("Congratulation! your record are "+ record+ " seconds")
time.sleep(10)

# Closing Browser
driver.close()