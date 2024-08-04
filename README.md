This test brings up a web browser and steps through each of the 11 text extraction algorithms.   
Run it in a virtual environment with all the files in selenium_requirements.txt installed.   
In the virtual environment: python test_w_selenium.py

The server is a minimal machine and is therefore slow. Be patient.   
The server is running tu2txt.py.    
Text is extracted from the tuple:    
    tuple_dict['url'] = 'http://100daystosuccess.com/2022/12/01/3-tips-for-making-the-most-of-your-visit-to-a-marijuana-dispensary/'    
    tuple_dict['length'] = '5867'    
    tuple_dict['offset'] = '37203'    
    tuple_dict['filename'] = 'crawl-data/CC-MAIN-2023-40/segments/1695233510368.33/warc/CC-MAIN-20230928063033-20230928093033-00593.warc.gz'    

The results of each text extraction algorithm are shown in turn for about 10 seconds before proceeding to the next algorithm.    
Hit "enter" on the keyboard to end the test.    

08/03/2024  Updated code to use webdriver-manager, which finds the needed geckodriver.    
