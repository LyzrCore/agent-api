import streamlit as st
import os
from lyzr_agent_api import AgentAPI, ChatRequest
from utils import page_config, style_app, template_end, about_app, social_media
from utils import remove_existing_files, save_uploaded_file, get_file_name
from utils import encode_image, gpt_vision_call
from dotenv import load_dotenv

load_dotenv()

LYZR_API_KEY = os.getenv('X_API_Key')
Agent_ID = os.getenv('AGENT_ID')
User_ID = os.getenv('USER_ID')
Session_ID = os.getenv('SESSION_ID')

page_config()
style_app()

ImageData = "ImageData"
os.makedirs(name=ImageData, exist_ok=True)

image = "src/logo/lyzr-logo-cut.png"
st.image(image=image, width=100)

st.header("LeafCare AI")
st.markdown("##### Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview)")
st.markdown('---')

image_file = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

if image_file:
    if st.button('Diagnose'):
        remove_existing_files(directory=ImageData)
        save_uploaded_file(directory=ImageData, uploaded_file=image_file)
        file_name = get_file_name(directory=ImageData)
        image_file_path = os.path.join(ImageData, file_name)
        st.image(image=image_file_path, width=100)
        st.markdown('---')
        with st.spinner("Diagnosis is been processing"):
            base64_image = encode_image(image_file_path)
            leafimageDescription = gpt_vision_call(openai_api_key=os.getenv('OPENAI_API_KEY'),
                                               base64_image=base64_image)
            with st.spinner("Getting the Image description"):
                client = AgentAPI(x_api_key=LYZR_API_KEY)

                chat_json = ChatRequest(
                    user_id=User_ID,
                    agent_id=Agent_ID,
                    message=f"This is the leaf image description:{leafimageDescription}. Provide clear and concise treatment recommendations, including potential products like fungicides, bactericides, fertilizers, and insecticides. Ensure the output includes sections for 'Identified Issues' and 'Suggested Treatments,' and list specific products or actions to remedy the plant's health issues. Use perplexity to find the product regarding treatment, if found then give the link.",
                    session_id=Session_ID
                )

                    
                recommendations = client.chat_with_agent(json_body=chat_json)
                    
                with st.spinner('Generating the Recommendations'):
                    if recommendations:
                        st.write(recommendations) 


else:
    remove_existing_files(directory=ImageData)
    st.warning('Please Upload Leaf Image')


template_end()
st.sidebar.markdown('---')
about_app()
st.sidebar.markdown('---')
social_media(justify="space-evenly")