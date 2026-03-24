from fastapi import FastAPI, UploadFile, HTTPException

from services.conversion import jpg_to_pdf

app = FastAPI()

@app.get("/")
def healthcheck():
  return { "message": "OK" }

@app.post("/convert/jpg-to-pdf")
async def convert_jpg_to_pdf(files: list[UploadFile]):
  ALLOWED_FORMATS = ("image/jpeg")

  for file in files:
    if file.content_type not in ALLOWED_FORMATS:
      raise HTTPException(status_code=400, detail="Invalid file type")

  return { "types": [file.content_type for file in files] }
