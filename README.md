Project Description
The libgen-chatbot project will provide chatbot functionality over the libgen book library using semantic search, a vector database, and a language model (ChatGPT)

Sprint 1: Search Component
Frontend Tasks
Create a search bar: Build a search bar that allows users to input the name of a book and search for it.

Display search results: Display search results on the frontend when a user enters a search query.

Style search results: Style the search results to be visually appealing and easy to read.

Connect search bar to backend: Connect the search bar to the backend API so that it sends a search request to the server when the user submits the search query.

Backend Tasks
Build API endpoint: Create an endpoint that receives a search query from the frontend and queries the Lib-Gen API for matching book titles.

Parse API response: Parse the API response to extract the relevant book information and return it to the frontend.

Connect to frontend: Send the search results back to the frontend to be displayed to the user.


Sprint 2: Chatbot Functionality
Frontend Tasks
Display selected book information: When a user selects a book from the search results, display the book's relevant information, including author, publisher, and publication year.

Create chat UI: Build a chat UI that allows users to ask questions about the selected book.

Connect chat UI to backend: Connect the chat UI to the backend so that it can retrieve relevant information about the selected book and respond to user questions.

Backend Tasks
Query Lib-Gen API: Use the Lib-Gen API to retrieve the online PDF link for the selected book.

Query OpenAI API: Use the OpenAI API to generate embeddings for the selected book.

Create Pinecone index: Use the embeddings to create a Pinecone index for the book.

Query Pinecone index: Use the Pinecone index to retrieve relevant information about the book in response to user questions in the chat UI.

Connect to frontend: Send the Pinecone index-generated responses back to the frontend to be displayed in the chat UI.