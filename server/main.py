import uvicorn 


if __name__ == "__main__":
    uvicorn.run("main:app.app", log_level="debug")