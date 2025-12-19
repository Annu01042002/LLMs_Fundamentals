import os
from dotenv import load_dotenv

load_dotenv()

# Environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY not set in environment")

# Model configuration
GEMINI_MODEL_NAME = "gemini-2.5-flash"

# App settings
MAX_OUTPUT_TOKENS = 2000
TEMPERATURE = 0.4
