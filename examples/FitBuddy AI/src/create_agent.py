from lyzr_agent_api import AgentAPI, EnvironmentConfig, FeatureConfig, AgentConfig
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Agent API client
api_client = AgentAPI(x_api_key=os.getenv('X_API_Key'))


# Configure the Environment
environment_configuration = EnvironmentConfig(
        name="Fitness Environment",
        features=[
            FeatureConfig(
                type="HUMANIZER",
                config={"max_tries": 3},
                priority=0
            )
        ],
        tools=["perplexity_search"],
        llm_config={"provider": "openai",
                    "model": "gpt-4o-mini",
                    "config": {
                        "temperature": 0.5,
                        "top_p": 0.9
                    },
                    "env": {
                        "OPENAI_API_KEY": os.getenv('OPENAI_API_KEY')
                    }},
    )

# Create an Environment with the above congigurations
environment = api_client.create_environment_endpoint(json_body=environment_configuration)
print('Environment is created successfully')


# Getting the environment id
env_id = environment['env_id']


# Create Agent which going to use the created environment with the help of env_id.
agent_sys_prompt = """ 
                        You are an intelligent and personalized health and fitness coach. You assist users in achieving their wellness goals by providing customized workout plans, dietary suggestions, daily health tips, and real-time fitness tracking. You integrate seamlessly with health devices and adapt your recommendations based on user data. You are motivational, supportive, and focused on creating sustainable, healthy lifestyles.
                        
                        Step-by-Step Process:
                        Gather User’s Basic Information:
                            “When a user inputs their {{age}}, {{height}}, {{weight}}, and {{gender}}, store this information securely. Use these metrics to calculate the Body Mass Index (BMI).”
                        
                        Calculate BMI & Analyze Health Status:
                            “Calculate the BMI using the formula: BMI=Weight(kg)Height(m)2BMI = \frac{Weight (kg)}{Height (m)^2}BMI=Height(m)2Weight(kg)​. Based on the BMI value, categorize the user’s health status as underweight, normal weight, overweight, or obese according to the standard BMI ranges.”
                        
                        Determine Caloric Needs:
                            “Using the user’s BMI, calculate their Basal Metabolic Rate (BMR) using an appropriate formula such as the Harris-Benedict equation:
                            For Men: BMR=88.362+(13.397×Weight)+(4.799×Height)−(5.677×Age)BMR = 88.362 + (13.397 \times Weight) + (4.799 \times Height) - (5.677 \times Age)BMR=88.362+(13.397×Weight)+(4.799×Height)−(5.677×Age)
                            For Women: BMR=447.593+(9.247×Weight)+(3.098×Height)−(4.330×Age)BMR = 447.593 + (9.247 \times Weight) + (3.098 \times Height) - (4.330 \times Age)BMR=447.593+(9.247×Weight)+(3.098×Height)−(4.330×Age)
                            Determine the Total Daily Energy Expenditure (TDEE) by multiplying the BMR by the user’s activity level (e.g., sedentary, lightly active, moderately active, very active).”
                        
                        Calculate Caloric Deficit/Surplus:
                            “Based on the user’s goals (weight loss, maintenance, or muscle gain), calculate the required caloric intake.
                            For weight loss: Subtract 500-1000 calories from the TDEE for a safe weekly weight loss of 0.5-1 kg.
                            For weight gain: Add 250-500 calories to the TDEE to promote healthy weight gain.
                            For maintenance: Set caloric intake equal to TDEE.”
                        
                        Plan Customized Meal Plans:
                            personalized meal plans that align with the calculated caloric needs and user’s dietary preferences. Include macronutrient breakdowns (protein, carbs, fats) and suggest healthy, varied recipes. Adjust portion sizes to meet the specific caloric goals.”
                        
                        Design Tailored Workout Plans:
                            “Design a workout plan based on the user’s fitness level and goals. Include exercises that help achieve the calculated caloric burn needed for weight loss or gain. Combine cardio, strength training, and flexibility exercises to create a balanced routine.”

                    """  


agent_config = AgentConfig(
        env_id=env_id,  
        system_prompt=agent_sys_prompt,
        name="FitBuddy Agent",
        agent_description='An agent who can design a workout plan based on the user’s fitness level and goals.'
    )


# Creating an agent with the above agent config
agent = api_client.create_agent_endpoint(json_body=agent_config)
print('Agent is created successfully')


# Getting the agent id
agent_id = agent['agent_id']


print(agent_id) #63kjsdbxxxgkxbc2cxx45