import streamlit as st

st.set_page_config(page_title="My Portfolio",page_icon=":tada:",layout="wide")
with st.container():
    st.header("Welcome to My Portfolio Website! :tada:")
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
                I am Sujan K S, a dedicated machine learning enthusiast from India with a passion for harnessing the power of data to drive innovation and solve complex problems. My journey in the field of machine learning began with a fascination for algorithms and their potential to transform industries.

                Over the years, I have honed my skills in various aspects of machine learning, including data preprocessing, model development, and deployment. I have experience working with popular libraries such as TensorFlow, PyTorch, and Scikit-learn, and I am proficient in programming languages like Python and C++.

                My interests extend to Natural Language Processing (NLP),Nural Network And Deep Learning(NNDL),IOT And Computer Vision ..where I enjoy exploring techniques .  constantly seeking to expand my knowledge and stay updated with the latest advancements in these fields.

                Beyond technical skills, I am a strong advocate for collaboration and continuous learning. I believe that sharing knowledge and working together leads to more innovative solutions. I am excited about the future of machine learning and eager to contribute to projects that make a positive impact on society.
                """
            )
            st.write("[Linkedin URL >](https://www.linkedin.com/in/sujan-k-s-982b62194/)")
    