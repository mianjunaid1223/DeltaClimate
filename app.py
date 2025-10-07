from pyreact import pyreact, component, route , JSON_Response, send_file

from gemini import process
import json
from components.navbar import Navbar
from components.story import story
from components.chatp import panel
from components.graph import Graph
from ask import ask
from components.map import cmap
import os
from fastapi.responses import FileResponse
pre_response : dict = {}
with open("pre-response.json") as file:
    pre_response = json.load(file)

years = []
emissions = []

for entry in pre_response["graph"]:
    years.append(entry[0]) 
    emissions.append(float(entry[1]))
@route("/")
async def home(request):
    return f"""
{Navbar()}
<div class="content-wrapper">

{story(data = pre_response.get("story",''), graph = Graph(years=years, emissions=emissions))}
{panel()}
</div>
"""


@route("/gemini", methods=["POST"])
async def gemini(request):


    prompt = await request.json()
    prompt = f""""{prompt.get("cu", "")}, from {prompt.get("from", "")} to {prompt.get("to", "")}"""
    process_result =  process("make long story on climate change ( with proper format and presentaion and also tell solution to that) of "+prompt)
    process_result = json.loads(process_result)

    return JSON_Response({"results": cmap(cu=process_result.get("cu", "")) + process_result.get(
        "story", "Sorry, I don't know the answer. Please try again."
    ) })
@route("/ask", methods=["POST"])
async def gemini(request):

    prompt = await request.json()
    prompt : str = f"""{prompt.get("question", "")} (cuntry: {prompt.get("cu", "")}, timeline: from {prompt.get("from", "")} to {prompt.get("to", "")}) """ 
    process_result =  ask(str(prompt))

    return JSON_Response({"answer":  f"""{process_result.get(
        "answer", "Sorry, I don't know the answer. Please try again."
    ).replace("*","")}"""})

@route("/portfolio-pdf", methods=["GET"])
async def get_portfolio_pdf(request):
    """Generate and serve the DeltaClimate project portfolio PDF."""
    from generate_project_pdf import generate_deltaclimate_pdf
    
    # Generate the PDF if it doesn't exist
    pdf_path = "DeltaClimate_Project_Portfolio.pdf"
    if not os.path.exists(pdf_path):
        generate_deltaclimate_pdf()
    
    # Return the PDF file
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="DeltaClimate_Project_Portfolio.pdf"
    )

app = pyreact.create_app()
pyreact.set_static_dir("static")
pyreact.add_global_css_file("styles.css")
pyreact.set_mode("build")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=3000, reload=True)
