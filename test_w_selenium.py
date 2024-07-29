from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as skeys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service

import ast
import os
import shutil
import time

import requests as rqsts

def load_dict_data_from_file(filename):
    """
    Loads data from a file containing a list of dictionaries into a dictionary.
    """
    # Open the file in read mode 
    with open(filename, 'r') as file:
        # Assuming the data is a Python list of dictionaries 
        data_str = file.read()
        data_str = data_str.strip()
        try:
            data = ast.literal_eval(data_str)
        except (SyntaxError, ValueError) as e:
            raise ValueError(f"Error parsing data: {e}") from e  

    # Check if data is a list of dictionaries
    if not isinstance(data, list):
        raise ValueError("Data in file is not a valid list")

    return data

def gen_tuple_dict():
    tuple_dict = {}
    tuple_dict['url'] = 'http://100daystosuccess.com/2022/12/01/3-tips-for-making-the-most-of-your-visit-to-a-marijuana-dispensary/'
    tuple_dict['length'] = '5867'
    tuple_dict['offset'] = '37203'
    tuple_dict['filename'] = 'crawl-data/CC-MAIN-2023-40/segments/1695233510368.33/warc/CC-MAIN-20230928063033-20230928093033-00593.warc.gz'
    return tuple_dict


temp_dir = "~/_tmp"
if (os.path.exists(temp_dir)):
#    print("removing and recreating temp_dir")
    shutil.rmtree(temp_dir)
os.makedirs(temp_dir)
os.environ["TMPDIR"] = temp_dir

'''
data_file = "tuples_list.txt"  # Replace with your actual filename
try:
    data_list = load_dict_data_from_file(data_file)
    print("Data loaded successfully!")
    print("data_list is: \n", data_list)
except (ValueError, FileNotFoundError) as e:
    print(f"Error loading data: {e}")
'''
'''
warc = data_list[0]["filename"]
length = data_list[0]["length"]
offset = data_list[0]["offset"]
url = data_list[0]["url"]
'''

driver_path = None # 
service = Service(executable_path=driver_path) #Service searches for executable in PATH, since driver_path=none
driver = webdriver.Firefox(service=service)
#driver.get("http://127.0.0.1:8000/") # test locally, run uvicorn tu2txt:app in virtual environment
driver.get("http://tuple-2-txt.site/")

print(driver.title)

tuple_dict = gen_tuple_dict()
warc = tuple_dict["filename"]
length = tuple_dict["length"]
offset = tuple_dict["offset"]
url = tuple_dict["url"]

field_warc = driver.find_element(By.ID, "warc")
field_length = driver.find_element(By.ID, "length")
field_offset = driver.find_element(By.ID, "offset")
field_url = driver.find_element(By.ID, "url")

field_warc.clear
field_length.clear
field_offset.clear
field_url.clear

field_warc.send_keys(warc)
field_length.send_keys(length)
field_offset.send_keys(offset)
field_url.send_keys(url)


#choices = ["goose3", "tika", "tika3", "trafilatura", "readability", "html2txt", "textract", "mcextract", "justext", "inscriptis", "ccrawl", "json", "tar"]
choices = ["goose3", "tika", "tika3", "trafilatura", "readability", "html2txt", "textract", "mcextract", "justext", "inscriptis", "ccrawl"]

for choice in choices:
    button = driver.find_element(By.ID, choice)
    button.click()
    WebDriverWait(driver, 100).until(EC.number_of_windows_to_be(2))
#    driver.switch_to.window(driver.window_handles[-1])
#    result_text = driver.find_element(By.TAG_NAME, "body").text
    time.sleep(10)
    
input("Press Enter to continue and end the test")
driver.quit()
print("\nend of all tests")
