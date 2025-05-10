import os

# Specify the path where Chroma stores its data (default or custom)
storage_path = "chroma/"  # Default path

# Expand user tilde (~) to full path
storage_path = os.path.expanduser(storage_path)

# List all files in the directory
if os.path.exists(storage_path):
    print("Files in Chroma storage directory:")
    for filename in os.listdir(storage_path):
        print(filename)
else:
    print("Chroma storage directory not found.")
