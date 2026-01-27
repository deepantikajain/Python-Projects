# 🧹 Automatic Folder Cleaner (Python)

A Python automation script that organizes files in a folder by moving them into categorized subfolders like Images, Videos, Documents, Music, Programs, Archives, and Others.

---

## 📌 Features

- ✅ Automatically scans a folder
- ✅ Categorizes files based on extensions
- ✅ Creates folders automatically if they don’t exist
- ✅ Moves files into appropriate folders
- ✅ Handles unknown file types (Others category)
- ✅ Simple and efficient automation script

---

## 🛠️ Technologies Used

- Python 🐍  
- Modules:
  - `os`
  - `shutil`

---

---

## ⚙️ How It Works

The script checks each file in the specified folder and:
- Identifies its file extension
- Matches it with predefined categories
- Moves it to the corresponding folder

---

## 🚀 How to Run the Program

1. Make sure Python is installed on your system.
2. Update the folder path in the script:
  
FOLDER_PATH = r"C:\Users\hp\Downloads"
3. run the python file
                                    python folder_cleaner.py



## EXAMPLE OUTPUT:
  Moved: photo.jpg → Images
Moved: movie.mp4 → Videos
Moved: report.pdf → Documents
Moved: song.mp3 → Music
Moved: setup.exe → Programs
Moved: unknown.xyz → Others
✅ Folder cleaned successfully!



