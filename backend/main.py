from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from libgen_api import LibgenSearch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root(): # only for testing
    return {"Hello": "World"}



@app.get("/search", response_class=JSONResponse)
def search_lib_gen(search_string: str):
    print(search_string)
    tf = LibgenSearch()
    title_filters = {"Extension": "pdf"}
    titles = tf.search_title_filtered(search_string, title_filters)
    resolve_download_links = [tf.resolve_download_links(item) for item in titles]
    print(resolve_download_links)
    return titles