from typing import List
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from libgen_api import LibgenSearch
from fastapi.middleware.cors import CORSMiddleware

class Book:
    ID: str
    Author: str
    Title: str
    Publisher: str
    Year: str
    Pages: str
    Language: str
    Size: str
    Extension: str
    Mirror_1: str
    Mirror_2: str
    Mirror_3: str


app = FastAPI()
lg = LibgenSearch()
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
def search_lib_gen(search_string: str) : # -> List[Book] - this throws a fastapi error - address
    print(search_string)
    title_filters = {"Extension": "pdf"}
    titles = lg.search_title_filtered(search_string, title_filters)
    return titles

@app.get("/resolve_download_links", response_class=JSONResponse)
def resolve_download_links(mirror_link: str) -> dict[str, str]:
    item: dict[str, str]= {
        "Mirror_1": mirror_link
    }
    download_links = lg.resolve_download_links(item)
    print(download_links)
    return download_links
    