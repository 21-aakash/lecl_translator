from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get GROQ API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is available
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable not found. Please set it before running the application.")

# Initialize the model
try:
    model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)
except Exception as e:
    raise RuntimeError(f"Failed to initialize ChatGroq model: {e}")

# Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Initialize the parser
parser = StrOutputParser()

# Create the chain
chain = prompt_template | model | parser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://music-app-kpb2dryucspbqjtcqxttjq.streamlit.app/"],  # Adjust to restrict access to specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define the FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using Langchain runnable interfaces"
)

# Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

