import streamlit as st
import google.generativeai as genai
from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(page_title='Prompt Vision Bot', page_icon='chatbot.ico')

# Loading gemini pro model  (Older models)
# model_vision = genai.GenerativeModel('gemini-pro-vision')
# model_pro = genai.GenerativeModel('gemini-pro')

# Newer Models
model_vision = genai.GenerativeModel('gemini-2.0-flash')
model_pro = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(prompt, image):
    if prompt != '' and image is not None:
        response = model_vision.generate_content([prompt, image])
        return response.text
    
    elif prompt != '' and image is None:
        response = model_pro.generate_content(prompt)
        return response.text
    
    elif prompt == '' and image is not None:
        response = model_vision.generate_content(image)
        return response.text
    else:
        return "Please enter the prompt!!"

# Application
st.header('Prompt Vision Bot')
prompt = st.text_input('Input prompt', key='input')

# file upload option
image_file = st.file_uploader('Choose an image file...', type=['jpg', 'jpeg', 'png']) 

image = None

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption='Uploaded image', use_column_width=True)


# submit button
submit = st.button('Ask')

# When submit button is clicked
if submit:
    if prompt != '' and image != None:
        response = get_gemini_response(prompt, image)
        
    elif prompt != '' and image == None:
        response = get_gemini_response(prompt, None)
       
    elif prompt == '' and image != None:
        response = get_gemini_response(prompt, image)


    st.subheader('Response:')
    st.write(response)
