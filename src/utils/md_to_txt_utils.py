import os
import glob

def convert_md_to_txt(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)

    md_files = glob.glob(os.path.join(source_folder, "*.md"))

    for md_file in md_files:
        print(f"Processing: {md_file}")

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        base_name = os.path.basename(md_file)
        txt_filename = os.path.splitext(base_name)[0] + ".txt"
        txt_path = os.path.join(destination_folder, txt_filename)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Converted: {base_name} → {txt_path}")
