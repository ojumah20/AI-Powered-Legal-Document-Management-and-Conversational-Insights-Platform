from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()

UPLOAD_FOLDER = "./uploaded_docs/"

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"message": f"File {file.filename} uploaded successfully", "path": file_location}
