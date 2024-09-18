# Job Agent Powered by [Lyzr.ai](https://www.lyzr.ai/)


**Job Agent** is a Streamlit-based web application that allows users to upload their resume and search for jobs tailored to their skills. The app is powered by the [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview) platform, and Serp API to provide AI-driven job search capabilities.

## Features

- Upload your resume (PDF format).
- Search for jobs based on your resume using AI.
- Got the Task status on display
- Get a mail with the matched jobs
- Powered by Lyzr, OpenAI, and Serp API.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.9+
- Required API keys from:
  - OpenAI
  - Lyzr X
  - Serp API
- Installed dependencies from `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-agent.git
   ```

2. Navigate to the project directory:
   ```bash
   cd job-agent
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   X_API_Key=your_lyzr_x_key
   SERP_KEY=your_serp_api_key
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Upload your resume in PDF format using the file uploader.

4. Click the "Search Jobs" button to start the AI-powered job search.

5. View job results displayed in a card layout with details such as:
   - Job title
   - Company name
   - Job description
   - Apply link

6. Apply for jobs directly using the provided link.

## Project Structure

```
Job-Agent/
│
├── src/
│   │   ├── logo/                      # Folder for image assets like logos
│   │   ├── lyzr-logo-cut.png       # Lyzr logo asset (cropped)
│   │   └── lyzr-logo.png           # Lyzr logo asset (standard)
│   │
│   │
│   ├── utils/                      # Utility functions and helper scripts
│   │   │   ├── __init__.py             # Initialize the utils package
│   │   └── utils.py                # Utility functions for the application
│   │
│   ├── __init__.py                 # Initialize the src package
│   │   └── job_finder.py               # Logic for job searching and API interaction
│
├── app.py                          # Main Streamlit app entry point
│
├── .env                            # Environment file for API keys (not tracked in version control)
├── requirements.txt                # List of Python dependencies
└── README.md                       # Project description and setup instructions
```