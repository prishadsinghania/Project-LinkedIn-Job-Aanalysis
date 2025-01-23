import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

data = {'Designation': [],
        'Name': [],
        'Location': [],
        'Level_and_involvement': [],
        'job_description': [],
        'Total_applicants': [],
        'Industry_and_Employee_count': [],
        'LinkedIn_Followers': []}

driver.maximize_window()

# Open the LinkedIn website
driver.get('https://www.linkedin.com/')

# The 'driver.maximize_window()' method is used to maximize the browser window.
# It ensures that the browser window occupies the entire screen, providing a better view and experience.

# The 'driver.get()' method is used to navigate to the specified URL, in this case, 'https://www.linkedin.com/'.
# It opens the LinkedIn website in the browser.

mail = input('Enter your Email: ')
password = input('Enter your Password: ')


def Login_func():
    """
    Perform login to the LinkedIn website.

    This function enters the provided email and password into the respective fields on the login page,
    clicks the login button, and waits for 5 seconds to allow for the login process to complete.

    Args:
        None

    Returns:
        None
    """
    Enter_mail = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[2]/div[1]/input')
    Enter_mail.send_keys(mail)
    Enter_pass = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[2]/div[2]/input')
    Enter_pass.send_keys(password)
    login_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/button')
    time.sleep(5)
    login_button.click()


# Call the Login_func() to perform the login operation
Login_func()

def linkdin_data_extraction(link):
    """
    Extract data from a LinkedIn job listing page.

    This function navigates to the provided LinkedIn job listing page, extracts various data points
    such as job title, company name, location, job level, number of applicants, industry, job description,
    and LinkedIn followers, and appends them to the respective lists in the 'data' dictionary.

    Args:
        link (str): The URL of the LinkedIn job listing page.

    Returns:
        None
    """
    # Open the provided link in the browser
    driver.get(link)  
    
    # Find the HTML element (used for scrolling) on the page
    bar = driver.find_element(By.XPATH, '/html')


    for i in range(1, 21):
        time.sleep(2.5)
        try:
            jobs = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section['
                                                  f'1]/div/ul/li[{i}]')
            time.sleep(1)
            jobs.click()
        except:
            print(link[link.find('start'):])
            return None
        time.sleep(1)

        try:
            job_title = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                       '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                       '1]/div/div[1]/div/div[1]/div[1]/a/h2')
            
            # Append job title to 'Designation' list in 'data' dictionary
            data['Designation'].append(job_title.text)  

        except NoSuchElementException:
            data['Designation'].append(np.nan)
        time.sleep(1)

        try:
            company_name = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                          '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                          '1]/div/div[1]/div/div[1]/div[1]/div[1]/span['
                                                          '1]/span[1]/a')
            
            # Append company name to 'Name' list in 'data' dictionary
            data['Name'].append(company_name.text)  

        except NoSuchElementException:
            data['Name'].append(np.nan)
        time.sleep(1)

        try:
            com_location = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                          '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                          '1]/div/div[1]/div/div[1]/div[1]/div[1]/span['
                                                          '1]/span[2]')
            
            # Append location to 'Location' list in 'data' dictionary
            data['Location'].append(com_location.text)  

        except NoSuchElementException:
            data['Location'].append(np.nan)
        time.sleep(1)

        for x in range(4):
            # Scroll down the page
            bar.send_keys(Keys.ARROW_DOWN)  

        try:
            job_level_and_type = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                                '4]/div/div/main/div/section[2]/div/div['
                                                                '2]/div[1]/div/div[1]/div/div[1]/div[1]/div['
                                                                '2]/ul/li[1]/span')
            
            # Append job level to 'Level_and_involvement' list in 'data' dictionary
            data['Level_and_involvement'].append(job_level_and_type.text)  

        except NoSuchElementException:
            data['Level_and_involvement'].append(np.nan)
        time.sleep(1)

        try:
            num_of_applicants = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                               '4]/div/div/main/div/section[2]/div/div['
                                                               '2]/div[1]/div/div[1]/div/div[1]/div[1]/div['
                                                               '1]/span[2]/span[2]/span')
            
            # Append number of applicants to 'Total_applicants' list in 'data' dictionary
            data['Total_applicants'].append(num_of_applicants.text)  

        except NoSuchElementException:
            data['Total_applicants'].append(np.nan)
        time.sleep(1)

        try:
            com_industry_and_employee_num = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                                           '4]/div/div/main/div/section['
                                                                           '2]/div/div[2]/div[1]/div/div['
                                                                           '1]/div/div[1]/div[1]/div['
                                                                           '2]/ul/li[2]/span')
            
            # Append industry and employee count to 'Industry_and_Employee_count' list in 'data' dictionary
            data['Industry_and_Employee_count'].append(com_industry_and_employee_num.text)  

        except NoSuchElementException:
            data['Industry_and_Employee_count'].append(np.nan)
        time.sleep(1)

        try:
            job_description = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                             '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                             '1]/div/div[4]/article')
            
            # Append job description to 'job_description' list in 'data' dictionary
            data['job_description'].append(job_description.text)  

        except NoSuchElementException:
            data['job_description'].append(np.nan)
        time.sleep(1)

        sec_bar = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section['
                                                 '2]/div')
        # Scroll down the secondary bar
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', sec_bar)  
        time.sleep(1.5)

        try:
            followers = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                       '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                       '1]/div/section/section/div[1]/div[1]/div/div[2]/div['
                                                       '2]')
            # Append LinkedIn followers count to 'LinkedIn_Followers' list in 'data' dictionary
            data['LinkedIn_Followers'].append(followers.text)  
        except NoSuchElementException:
            data['LinkedIn_Followers'].append(np.nan)
        time.sleep(1)

def scrape_linkedin_jobs():
    """
    Scrapes job data from multiple pages on LinkedIn job search.

    The function navigates through different pages of job search results on LinkedIn,
    extracts relevant job details, and stores them in the 'data' dictionary.

    Returns:
        None
    """
    # Create a list of values from 0 to 400 (inclusive) in increments of 25
    flag = [i for i in range(0, 401, 25)]  
    
    # Remove the value 0 from the list
    flag.remove(0)  
    
    # Insert the value 1 at the beginning of the list
    flag.insert(0, 1)  

    for i in flag:
        # Calling linkdin_data_extraction func and passing link to different pages as arugment
        linkdin_data_extraction(f'https://www.linkedin.com/jobs/search/?currentJobId=3365364752&f_C=165158%2C1353%2C58396'
                                f'%2C51692521%2C1283%2C6567943%2C1073%2C18145101%2C12770%2C9215331%2C4300%2C1318%2C3178'
                                f'%2C86813252%2C6339%2C210064%2C14439560&f_E=1%2C2%2C3%2C4%2C5%2C6&geoId=102713980&location'
                                f'=India&refresh=true&start={i}')

# Call the function to start scraping
scrape_linkedin_jobs()

def create_DataFrame():
    """
    Creates a DataFrame from the collected job data and saves it as a CSV file.

    The function converts the 'data' dictionary into a DataFrame using pandas,
    and then saves the DataFrame as a CSV file.

    Returns:
        None
    """
    
    # Create a DataFrame from the 'data' dictionary
    df = pd.DataFrame(data)  
    
    # Save the DataFrame as a CSV file
    df.to_csv(r"\Users\prishadsinghania\Documents\LinkedIn Jobs Data Analysis Project\scrapped_data\scrapped_data.csv", index=False)

# Call the func to create DataFrame
create_DataFrame()
