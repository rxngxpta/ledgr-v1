import streamlit as st
import pandas as pd
from datetime import datetime
import os
direc = os.getcwd()
# Initialize a list to store threads
if 'threads' not in st.session_state:
    st.session_state['threads'] = []

# Function to add a thread
def add_thread(username, content, date_time):
    st.session_state['threads'].append({
        'username': username,
        'content': content,
        'date_time': date_time
    })

# Title of the app
st.title("DiscussionRow")
st.caption("Your Financial MicroBlogging Platform")
logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
st.logo(logofile, size="medium", link='https://alphaledgr.com/Blog/',
        icon_image=logofile)
with st.sidebar:
    st.image(logofile, use_container_width=True)
    st.caption("Your unified Fintelligence Portal!")
    st.caption("Post, comment & share your Portfolios, Earnings and Knowhow.")

# #######################################
# Icons and Links ###########################
ytube = f'{direc}/pages/appdata/imgs/ytube.svg'
fbook = f'{direc}/pages/appdata/imgs/fbook.svg'
insta = f'{direc}/pages/appdata/imgs/insta.svg'
linkedin = f'{direc}/pages/appdata/imgs/linkedin.svg'
ledgrblog = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F1.png'
icon_size = 100
# Section for posting a new thread
st.subheader("Post a New Thread")
username = st.text_input("Username")
content = st.text_area("What's on your mind?")
if st.button("Post"):
    if username and content:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_thread(username, content, date_time)
        st.success("Thread posted!")

# Display all threads
st.subheader("All Threads")
if st.session_state['threads']:
    df = pd.DataFrame(st.session_state['threads'])
    for index, row in df.iterrows():
        st.write(f"**User**: {row['username']}")
        st.write(f"**Posted on**: {row['date_time']}")
        st.write(f"**Content**: {row['content']}")
        st.write("---")

# If there are no threads
else:
    st.write("No threads to display yet.")

column1, column2, column3, column4, column5 = st.columns([1, 1, 1, 2, 1])
with column1:
    st.image(ytube, 'Ledgr\'s YouTube Channel')
with column2:
    st.image(fbook, 'Ledgr\'s FaceBook Page')
with column3:
    st.image(linkedin,  'Ledgr\'s LinkedIn Page')
with column4:
    st.write(" ")
    st.image(ledgrblog,  'Ledgr\'s own Blog', use_container_width=True)
    st.write(" ")
with column5:
    st.image(insta, 'Ledgr @ Instagram')
