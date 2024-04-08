import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.auth.router import auth_router
# from backend.notification.router import notif_router
from backend.requests.course.router import course_request_router

app = FastAPI(root_path='/api')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth_router)
# app.include_router(notif_router)
app.include_router(course_request_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=5173)
