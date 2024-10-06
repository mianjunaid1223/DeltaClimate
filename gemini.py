import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


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
    "max_output_tokens": 20000,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="""\nCreate a detailed data schedule and generate a long, narrative story in HTML format. Ensure to structure the content using the following:

Use h1 and h2 tags for headings.
Bold important text <b> tag.
Break the content into paragraphs and use bullet points to make the layout visually appealing and easy to read.
Use Daisy UI classes for styling and include inline CSS to enhance the presentation of the text.
Make headings large and prominent.
Structure the content clearly, using bullet points where necessary.
Provide solutions under a separate heading.
Ensure the final result is professional and visually attractive with bg-base-100.
Additionally, include full in timeline given,
futhermore, srictly use these:

1. Introduction: Facing the Climate Crisis
2. Extreme Weather and Environmental Changes
3. Human and Social Impacts
4. Adaptation Efforts and Resilience Building
5. Mitigation and Global Cooperation
6. Solutions

:\n\n{\n  \"story\": \"....................\"}\n"""
    "",
)


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


def process(message: str) -> dict:
    try:
        message: dict = chat_session.send_message(str(message))
        return message.text
    except Exception as e:
        return {"error": str(e)}


