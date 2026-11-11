from fastapi import  FastAPI
from mysite.api import ai
import uvicorn


app_router = FastAPI(title='Job Finder Agent', version='1.0.0')
app_router.include_router(ai.ai_router)



if __name__ == '__main__':
    uvicorn.run(app_router, host='127.0.0.1', port=8000)