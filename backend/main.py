from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,})

@app.post("/", response_class=HTMLResponse)
async def search(request: Request, search_query: str = Form(...)):
    result = f"You searched for: {search_query}"
    return templates.TemplateResponse("index.html", {"request": request, "result": result, "chatbot": True})


@app.post("/chat", response_class=JSONResponse)
async def chat(request: Request):
    print(request)
    # Get the chat message from the form data
    form_data = await request.form()
    chat_message = form_data["chat_message"]
    
    # Do something with the chat message (e.g. call a chatbot API)
    # For now, just return the message as the bot response
    bot_response = f"Thanks for asking: {chat_message}"
    
    # Return the bot response as a JSON object
    return {"bot_response": bot_response}


@app.get("/")
