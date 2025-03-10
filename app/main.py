from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from .routers import hello, auction
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hello.router, prefix="/api/v1")
app.include_router(auction.router, prefix="/api/v1") 

@app.get("/", include_in_schema=False)
async def root():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="BidWize API")
