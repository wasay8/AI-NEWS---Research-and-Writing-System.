from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer
import streamlit as st


## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

st.set_page_config("New AI", page_icon="📰")
st.title("Ask any latest News")

# topic = st.text_input("Please Enter the topic", placeholder="Latest new about US Elections 2024")


# Initialize session state to store the topic
if "topic" not in st.session_state:
    st.session_state["topic"] = ""

# Input text field that stores its value in session state
st.session_state["topic"] = st.text_input(
    "Please Enter the topic", 
    placeholder="Latest news about US Elections 2024", 
    value=st.session_state["topic"]
)



if crew and st.session_state["topic"]:
    if st.button("Get News"):
        with st.spinner("Generating"):
            result=crew.kickoff(inputs={"topic":st.session_state["topic"]})

        st.success(result)
        

