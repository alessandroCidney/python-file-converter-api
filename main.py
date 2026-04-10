from fastapi import FastAPI, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from services.conversion import jpg_to_pdf

app = FastAPI()

@app.get("/")
def healthcheck():
  return { "message": "OK" }

@app.post("/convert/jpg-to-pdf")
async def convert_jpg_to_pdf(files: list[UploadFile], background_tasks: BackgroundTasks):
  ALLOWED_FORMATS = ("image/jpeg")

  for file in files:
    if file.content_type not in ALLOWED_FORMATS:
      raise HTTPException(status_code=400, detail="Invalid file type")

  try:
    result_file_path = jpg_to_pdf(files, background_tasks)

    return FileResponse(result_file_path)
  except Exception as e:
    print(e)
    raise HTTPException(status_code=500, detail="Internal error during file conversion")
