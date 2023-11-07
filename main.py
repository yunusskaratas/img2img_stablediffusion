from fastapi import FastAPI, APIRouter,UploadFile
import uvicorn
from fastapi.responses import FileResponse
from pathlib import Path


app = FastAPI()

@app.post("/upload/")
async def upload_image(image: UploadFile):
    # Ensure the uploaded file is a PNG image
    if image.content_type != "image/png":
        return {"error": "Only PNG images are allowed."}
    
    # Save the uploaded PNG image to a temporary directory
    save_path = Path("uploads") / image.filename
    with save_path.open("wb") as f:
        f.write(image.file.read())
    
    return {"message": "Image uploaded successfully."}


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)