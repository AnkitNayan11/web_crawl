from run_converter import run_md_to_txt_conversion_process
from run_cleaning import run_review_cleaning_process
from folder_cleaner import clean_output_folders
from programatic_login import *
import asyncio



if __name__ == "__main__":
    print("✅ ######### Step 1: Loading credentials and initializing... #########")
    
    browser_cookies_filePath = '.env_temp_browser_cookies'
    creds_filepath = '.creds_env'
    url = 'https://amazon.in'
    # cookies = get_amazon_cookies(browser_cookies_filepath=browser_cookies_filePath,creds_file_path=creds_filepath)
    # print(cookies)
    import os
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=creds_filepath)
    email = os.getenv('AMAZON_EMAIL')
    password = os.getenv('AMAZON_PASSWORD')
    product = input('Enter the prodct to search:')
    print(product)

    print("\n ✅ ######### Step 2: Navigating Amazon and logging in... #########")
    asyncio.run(amazon_navigation_async(url=url,email=email,password=password,product=product))


    clean_output_folders()
    print("\n ✅ ######### Step 3: Completed the cleaning process... #########")
    print("\n")

    run_md_to_txt_conversion_process()
    print("\n ✅ ######### Step 4: Running Markdown to Text conversion... #########")

    run_review_cleaning_process()
    print("\n ✅ ######### Step 5: Completed review cleaning process ... #########")

