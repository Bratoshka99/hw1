import os
import shutil
import glob
import sys

def normalize(filename):
  """Transliterates the Cyrillic alphabet into Latin and replaces all other characters with '_'."""
  filename = filename.lower()
  for i in range(len(filename)):
    if not filename[i].isalnum():
      filename = filename[:i] + "_" + filename[i+1:]
  return filename

def process_folder(folder):
  """Recursively processes the folder and its subfolders."""
  for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if os.path.isdir(path):
      process_folder(path)
    else:
      extension = os.path.splitext(path)[1]
      if extension in KNOWN_EXTENSIONS:
        new_path = os.path.join(folder, normalize(file))
        shutil.move(path, new_path)
      elif extension in ARCHIVE_EXTENSIONS:
        shutil.unpack(path, os.path.join(folder, os.path.splitext(file)[0]))
      else:
        print(f"Unknown extension: {extension}")

if __name__ == "__main__":
  folder = os.path.abspath(r"o:\питончики/import os.py")
  process_folder(folder)

