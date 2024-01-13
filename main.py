from fastapi import FastAPI, UploadFile, File
import pandas

app = FastAPI()

#@app.get("/")
#def home():
    #return "Hello world, minha primeira API"

@app.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    df = pandas.read_csv(file.file)
    data_list = df.to_dict(orient='records')

    result = {"data": data_list}

    return  result
