import streamlit as st 


st.markdown("""

<style>
            .stSlider > slider
            {
            background-color : pink;
            color : white;
            }   

            .stButton > button 
            {
            background-color : yellow;
            color : black;
            border-radiuss : 50%; 
            }
            
</style>      
            
            
            
            
            
            
            
            
""",unsafe_allow_html=True)




st.title("Welcome to basic streamlit app")

f_name = st.text_input("Enter your first name")
l_name = st.text_input("Enter your last name")
age = st.slider("Select your age",1,100)
city = st.selectbox("Select your city ",["Delhi","Mumbai","Bangalore","Pune"])

if st.button("Show details"):
    st.write("First Name",f_name)
    st.write("Last Name",l_name)
    st.write("Age",age)
    st.write("City",city)