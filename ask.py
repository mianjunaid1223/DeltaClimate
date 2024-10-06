import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["ASK"])


def upload_to_gemini(path, mime_type=None):

    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file


def wait_for_files_active(files):
    print("Waiting for file processing...")
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")
    print("...all files ready")
    print()


# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="""
Respond according to the specified timeline and region, incorporating the context of climate change, global warminig, co2 emmisions, greenhouse effect, globally or within the specified country (if provided) for concise answers. Use only HTML for emphasis and highlight key points. Ensure the output is, clear, and aligned with the timeline. keep your response short as posible   """,)


files = [
    upload_to_gemini(
        "SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv",
        mime_type="text/csv",
    ),
    upload_to_gemini("CO2_Emissions_1960-2018.csv", mime_type="text/csv"),
]

# Some files have a processing delay. Wait for them to be ready.
wait_for_files_active(files)

chat_session = model.start_chat(history=[])


def ask(message: str) -> dict:
    try:
        message: dict = chat_session.send_message(str(message))
        return {"answer":message.text}
    except Exception as e:
        return {"error": str(e)}


