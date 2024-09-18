# Lyzr Product Description Generator

Welcome to the **Lyzr Product Description Generator**! This project provides a streamlined tool for generating product descriptions using AI. The application is built using Python, Streamlit, and the LyzrAgent API, which integrates with OpenAI's language model to generate high-quality product descriptions.

## Features

- **Streamlit Interface**: An intuitive and user-friendly interface to input product specifications.
- **AI-Powered Descriptions**: Generates product descriptions using advanced AI models.
- **Environment Configuration**: Leverages environment variables for secure API key management.
- **Session Management**: Maintains agent sessions using Streamlit's session state.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)
- A [Streamlit](https://streamlit.io/) account
- A [Lyzr](https://lyzr.ai) account with API access
- An [OpenAI](https://openai.com) API key

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/harshit-lyzr/product_description_agent.git
    cd product_description_agent
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:

    Create a `.env` file in the project root and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    LYZR_API_KEY=your_lyzr_api_key
    ```

5. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit app in your web browser.
2. Enter the product specifications in the provided text area.
3. Click on the "Generate" button to create a product description.
4. The AI-generated description will be displayed below the input area.

## Code Overview

- **app.py**: The main application file that sets up the Streamlit interface and handles user interactions.
- **LyzrAgent Integration**: The code initializes an instance of `LyzrAgent` to interact with the Lyzr API and generate responses based on the provided product specifications.
- **Environment Management**: API keys are loaded from environment variables using `python-dotenv`.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for providing the framework for the UI.
- [Lyzr](https://lyzr.ai) for the API and agent functionalities.
- [OpenAI](https://openai.com) for the language model API.

---

Powered by Lyzr and OpenAI.
