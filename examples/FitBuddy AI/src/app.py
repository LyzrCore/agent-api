import streamlit as st
import os
from lyzr_agent_api import AgentAPI, ChatRequest
from datetime import datetime
from utils import page_config, style_app, template_end, about_app, social_media
from dotenv import load_dotenv

load_dotenv()

LYZR_API_KEY = os.getenv('X_API_Key')
Agent_ID = os.getenv('AGENT_ID')
User_ID = os.getenv('USER_ID')
Session_ID = os.getenv('SESSION_ID')

page_config()
style_app()


image = "src/logo/lyzr-logo-cut.png"
st.image(image=image, width=100)

st.header("FitBuddy AI")
st.markdown("##### Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview)")
st.markdown('---')

col1, col2, col3 = st.columns(3)

with col1:
    userAge = st.text_input(label='Age')
    userHeight = st.text_input(label='Height', placeholder='in cms')
    userWeight = st.text_input(label="Weight", placeholder='in pound')
    dietType = st.selectbox(label="Diet", options=['Standard', 'Vegetarian', 'Vegan', 'Keto', 'Paleo'])
    foodAllergies = st.text_input(label='Food Allergies & Restrictions')


with col2:
    userGender = st.selectbox(label='Gender', options=['Female', 'Male', 'Other'])
    primaryGoal = st.selectbox(label="Primary Goal", options=['Weight Loss', 'Muscle Gain', 'Improving Endurance', 'General Fitness'])
    secondaryGoal = st.selectbox(label='Secondary Goal', options=['Flexibility', 'Stress Reduction', 'Better Sleep Quality'])
    existingHealthCondition = st.text_input(label='Existing Health Condition')
    physicalLimitaion = st.text_input(label='Physical Limitaion')

with col3:
    activityLevel = st.selectbox('Activity Level', options=['Sedentary', 'Lightly Active', 'Moderate Active', 'Very Active'])
    exerciseExperience = st.selectbox('Exercise Experience', options=['Beginner', 'Intermediate', 'Advance'])
    preferedExerciseType = st.selectbox('Excercise Type', options=['Cardio', 'Strenght Training', 'Yoga', 'HIIT'])
    preferedWorkoutTimes = st.selectbox(label='Workout Time', options=['Morning', 'Afternoon', 'Evening', 'Flexible'])
    workSleepSchedule = st.text_input('Work & Sleep Schedule')

targetDate = st.date_input(label='Target Date')

if st.button('Search'):
    if (userAge and userGender and userHeight and userWeight and targetDate):    
        with st.spinner("Getting the Your Diet and Workout"):
            
            Todaysdate = datetime.today().date()
            UserInfo = {
                            'Diet Type': dietType,
                            'Food Allergies': foodAllergies,
                            'Primary Goal': primaryGoal,
                            'Secondary Goal': secondaryGoal,
                            'Existing Health Condition': existingHealthCondition,
                            'Physical Limitaion': physicalLimitaion,
                            'Activity Level': activityLevel,
                            'Exercise Experience': exerciseExperience,
                            'Prefered ExerciseType': preferedExerciseType,
                            'Prefered Workout Times': preferedWorkoutTimes,
                            'Work & Sleep Schedule': workSleepSchedule
                        }
            
            client = AgentAPI(x_api_key=LYZR_API_KEY)

            chat_json = ChatRequest(
                user_id=User_ID,
                agent_id=Agent_ID,
                message=f"UserAge:{userAge}, UserWeight:{userWeight}, UserHeight:{userHeight}, UserGender:{userGender}, Todays Date:{str(Todaysdate)}-Target Date:{targetDate} and other UserInformation:{UserInfo}",
                session_id=Session_ID
            )

                    
            script = client.chat_with_agent(json_body=chat_json)
                    
            if script:
                st.write(script['response']) 

    else:
        st.warning('First provide the User Data')


template_end()
st.sidebar.markdown('---')
about_app()
st.sidebar.markdown('---')
social_media(justify="space-evenly")