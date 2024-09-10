# Lyzr Twitter Agent

A **Streamlit** application powered by **Lyzr Agent API** and **OpenAI** that allows users to research topics by sending queries to the Lyzr API, which then processes the requests and returns responses using a large language model.

## Features

- User-friendly text input interface for querying the Lyzr API.
- Streamlit interface with wide layout and responsive columns for input and output.
- Integrates **OpenAI** and **Lyzr APIs** for query handling and task completion.
- Displays research status and final results within the Streamlit app.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Streamlit installed (`pip install streamlit`)
- Lyzr Agent installed (`pip install lyzr-agent`)
- A valid OpenAI API key and Lyzr API key

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/harshit-lyzr/auto_tweet.git
    cd lyzr-twitter-agent
    ```

2. **Install dependencies**:

    Make sure you have Python and pip installed. Then, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:

    Create a `.env` file in the root directory of the project and add your OpenAI and Lyzr API keys:

    ```bash
    OPENAI_API_KEY=your_openai_api_key
    LYZR_API_KEY=your_lyzr_api_key
    ```

4. **Run the Streamlit app**:

    Launch the application using Streamlit:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your browser (typically, it will open automatically at `http://localhost:8501`).
2. Enter your query in the "Enter Text Here" text box on the left-hand side.
3. Click the **Generate** button to send your query.
4. Wait for the response to be generated. The response will appear on the right-hand side under **Response**.

## Project Structure

```plaintext
.
├── .env                 # API keys for OpenAI and Lyzr
├── app.py               # Main application code
├── requirements.txt     # Python dependencies
└── README.md            # This readme file
