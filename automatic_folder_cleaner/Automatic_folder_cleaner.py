import os
import shutil

# Folder path to clean (change this)
FOLDER_PATH = r"C:\Users\hp\Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Programs": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z"]
}

def clean_folder():
    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                target_folder = os.path.join(FOLDER_PATH, folder)

                # Create folder if not exists
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved: {file} → {folder}")
                moved = True
                break

        if not moved:
            # Other files
            other_folder = os.path.join(FOLDER_PATH, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))
            print(f"Moved: {file} → Others")

if __name__ == "__main__":
    clean_folder()
    print("✅ Folder cleaned successfully!")
