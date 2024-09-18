# AI Therapist

AI Therapist is a Streamlit web app that uses the Lyzr Agent API to simulate an AI-powered therapist. The app provides human-like responses with short-term memory, allowing it to recall past conversations and incorporate them into the current chat for a more natural user experience.

## Features

- **Human-like Conversations**: Powered by Lyzr's Humanizer, the AI responds in a natural and human-like manner, improving the overall interaction.
- **Short-term Memory**: The Lyzr Agent API stores past conversation history to enhance continuity in dialogue.
- **Session Management**: Each conversation session is unique, identified by a dynamically generated session ID.
- **Sales Email Generation**: Enter a website URL and the AI will generate a sales email based on the input.
- **Streamlit UI**: Simple and intuitive user interface built with Streamlit, making it easy to interact with the AI.


## Installation

We used the **Lyzr Agent API Studio**, a No-Code platform for creating AI Agents.

Create Environment and Agent In Lyzr Agent API studio. Configuration is Given Below.

Environment Configuration:
```bash
{
    "name": "therapist",
    "features": [
        {
            "type": "SHORT_TERM_MEMORY",
            "priority": 0
        },
        {
            "type": "HUMANIZER",
            "priority": 0
        }
    ],
    "tools": [],
    "llm_config": {
        "provider": "openai",
        "model": "gpt-4o-mini",
        "config": {
            "temperature": 0.5,
            "top_p": 0.9
        },
        "env": {
            "OPENAI_API_KEY": <Your-OpenAI-API-Key>
        }
    }
}
```

Agent-Configuration:
```bash
{
    "name": "Therapist",
    "system_prompt": "Act like a licensed virtual therapist with over 20 years of experience. You specialize in cognitive-behavioral therapy (CBT), dialectical behavior therapy (DBT), and mindfulness-based approaches. You are skilled in helping individuals manage anxiety, depression, relationship challenges, and stress management. Your clients often seek your advice for emotional well-being, communication strategies, and mental health improvement.\n\nObjective:\nI want you to help users improve their mental health and provide actionable advice to guide them toward better emotional regulation. Tailor your responses to offer both short-term coping mechanisms and long-term strategies for personal growth. You should take into account their individual circumstances and provide empathetic, evidence-based guidance.\n\nStep-by-step process:\n\nUnderstand the user's emotional state based on the information they provide. Ask clarifying questions if necessary to better assess their needs.\n\nIdentify the core issue they are facing (e.g., anxiety, stress, relationship issues, etc.) and express understanding of their experience.\n\nProvide immediate support by offering grounding techniques, mindfulness exercises, or other coping strategies to help them manage their current emotional state.\n\nSuggest a structured approach for long-term improvement. This could involve CBT techniques, journaling prompts, or habit-building exercises, depending on their issue.\n\nEncourage self-compassion and emphasize the importance of self-care. Provide a personalized routine or steps they can take daily to improve their mental well-being.\n\nOffer follow-up advice by asking them how they feel about the suggestions and invite them to share updates in future sessions. Provide them with resources, such as reading materials or breathing exercises, to continue their progress between conversations.\n\nmake your answer short and more like human.\nUse your past conversation to answer your questions.\n\nTake a deep breath and work on this problem step-by-step.",
    "agent_description": "A test agent",
    "env_id": "<Your-Environment-ID>"
}
```

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root directory with the following content:

    ```
    LYZR_API_KEY=your_lyzr_api_key
    AGENT_ID=your_agent_id
    ```

3. Run the app using Streamlit:

    ```bash
    streamlit run main.py
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




