
import os
import markdown2
from bs4 import BeautifulSoup

import os

# Define root project folder
project_root = os.path.join(os.getcwd())

# Define input and output paths
input_folder = os.path.join(project_root, "scrapped_files")
merged_md_path = os.path.join(project_root, "webscraper_result", "merged_reviews.md")
final_txt_path = os.path.join(project_root, "webscraper_result", "extracted_review.txt")

# Step 1: Merge all .md files into one .md file
print(" Merging markdown files...")

with open(merged_md_path, "w", encoding="utf-8") as outfile:
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".md"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(f"# {filename}\n\n")  # Optional: write file name as a header
                outfile.write(infile.read())       # Append file content
                outfile.write("\n\n---\n\n")        # Separator between files
            print(f" Merged: {filename}")

print(f" All markdown files merged into: {merged_md_path}")

# Step 2: Convert merged .md to clean plain text
print(" Converting merged markdown to plain text...")

# Read the merged markdown content
with open(merged_md_path, "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# Convert markdown → HTML → Plain Text
html = markdown2.markdown(md_content)
soup = BeautifulSoup(html, "html.parser")
text_content = soup.get_text()

# Step 3: Write the final plain text output
with open(final_txt_path, "w", encoding="utf-8") as txt_file:
    txt_file.write(text_content)

print(f" Extracted plain text saved to: {final_txt_path}")
