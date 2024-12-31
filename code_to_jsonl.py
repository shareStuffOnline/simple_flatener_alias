import os
import json
import sys
import subprocess
import sys
#print("Script is running", file=sys.stderr)
def process_directory(directory):
    # Define the file extensions to process
    allowed_extensions = {".txt", ".py", ".html", ".css", ".md"}

    # Get the name of the current script to exclude it
    current_script = os.path.basename(__file__)

    # Collect all JSON records
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

                # Flatten newlines and escape double quotes
                flattened_text = content.replace("\n", " ")
                flattened_text = flattened_text.replace('"', '\\"')

                # Create the JSON record
                record = {
                    "filename": os.path.relpath(file_path, start=directory),
                    "text": flattened_text
                }
                records.append(record)

    # Convert all records to JSONL format
    jsonl_output = "\n".join(json.dumps(record) for record in records)

    # Wrap the JSONL output in the specified template
    template = f'''"on_disk_content":"""You are to use the following data:\n{jsonl_output}\n  to answer the question: """'''

    # Copy the templated output to the Ubuntu clipboard
    try:
        subprocess.run(["xclip", "-selection", "clipboard"], input=template.encode("utf-8"), check=True)
        print("Templated output has been copied to the clipboard.", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Failed to copy to clipboard: {e}", file=sys.stderr)

    # Pass the templated output to standard output
    print(template)

if __name__ == "__main__":
    # Get the directory to process (default to current directory)
    target_directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    process_directory(target_directory)
