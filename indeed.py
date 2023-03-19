import random
import time
import parsel
from time import sleep
import pandas as pd
import numpy as np
from parsel import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


DRIVER_PATH = Service(r"C:\chromedriver.exe")
PROXY = ""
op = webdriver.ChromeOptions()
op.add_argument(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(service=DRIVER_PATH, options=op)

driver.implicitly_wait(3)

Job_data = []
c_type = "NaN"

for page in range(0, 500, 10):
    driver.get(
        f'https://indeed.com/jobs?q=Software+Developer&l=United+States&start={60}')
    time.sleep(random.uniform(8.5, 10.9))
    try:
        close = driver.find_element(
            By.XPATH, '//button[@class="icl-CloseButton icl-Model-close]')
        close.click()
    except:
        pass

        jobs = driver.find_elements(
            By.XPATH, '//div[@class = "css-1m4cuuf e37uo190"]')

        for job in jobs:
            job.location_once_scrolled_into_view
            job.click()
            time.sleep(random.uniform(4.6, 6.9))

            Job_title = driver.find_element(
                By.XPATH, '//h2[@class= "icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded"]').text.strip()

            title = Job_title.split("\n")[0]
            # print(title)
            company = driver.find_element(
                By.XPATH, '//div[@class="css-1h46us2 eu4oa1w0"]').text.strip()
            comp = company.split("\n")[0]
            # print(comp)
            location = driver.find_element(
                By.XPATH, '//div[@class="css-6z8o9s eu4oa1w0"]').text.strip()
            loc = location.split("•")[0]
            # print(loc)
            try:
                type = location.split("•")[1]
                # print(type)
            except:
                # print("Onsite")
                type = "Onsite"
            try:
                salary = driver.find_element(
                    By.XPATH, '//div[@ id = "salaryInfoAndJobType"]').text.strip()
                sal = salary.split("a")
                # print(sal[0])
                try:
                    c_type = sal[-1]
                except:
                    c_type = "NaN"
            except:
                # print("NaN")
                sal = "NaN"
            job_desc = driver.find_element(
                By.XPATH, '//div[@ id = "jobDescriptionText"]').text.strip()
            # print(job_desc)
            data = {'Title': title, 'Company': comp, 'Location': loc, 'Type': type,
                    'Salary': sal[0], 'Contract_type': c_type, 'Job Description': job_desc}
            Job_data.append(data)
            # print(data)

        print('[*] Saving')
        df = pd.DataFrame(Job_data)
        df.to_csv("Indeed_JD_SoftwareDeveloper1.csv")
        driver.quit()
