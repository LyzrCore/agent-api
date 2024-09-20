# Lyzr Property Recommendation Chatbot

This Streamlit app uses the Lyzr Agent API to build a property recommendation chatbot. The chatbot allows users to input their property preferences, and in response, it suggests matching properties by communicating with the Lyzr Agent.

## Requirements

- Python 3.7+
- Streamlit
- Lyzr Agent API
- dotenv for environment variables

## Installation

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
   
2. Run create_agent.py file

   This File creates Environment, Agent and Returns agent_id. This Agent ID used in .env file.  

   ```bash
    python create_agent.py
    ```

3. Create a `.env` file in the root directory with the following content:

    ```
    LYZR_API_KEY=your_lyzr_api_key
    AGENT_ID=your_agent_id
    ```

4. Run the app using Streamlit:

    ```bash
    streamlit run app.py
    ```

## How to Use

- input your property search preferences in the text box provided.
- Click the "Suggest Property" button.
- The chatbot will respond with property recommendations based on your input.
- Example

    **Input:** "I'm looking for a 2-bedroom apartment in New Jersey with a view of the bay."
    **Output:** A list of suggested properties matching your criteria.