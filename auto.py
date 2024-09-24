from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pywinauto.application import Application
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

gender_flag = -1
age_flag = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--lang=en")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def checkNum(num):
    return str(num).zfill(2)

def read_variables(filename):
    settings = {}
    with open(filename, 'r') as file:
        for line in file:
            name, value = line.split('=')
            name = name.strip()
            value = eval(value.strip())
            settings[name] = value
    return settings

def CreateCampaign(num):
    Create_Campaigns = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".ant-btn-primary"))
    )
    Create_Campaigns[0].click()

    campaign_name_input = driver.find_element(By.ID, "name")
    campaign_name_str = "abibi_" + checkNum(num+1)
    campaign_name_input.send_keys(campaign_name_str)

    Save_next = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".ant-btn-primary"))
    )
    Save_next[2].click()

def CreateAdset(num):
    global gender_flag

   
    for attempt in range(3): 
        try:
            ad_set_name_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "name"))
            )
            time.sleep(2)
            ad_set_name_str = "abibi_adset_" + checkNum(num+1)

            ad_set_name_input.send_keys(" ") 
            ad_set_name_input.send_keys(Keys.BACKSPACE)  
            time.sleep(1)
            ad_set_name_input.send_keys(ad_set_name_str)
            break

        except StaleElementReferenceException:
            print("Encountered StaleElementReferenceException, retrying...")
            time.sleep(2)  
        except Exception as e:
            print(f"Error in CreateAdset: {e}")
            break    
    time.sleep(2)
    Gender_label_element = driver.find_elements(By.CSS_SELECTOR, "label.ant-checkbox-wrapper")
    if num % 5 == 0:
        gender_flag += 1
    driver.execute_script("arguments[0].scrollIntoView(true);", Gender_label_element[10])
    time.sleep(1)
    if 10 != (10 + gender_flag):
        Gender_label_element[10 + gender_flag].click()

    Age_label_element = driver.find_elements(By.CSS_SELECTOR, "label.ant-checkbox-wrapper")
    if num != 0:
        Age_label_element[13 + num%5].click()

    now_data_input = driver.find_element(By.ID, "startTime")
    driver.execute_script("arguments[0].scrollIntoView(true);", now_data_input)
    time.sleep(1)
    now_data_input.click()

    Now_data_btn = driver.find_element(By.CLASS_NAME, "ant-picker-now-btn")
    Now_data_btn.click()

    Daily_budge_input = driver.find_element(By.ID, "budget")
    driver.execute_script("arguments[0].scrollIntoView(true);", Daily_budge_input)
    time.sleep(1)
    Daily_budge_input.send_keys(settings['dailyBudget'])

    Bid_type_radio = driver.find_elements(By.CLASS_NAME, "ant-radio-input")
    Bid_type_radio[6].click()

    Bid_rate_input = driver.find_element(By.ID, "bidRate")
    driver.execute_script("arguments[0].scrollIntoView(true);", Bid_rate_input)
    time.sleep(1)
    Bid_rate_input.send_keys(settings['bid_Rate'])

    Delivery_rate_radio = driver.find_elements(By.CLASS_NAME, "ant-radio-input")
    Delivery_rate_radio[11].click()

    New_time_slot_btn = driver.find_elements(By.CLASS_NAME, "ant-btn-default")
    driver.execute_script("arguments[0].scrollIntoView(true);", New_time_slot_btn[3])
    time.sleep(1)
    New_time_slot_btn[3].click()

    Frequency_cap_input_1 = driver.find_elements(By.CLASS_NAME, "ant-input-number-input")
    Frequency_cap_input_1[2].send_keys("1")

    Frequency_cap_input_2 = driver.find_elements(By.CLASS_NAME, "ant-select-selection-search-input")
    Frequency_cap_input_2[3].click()
    Day_option_div = driver.find_elements(By.CSS_SELECTOR, "div.ant-select-item-option-content")
    Day_option_div[0].click()

    Save_next_ad_btn = driver.find_elements(By.CLASS_NAME, "ant-btn-primary")
    Save_next_ad_btn[3].click()

    time.sleep(5)
    Proceed_btn = driver.find_elements(By.CLASS_NAME, "ant-btn-default")
    Proceed_btn[5].click()

