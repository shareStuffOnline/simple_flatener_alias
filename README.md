# simple_flatener_alias
Here’s a simple guide in Markdown format to save the script, make it executable, and set up an alias for easy use:

---

# Guide to Save and Use the `code_to_jsonl.py` Script

## 1. Save the Script
Save the following script as `code_to_jsonl.py` in `/usr/local/bin/` or another directory on your `PATH`.

```bash
sudo vi /usr/local/bin/code_to_jsonl.py
```

Paste the script content into the file and save it.

---

## 2. Make the Script Executable
Set the executable permission for the script:

```bash
sudo chmod +x /usr/local/bin/code_to_jsonl.py
```

---

## 3. Add an Alias
Add an alias to your `.bashrc` file so you can run the script with the `code` command.

```bash
echo 'alias code="python3 /usr/local/bin/code_to_jsonl.py"' >> ~/.bashrc
source ~/.bashrc
```

---

## 4. Run the Command
Now you can use the `code` command to process the current directory and output the templated JSONL to standard output and the clipboard.

```bash
code
```

---

## 5. Example Usage
### Process the Current Directory
```bash
code
```

### Process a Specific Directory
```bash
code /path/to/your/directory
```

### Redirect Output to a File
```bash
code > output.jsonl
```

### Pipe Output to Clipboard (Optional)
If `xclip` is installed, the output is automatically copied to the clipboard. You can also manually pipe it:

```bash
code | xclip -selection clipboard
```

---

## 6. Verify
Check if the script works by running `code` in a directory containing `.txt`, `.py`, `.html`, or `.css` files. The output will be printed to the terminal and copied to the clipboard.

---

## Notes
- Ensure `xclip` is installed for clipboard functionality:
  ```bash
  sudo apt install xclip
  ```
- If you modify the script, make sure to save it and reload the `.bashrc` file:
  ```bash
  source ~/.bashrc
  ```

---

This setup allows you to use the `code` command anywhere on your system to process files and generate JSONL output. Let me know if you need further assistance!
