import os

def rename_files_to_lowercase(directory):
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            old_path = os.path.join(root, name)
            new_name = name.lower().replace("_", "-")
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

# Replace 'your-docs-directory' with the path to your docs
rename_files_to_lowercase("natives-reference")
