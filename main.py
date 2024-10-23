from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def root():
    return {"status": "ok!"}

@app.get("/user/{id}")
def read_id(id: int):
    return {"message": id }