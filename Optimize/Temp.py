import os
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define temporary directories
temp_dirs = [
    r'C:\Windows\Temp',
    os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Temp')
]

# List of important files to preserve
important_files = ['important_file1.txt', 'important_file2.tmp']

def clear_temp_files():
    for temp_dir in temp_dirs:
        logging.info(f"Checking directory: {temp_dir}")
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if file in important_files:
                    logging.info(f"Skipping important file: {file_path}")
                    continue
                try:
                    os.remove(file_path)
                    logging.info(f"Deleted file: {file_path}")
                except Exception as e:
                    logging.warning(f"Failed to delete file: {file_path} - {e}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if any(os.path.join(root, important_file) in dir_path for important_file in important_files):
                    logging.info(f"Skipping directory containing important files: {dir_path}")
                    continue
                try:
                    shutil.rmtree(dir_path)
                    logging.info(f"Deleted directory: {dir_path}")
                except Exception as e:
                    logging.warning(f"Failed to delete directory: {dir_path} - {e}")

if __name__ == "__main__":
    clear_temp_files()
