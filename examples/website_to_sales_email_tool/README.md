# 🚀 Website to Sales Email Generator

This project is a **Streamlit** web application that generates personalized sales emails by scraping content from a given website. It utilizes the **Lyzr Agent API** and **OpenAI** to extract relevant information and compose an email based on user input. You can specify the tone and length of the email, and the app will generate a customized sales email for your product.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)

## Features
- 🌐 **Website Scraping**: Automatically extracts content from the provided website URL.
- 🛍️ **Customizable Product Description**: Accepts a product description to generate more relevant sales emails.
- 🎯 **Tone Selection**: Choose between different email tones such as Formal, Casual, Humorous, and Persuasive.
- 📝 **Email Length Preference**: Customize the desired length of the email with a slider.
- ✉️ **Sales Email Generation**: Leverages the Lyzr Agent and OpenAI to generate a high-quality sales email.

## Tech Stack
- **Python**: Core programming language.
- **Streamlit**: Web framework to create an interactive app.
- **Lyzr Agent API**: Scrapes website content and generates tasks.
- **OpenAI API**: Used for language model generation.
- **Pillow (PIL)**: For image handling (e.g., logo).
- **Dotenv**: To manage environment variables.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- Streamlit
- Lyzr Agent API Key
- OpenAI API Key

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/harshit-lyzr/website_to_sales_email_tool
    cd website-to-sales-email-generator
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables** (see [Environment Variables](#environment-variables)).

5. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Environment Variables

You will need to set up a `.env` file in the root directory of your project with the following keys:
```bash
OPENAI_API_KEY=your_openai_api_key 
LYZR_API_KEY=your_lyzr_api_key 
AGENT_ID=your_lyzr_agent_id
```


- **OPENAI_API_KEY**: Your API key for OpenAI's language models.
- **LYZR_API_KEY**: Your API key for the Lyzr Agent API.
- **AGENT_ID**: The ID of the agent you're using from Lyzr.

## Usage

1. **Enter a Website URL**: Input the URL of the website whose content you want to scrape.
2. **Describe Your Product**: Enter a product description to personalize the sales email.
3. **Select Email Tone**: Choose the tone for the email (Formal, Casual, Humorous, Persuasive).
4. **Choose Preferred Email Length**: Use the slider to specify the word count range of the email.
5. **Generate Email**: Click the "Generate" button, and the app will scrape the website and generate a customized email.

Once completed, the generated email will be displayed on the page.