def CreateAd(num):
    for attempt in range(3): 
        try:
            ad_name_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "name"))
            )
            time.sleep(2)
            ad_name_str = "abibi_ad_" + checkNum(num+1)

            ad_name_input.send_keys(" ") 
            ad_name_input.send_keys(Keys.BACKSPACE)  
            time.sleep(1)
            ad_name_input.send_keys(ad_name_str)
            break

        except StaleElementReferenceException:
            print("Encountered StaleElementReferenceException, retrying...")
            time.sleep(2) 
        except Exception as e:
            print(f"Error in CreateAdset: {e}")
            break  
    time.sleep(2)
    Title_textarea = driver.find_elements(By.CSS_SELECTOR, "textarea.ant-input")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", Title_textarea[0])
    Title_textarea[0].send_keys("They Tried to Ban This Wrinkle Fix")

    Image_upload_input = driver.find_element(By.ID, "creative_assetUrl")
    driver.execute_script("arguments[0].scrollIntoView(true);", Image_upload_input)
    time.sleep(2)
    Image_upload_input.click()

    time.sleep(2)
    app = Application().connect(title_re="Open")
    dialog = app.window(title_re="Open")
    file_path = os.path.abspath("./assets/image/1.jpg")
    dialog.Edit.set_text(file_path)
    dialog.Open.click()

    time.sleep(2)
    Upload_without_crop_btn = driver.find_elements(By.CSS_SELECTOR, "button.ant-btn-default")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView(true);", Upload_without_crop_btn[5])
    time.sleep(5)
    Upload_without_crop_btn[5].click()

    time.sleep(2)
    Description_textarea = driver.find_elements(By.CSS_SELECTOR, "textarea.ant-input")
    driver.execute_script("arguments[0].scrollIntoView(true);", Description_textarea[1])
    Description_textarea[1].send_keys("Big Skincare doesn't want you to see See the (controversial) truth about anti-aging and…")

    Text_on_btn = driver.find_element(By.ID, "creative_callToAction")
    Text_on_btn.click()
    time.sleep(2)
    Customized_text = driver.find_elements(By.CSS_SELECTOR, "input.flex-1")
    Customized_text[0].send_keys("Watch Now")
    time.sleep(2)
    Ok_btn = driver.find_elements(By.CSS_SELECTOR, "button.ant-btn-link")
    Ok_btn[4].click()
    time.sleep(2)
    Watch_now_option = driver.find_elements(By.CSS_SELECTOR, "div.ant-select-item-option-content")
    Watch_now_option[0].click()

    Brand_name_textarea = driver.find_elements(By.CSS_SELECTOR, "textarea.ant-input")
    Brand_name_textarea[2].send_keys("Your Skin Report")

    Logo_upload_div = driver.find_element(By.ID, "creative_logoUrl")
    Logo_upload_div.click()

    time.sleep(2)
    app = Application().connect(title_re="Open")
    dialog = app.window(title_re="Open")
    file_path = os.path.abspath("./assets/logo/1.png")
    dialog.Edit.set_text(file_path)
    dialog.Open.click()

    LandingPage_Url_input = driver.find_element(By.ID, "creative_clickThroughUrl")
    LandingPage_Url_input.send_keys("https://t.cerial.org/663fe16475c8a80001d7a66e?sub1=__CAMPAIGN_ID__&sub2=__CAMPAIGN_NAME__&sub3=__FLIGHT_ID__&sub4=__FLIGHT_NAME__&sub5=__CREATIVE_ID__&sub6=__CREATIVE_NAME__&sub7=__OS__&sub8=__IS_LAT__&ref_id=__CALLBACK_PARAM__")

    Submit_btn = driver.find_elements(By.CSS_SELECTOR, "button.ant-btn-primary")
    time.sleep(2)
    Submit_btn[2].click()
    time.sleep(10)

if __name__ == "__main__":
        
    filename = 'settings.txt'
    settings = read_variables(filename)

    #Create browser and signin
    try:
        driver.get("https://admanager.newsbreak.com/signin")
        driver.maximize_window()
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "basic_email"))
        )
        password_input = driver.find_element(By.ID, "basic_password")
        username_input.send_keys(settings['username'])
        password_input.send_keys(settings['password'])
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
        )
        driver.execute_script("arguments[0].click();", login_button[1])
    except Exception as e:
        print("Error on openning and signing:", e)

    time.sleep(20)

    # Select the Ad management
    Ad_management_li = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-pro-sider-menu li:nth-child(2)"))
    )
    Ad_management_li.click()

    time.sleep(10)

    campaign_tag = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".guide-mask"))
    )
    driver.execute_script("arguments[0].click();", campaign_tag)
    time.sleep(2)
    for i in range(15):    
        if(i != 0):
            Campaigns_btn = driver.find_element(By.ID, "rc-tabs-0-tab-campaign")
            Campaigns_btn.click()
        CreateCampaign(i)
        CreateAdset(i)
        CreateAd(i)