from utils import get_file_name
import os
import pypdf
import json
from serpapi import GoogleSearch
from utils import extract_prefered_job_role
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
serp_api_key = os.getenv('SERP_KEY')

def JobFinder(SERP_KEY, OPENAI_API_KEY):
    resume_pdf_content = ""
    file_name = get_file_name(directory="ResumeData")
    file_path = os.path.join("ResumeData", file_name)

    with open(file_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page in range(len(pdf_reader.pages)):
            resume_pdf_content += pdf_reader.pages[page].extract_text()
    
    
    job_role = extract_prefered_job_role(resumeData=resume_pdf_content, OpenAI_API_KEY=OPENAI_API_KEY)

    if job_role:
        params = {
            "engine": "google_jobs",
            "q": job_role,
            "hl": "en",
            "ltype": "1",
            "api_key": SERP_KEY
            }
        
        search = GoogleSearch(params)
        serp_results = search.get_dict()

        
        return serp_results, resume_pdf_content
