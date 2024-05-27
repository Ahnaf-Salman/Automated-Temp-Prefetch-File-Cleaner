import os
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define Prefetch directory
prefetch_dir = r'C:\Windows\Prefetch'

# List of important files to preserve
important_files = ['important_file1.txt', 'important_file2.tmp']

def clear_prefetch_files():
    logging.info(f"Checking directory: {prefetch_dir}")
    for root, dirs, files in os.walk(prefetch_dir):
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

if __name__ == "__main__":
    clear_prefetch_files()
