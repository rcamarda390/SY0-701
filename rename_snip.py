import os
import logging
import sys

# Define paths
root_folder = r"e:\projects\sy0-701"
parsed_path_file = os.path.join(root_folder, "parsed_path.txt")
ch_q_file = os.path.join(root_folder, "ch-q.txt")
log_dir = os.path.join(root_folder, "log")
log_file = os.path.join(log_dir, "rename_snip.log")

# Setup logging
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_and_print(message, level="info"):
    """Log a message and print it to the console."""
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)

def main():
    # Check if required files exist
    if not os.path.exists(parsed_path_file):
        log_and_print(f"Error: File {parsed_path_file} does not exist.", "error")
        sys.exit(1)

    if not os.path.exists(ch_q_file):
        log_and_print(f"Error: File {ch_q_file} does not exist.", "error")
        sys.exit(1)

    # Read the parsed path
    with open(parsed_path_file, "r") as f:
        parsed_path = f.read().strip()

    if not os.path.exists(parsed_path):
        log_and_print(f"Error: Parsed path {parsed_path} does not exist.", "error")
        sys.exit(1)

    fixedNameFile = os.path.join(parsed_path, "fixedname.jpg")
    if not os.path.exists(fixedNameFile):
        log_and_print(f"Error: File {fixedNameFile} does not exist in the parsed path.", "error")
        sys.exit(1)

    # Read the new name from ch-q.txt
    with open(ch_q_file, "r") as f:
        new_name = f.read().strip()

    if not new_name:
        log_and_print("Error: ch-q.txt is empty. Cannot determine the new filename.", "error")
        sys.exit(1)

    # Generate the new file path
    new_file_path = os.path.join(parsed_path, f"{new_name}.jpg")

    # Rename the file
    try:
        os.rename(fixedNameFile, new_file_path)
        log_and_print(f"Successfully renamed {fixedNameFile} to {new_file_path}.")
    except Exception as e:
        log_and_print(f"Error renaming file: {e}", "error")
        sys.exit(1)

if __name__ == "__main__":
    log_and_print("Script started.")
    main()
    log_and_print("Script completed successfully.")
