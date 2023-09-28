from PIL import Image #importing all required packages
import streamlit as st


st.set_page_config(page_title="James's Webpage", page_icon=":tada:", layout="wide") #Setting up the name and icom that will display in the tab on your browser.


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ---- LOAD ASSETS ----
img_grok_learning = Image.open("City_coding.png") #Defining images to be used later.
img_web_browser = Image.open("Finished_Web_Code.png")
img_coding = Image.open("Python_Beginners.png")
img_website_code = Image.open("Website_Code.png")

#---- HEADER SECTION ----
with st.container(): #Making the first bit of my website.
    st.subheader("Hi, I am James :wave:") #Writing a subheader
    st.title("These are some things I have done in my Research Project") #writing a title
    st.write("I have used [Grok Learning](https://groklearning.com) and various other sources to learn how to code in Python.")
    st.write("I used Python to code a web browser") #Writing normal text
    st.write("In fact, this website is coded in Python!") 

# ---- What I have done ----#
with st.container(): #Explaing the things I did.
    st.write("---")
    left_column, right_column = st.columns(2) #Defining two columns
    with left_column: #Editing the left column
        st.header("What I Learnt")
        st.write("## ")
        st.write(
            """
            Among other things, I learnt:
            - How to draw with Python Turtle
            - How to use lists and the functions that go with them (.append(), .split(), etc.)
            - How to use loops (for, if, else, elif, while, etc.)
            - How to code a web browser
            - How to code this website
            """
        )
    with right_column: #Editing the right column
        st.image(img_coding) #Inserting an image in the right column

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("What I Did")
    st.write("##")
    image_column, text_column = st.columns((1,2)) #Defining two columns
    with image_column:
        st.image(img_grok_learning) #Inserting an image
    with text_column:
        st.write("Here is a picture of some of the coding that I did on Grok learning.")
with st.container():
    image_column, text_column = st.columns((1,2)) #Defining two columns
    with image_column:
        st.image(img_web_browser) #Inserting an image
    with text_column:
        st.write("Here is a picture of the code used for the web browser I coded.")
with st.container():
    image_column, text_column = st.columns((1,2)) #Defining two images
    with image_column:
        st.image(img_website_code) #Inserting Image
    with text_column:
        st.write("Here is a picture of the code used for this website.")  

# ---- CONTACT ----     
with st.container():
    st.write("---")
    st.header("Give me Feedback")
    st.write("##")

    # Documentation
    contact_form = """
    <form action="https://formsubmit.co/james.millan8@schools.sa.edu.au" method="POST"> 
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
""" #Code for inserting contact form
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True) #Inserting the contact form
with right_column:
    st.empty() #Making the right column empty
