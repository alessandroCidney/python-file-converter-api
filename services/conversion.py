import uuid

from PIL import Image

from fastapi import UploadFile, BackgroundTasks

from pathlib import Path
import shutil

import shutil

def create_conversion_folder():
  conversion_folder_path = "./temporary_conversion_folder/{}".format(uuid.uuid4())

  Path(conversion_folder_path).mkdir(parents=True, exist_ok=True)

  return conversion_folder_path

def remove_conversion_folder(path: str):
  shutil.rmtree(path)

def jpg_to_pdf(files: list[UploadFile], background_tasks: BackgroundTasks):
  conversion_folder_path = create_conversion_folder()

  try:
    opened_images = [
      Image.open(file.file) for file in files
    ]

    first_image = opened_images[0]
    other_images = opened_images[1:]

    result_file_path = "{}/{}".format(conversion_folder_path, "result_file.pdf")

    first_image.save(result_file_path, save_all=True, append_images=other_images)

    return result_file_path
  finally:
    background_tasks.add_task(remove_conversion_folder, conversion_folder_path)