import shutil
import os

# Define the target directory name (replace with your desired name)
target_dir_name = "Copy"

# Get the desktop path using a more robust method
desktop_path = os.path.join(os.path.expanduser("~"), r"C:\Users\Admin\OneDrive\Desktop")  # Expand "~" to user's home directory

# Construct the full path for the target directory
target_dir_path = os.path.join(desktop_path, target_dir_name)

try:
  # Create the directory if it doesn't exist
  if not os.path.exists(target_dir_path):
    os.makedirs(target_dir_path)
    print(f"Directory '{target_dir_name}' created successfully on your desktop.")
  else:
    print(f"Directory '{target_dir_name}' already exists on your desktop.")
except OSError as e:
  print(f"Error creating directory: {e}")

# Define folders within the target directory
text_folder = os.path.join(target_dir_path, "Text")
pdf_folder = os.path.join(target_dir_path, "Pdf")
pictures_folder = os.path.join(target_dir_path, "Pictures")

# Create folders if they don't exist
if not os.path.exists(text_folder):
    os.makedirs(text_folder)
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)
if not os.path.exists(pictures_folder):
    os.makedirs(pictures_folder)

# Source folder path (replace with your actual source folder)
source_folder = r"C:\Users\Admin\OneDrive\Desktop\Test"

# Define file extensions for each folder type
text_extensions = (".txt")
pdf_extensions = (".pdf")
picture_extensions = (".jpg", ".jpeg", ".png")

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    # Construct full source file path
    source_file_path = os.path.join(source_folder, filename)

    # Determine destination folder based on file extension
    destination_folder = None
    if filename.lower().endswith(text_extensions):
        destination_folder = text_folder
    elif filename.lower().endswith(pdf_extensions):
        destination_folder = pdf_folder
    elif filename.lower().endswith(picture_extensions):
        destination_folder = pictures_folder

    # Check if destination folder exists and copy the file if applicable
    if destination_folder:
        destination_file_path = os.path.join(destination_folder, filename)
        try:
            shutil.copy(source_file_path, destination_file_path)
            print(f"Copied '{filename}' to {destination_folder}")
        except OSError as e:
            print(f"Error copying '{filename}': {e}")
