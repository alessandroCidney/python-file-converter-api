from PIL import Image

from fastapi import UploadFile, HTTPException

# IN PROGRESS

def jpg_to_pdf(files: list[UploadFile]):
  images = []

  try:
    images = [
      Image.open(file) for file in files
    ]

    for img in images:
      print(img.filename)
      # img.save("./images_test/{}".format(img.filename))
  except Exception:
    raise HTTPException(status_code=500, detail="Internal error during file conversion")
  finally:
    for img in images:
      img.close()