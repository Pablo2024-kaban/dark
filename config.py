import os
from dotenv import load_dotenv

load_dotenv()

# Configuration variables loaded from the .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("AIzaSyAVOg8xwBHpWWwrhBT_5yaMVDtN_mYK8Ck")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OLLAMA_BASE_URL = os.getenv("2f0be20052944a4e984381839619ba05.GWvpLJRuFrGfgJbN_VbO-iFx")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_API_KEY = os.getenv("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")
LLAMA_CPP_BASE_URL= os.getenv("LLAMA_CPP_BASE_URL")
