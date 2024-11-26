import os
import logging
import subprocess
import sys
import time

# Define paths
root_folder = r"e:\projects\sy0-701"
parsed_path_file = os.path.join(root_folder, "parsed_path.txt")
ch_q_file = os.path.join(root_folder, "ch-q.txt")
batch_file = os.path.join(root_folder, "make_filename.cmd")
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

def run_batch_file(batch_path):
    """Execute a batch file."""
    try:
        result = subprocess.run(batch_path, shell=True, check=True, text=True, capture_output=True)
        log_and_print(f"Batch file executed successfully: {batch_path}")
        log_and_print(f"Batch output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        log_and_print(f"Error executing batch file: {e}. Output:\n{e.stderr}", "error")
        sys.exit(1)

def main():
    # Check if required files exist
    if not os.path.exists(parsed_path_file):
        log_and_print(f"Error: File {parsed_path_file} does not exist.", "error")
        sys.exit(1)

    if not os.path.exists(ch_q_file):
        log_and_print(f"Error: File {ch_q_file} does not exist.", "error")
        sys.exit(1)

    if not os.path.exists(batch_file):
        log_and_print(f"Error: Batch file {batch_file} does not exist.", "error")
        sys.exit(1)

    # Read the parsed path
    with open(parsed_path_file, "r") as f:
        parsed_path = f.read().strip()

    if not os.path.exists(parsed_path):
        log_and_print(f"Error: Parsed path {parsed_path} does not exist.", "error")
        sys.exit(1)

    fixedname_file = os.path.join(parsed_path, "fixedname.jpg")
    if not os.path.exists(fixedname_file):
        log_and_print(f"Error: File {fixedname_file} does not exist in the parsed path.", "error")
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
        os.rename(fixedname_file, new_file_path)
        log_and_print(f"Successfully renamed {fixedname_file} to {new_file_path}.")
    except Exception as e:
        log_and_print(f"Error renaming file: {e}", "error")
        sys.exit(1)

    # Introduce a short delay to ensure visibility
    time.sleep(1)

    # Verify the renamed file exists
    if os.path.exists(new_file_path):
        log_and_print(f"Renamed file is now visible: {new_file_path}")
    else:
        log_and_print(f"Error: Renamed file is not visible after operation: {new_file_path}", "error")
        sys.exit(1)

    # Run the batch file last
    log_and_print("Running the batch file as the final step.")
#    run_batch_file(batch_file)

if __name__ == "__main__":
    log_and_print("Script started.")
    main()
    log_and_print("Script completed successfully.")
