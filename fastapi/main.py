from fastapi import FastAPI

import uvicorn


# Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

# app.include_router(task_router, prefix="/tasks", tags=["Tasks"])


@app.get("/")
def root():
    return {"message": "Server is running 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)