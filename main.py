from fastapi import FastAPI, UploadFile, File
import pandas

app = FastAPI()

@app.post("/")
async def create_upload_file(user_id: str, file: UploadFile = File(...)):
    df = pandas.read_csv(file.file)
    data_list = df.to_dict(orient='records')

    result = {"user_id": user_id, "data": data_list}

    return  result
