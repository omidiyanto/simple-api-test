from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio
import json

app = FastAPI()

@app.get("/get-json")
async def get_json():
    # Asynchronous file reading
    async def read_json_file(file_path: str):
        loop = asyncio.get_event_loop()
        with open(file_path, "r") as file:
            data = await loop.run_in_executor(None, file.read)
        return json.loads(data)

    # Read JSON from local file
    json_data = await read_json_file("data.json")
    return JSONResponse(content=json_data)
