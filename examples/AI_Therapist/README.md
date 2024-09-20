# AI Therapist

AI Therapist is a Streamlit web app that uses the Lyzr Agent API to simulate an AI-powered therapist. The app provides human-like responses with short-term memory, allowing it to recall past conversations and incorporate them into the current chat for a more natural user experience.

## Features

- **Human-like Conversations**: Powered by Lyzr's Humanizer, the AI responds in a natural and human-like manner, improving the overall interaction.
- **Short-term Memory**: The Lyzr Agent API stores past conversation history to enhance continuity in dialogue.
- **Session Management**: Each conversation session is unique, identified by a dynamically generated session ID.
- **Sales Email Generation**: Enter a website URL and the AI will generate a sales email based on the input.
- **Streamlit UI**: Simple and intuitive user interface built with Streamlit, making it easy to interact with the AI.


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

## Usage

Once the app is running, you can:

1. View the Lyzr logo on the interface.
2. Enter a website URL in the chat input to generate a sales email.
3. Chat with the AI Therapist by typing in the chat input. The Lyzr Agent will respond based on the past conversation using its short-term memory.
4. The conversation history will be displayed in the chat window for continuity.

## Environment Variables

Make sure to set the following environment variables in your `.env` file:

- `LYZR_API_KEY`: Your Lyzr API key for using the Lyzr Agent's features.
- `AGENT_ID`: The unique identifier for the Lyzr Agent.




