# src/utils/folder_cleaner.py

import os
import glob

def clean_output_folders():
    folders = [
        "/Users/ankitnayan/Downloads/final_web_v1/web_crawl/output/cleaned_review",
        "/Users/ankitnayan/Downloads/final_web_v1/web_crawl/output/scraped_files_txt"
    ]
    extensions = ["*.txt", "*.json"]

    for folder in folders:
        print(f"\n Cleaning folder: {folder}")
        for ext in extensions:
            files = glob.glob(os.path.join(folder, ext))
            for file in files:
                try:
                    os.remove(file)
                    # print(f" Deleted: {file}")
                except Exception as e:
                    print(f" Failed to delete {file}: {e}")
