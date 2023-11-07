from fastapi import FastAPI, APIRouter,UploadFile
import uvicorn
from fastapi.responses import FileResponse
from pathlib import Path
from PIL import Image
import io


app = FastAPI()

@app.post("/upload/")
async def upload_image(image: UploadFile, output_format: str = "png"):
    # Ensure the uploaded file is a PNG image
    if image.content_type != "image/png":
        return {"error": "Only PNG images are allowed."}
    
    # Save the uploaded PNG image to a temporary directory
    save_path = Path("uploads") / image.filename
    with save_path.open("wb") as f:
        f.write(image.file.read())
        
    input_image = Image.open(save_path)
    
    print('Input image is loaded')
    # #input_data = preprocess_input(input_image)
    result_image = input_image
    # # Save the generated image to a temporary file
    generated_image_path = Path("uploads") / 'output.png'
    result_image.save(generated_image_path)


    return FileResponse(generated_image_path)

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)