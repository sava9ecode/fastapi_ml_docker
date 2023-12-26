# import io

from PIL import Image
from fastapi import FastAPI, UploadFile

from model import model_pipeline

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    # content = image.file.read()

    # image = Image.open(io.BytesIO(content))
    image = Image.open(image.file)

    result = model_pipeline(text, image)
    return {"answer": result}
