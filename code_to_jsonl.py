import os
import json
import sys
import subprocess
from datetime import datetime

def process_directory(directory):
    # Define the file extensions to process
    allowed_extensions = {".txt", ".py", ".html", ".css", ".md", ".json",".js"}

    # Get the name of the current script to exclude it
    current_script = os.path.basename(__file__)

    # Collect all file records
    records = []

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            # Get the file extension
            _, file_extension = os.path.splitext(filename)

            # Check if the file extension is in the allowed list and exclude the script itself
            if file_extension.lower() in allowed_extensions and filename != current_script:
                file_path = os.path.join(root, filename)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Get file metadata
                file_stat = os.stat(file_path)
                metadata = {
                    "size": file_stat.st_size,
                    "last_modified": datetime.fromtimestamp(file_stat.st_mtime).isoformat()
                }

                # Create the file record
                record = {
                    "filename": os.path.relpath(file_path, start=directory),
                    "text": content,
                    "metadata": metadata
                }
                records.append(record)

    # Convert records to JSON format
    json_output = json.dumps({"files": records}, indent=2)

    # Wrap the JSON output in the specified template
    template = f'''
"on_disk_content": """{json_output}"""
'''

    # Copy the templated output to the clipboard using xclip
    try:
        subprocess.run(["xclip", "-selection", "clipboard"], input=template.encode("utf-8"), check=True)
        print("Templated output has been copied to the clipboard using xclip.", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Failed to copy to clipboard: {e}", file=sys.stderr)

    # Pass the templated output to standard output
    print(template)

if __name__ == "__main__":
    # Get the directory to process (default to current directory)
    target_directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    process_directory(target_directory)
