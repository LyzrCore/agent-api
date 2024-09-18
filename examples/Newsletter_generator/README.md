# Lyzr Newsletter Generator

Welcome to the **Lyzr Newsletter Generator**! This project allows you to generate engaging and informative newsletters using the Lyzr Agent framework combined with OpenAI's language models. The interface is built using Streamlit, providing a user-friendly experience.

## Features

- **Automated Newsletter Generation**: Create newsletters based on a given topic using state-of-the-art AI.
- **Perplexity Search Tool Integration**: Fetch the latest and most relevant insights for your newsletter content.
- **Interactive User Interface**: Powered by Streamlit, offering a simple and responsive interface.

## Prerequisites

Make sure the following are installed:

- Python 3.8+
- Streamlit
- LyzrAgent SDK
- dotenv

Install the required dependencies by running:

```bash
pip install streamlit lyzr_agent python-dotenv
```
# Setup

### Clone the Repository:

```bash
git clone https://github.com/your-username/lyzr-newsletter-generator.git
cd lyzr-newsletter-generator
```

### Set Up Environment Variables:
Create a .env file in the root directory and add your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key
LYZR_API_KEY=your_lyzr_api_key
```

### Run the Application:
Start the Streamlit application:
```bash
streamlit run app.py
```

### How It Works
- The LyzrAgent is initialized with both OpenAI and Lyzr API keys.
- The agent environment is configured with features like tool calling and short-term memory to aid in generating high-quality content.
- Users provide a topic and description, which is processed by the agent to generate a newsletter.
- The generated newsletter includes headlines, structured sections, and a call to action, all designed to engage readers.

### Usage
- Enter the Topic and Description: Provide a brief topic and description for the newsletter in the input area.
- Click "Generate NewsLetter": The AI processes your request and generates a newsletter tailored to your topic.
- View the Generated Content: The output is displayed in markdown format for easy reading and further editing.