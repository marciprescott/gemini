import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)


def generate_response(prompt, temperature=0.5):
    # Configure the API key
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    # Select the model with a generation configuration
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        system_instruction="You are a chatbot that is embedded in a skincare website. You will have access to the database of products and their descriptions. You will answer questions relating to skin type and return a list of products that would work with the skin concern question",
    )
    generation_config = genai.types.GenerationConfig(
        temperature=temperature, top_p=1, top_k=1
    )
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text


genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
