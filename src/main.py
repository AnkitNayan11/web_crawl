from run_converter import run_md_to_txt_conversion_process
from run_cleaning import run_review_cleaning_process
from folder_cleaner import clean_output_folders

if __name__ == "__main__":
    clean_output_folders()
    print("Completed the cleaning process...")
    print("/n")

    run_md_to_txt_conversion_process()
    run_review_cleaning_process()
