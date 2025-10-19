import streamlit as st
import requests 
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Portfolio",page_icon=":tada:",layout="wide")
import json
import streamlit as st
from streamlit_lottie import st_lottie

# Load Lottie animation from local file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lootile_codeing=load_lottiefile("Robot Futuristic Ai animated.json")
cam=load_lottiefile("Headphone with blueberry cartoon.json")
st_lottie(cam,height=200,width=300,key="codings")
st.header("Welcome to My Portfolio :tada:")
with st.container():
    st.divider()
    st.subheader("Hi, I am Sujan K S :smile::wave:")
    st.title("A Machine Learning Enthusiast from India")
    st.write("I am passionate about leveraging machine learning to solve real-world problems and create impactful solutions. With a strong foundation in data analysis, model development, and deployment, I enjoy exploring new technologies and methodologies in the field of artificial intelligence,im also Intrested in Natural Language Processing and Deep Learning,IoT etc..")
    
    
    with st.container():
        st.write("---")
        left_column,right_column=st.columns(2)
        with left_column:
            st.header("About Me")
            st.write("##")
            st.write(
                """
                - I am Sujan K S, a dedicated machine learning enthusiast from India.Driven by the power of  data to drive innovation and solve problems.

                - Over the years, I have honed my skills in various aspects of machine learning, including data preprocessing, model development, and deployment.Using tools such as TensorFlow, PyTorch, and Scikit-learn,With proficient Python and C++.

                - My interests extend to NLP,Nural Network And Deep Learning,IOT And Computer Vision.constantly seeking to expand my knowledge and stay updated with the latest advancements in these fields.

                - Beyond technical skills, I am a strong advocate for collaboration and continuous learning. I believe that sharing knowledge and working together leads to more innovative solutions. I am excited about the future of machine learning and eager to contribute to projects that make a positive impact on society.
                """
            )
            st.write("[Linkedin URL >](https://www.linkedin.com/in/sujan-k-s-982b62194/)")
            
    with right_column:
            st_lottie(lootile_codeing,height=400,width=700,key="coding")