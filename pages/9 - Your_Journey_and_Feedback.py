import pandas as pd
# import datetime as dt
import streamlit as st
import os

st.set_page_config(page_title='Ledgr | Contact Us', layout="wide",
                   initial_sidebar_state="expanded")


direc = os.getcwd()
st.header("Contact, Suggestions & Communication")
logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
st.logo(logofile, size="medium", link='https://alphaledgr.com/Blog/',
        icon_image=logofile)
with st.sidebar:
    st.image(logofile, use_container_width=True)
    st.caption("Some Feedback Please!")

# #######################################
# Icons and Links ###########################
ytube = f'{direc}/pages/appdata/imgs/ytube.svg'
fbook = f'{direc}/pages/appdata/imgs/fbook.svg'
insta = f'{direc}/pages/appdata/imgs/insta.svg'
linkedin =f'{direc}/pages/appdata/imgs/linkedin.svg'
ledgrblog =f'{direc}/pages/appdata/imgs/Ledgr_Logo_F1.png'


icon_size = 100
st.sidebar.caption("Hi. Thanks for your time with Ledgr. Ledgr develops on active guidance from its Users and Visitors. Any suggestion and feedback is welcome!")

st.write("  ---------------------------------------------------------------  ")
c21, c22 = st.columns(2)
with c21:
    st.header("Drop in some wisdom here, please!")
    st.write("Please let us know about your experience and suggestions below:")
    with st.form('Feedback'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        phone = st.number_input("Your Contact Number [Not Mandatory]")
        feedbck_1 = st.text_area("Please write in your message here!!")
        feedbck_2 = st.text_area("Any additional features/ideas/suggestions?")
        exp_level = st.slider(label='Rate your Experience out of 10!',
                              min_value=1, max_value=10,
                              value=6, step=1, help=None)
        submitted = st.form_submit_button("Submit")
        if submitted:
            df_feedback_2 = pd.DataFrame({"Name": [name], "Email": [email],
                                          "Phone": [phone],
                                          "feedbck_1": [feedbck_1],
                                          "feedbck_2": [feedbck_2],
                                          "exp_level": [exp_level]})
            st.write(df_feedback_2)
            df_feedback_2.to_csv(f"{direc}/appdata/User_FBAck.csv")
st.write("  ---------------------------------------------------------------  ")
with c22:
    st.header("2. Acknowledgements")
    st.subheader("*Mentors, Critiques, Collaborators and other partners in crime!*")
    st.caption("To you guys, LedgrTeam fail to articulate their gratitude. Best we can do is deliver, with your guidance as our rudder.")
    st.caption('The list is inexhaustive. People help us by the day. We shall do our best to include as many of them here!')
    list1 = ["Dr. A & S Dasguptas", "Mr. G Bhattacharyya", " Mr. Debayan Chaterjee", "Mr. Pritam Saha", " Mr. D Bose", "Mr. T Sengupta", "Mrs U Sen", "Mr M Sarkar", "Mrs. R Davidson", "Mr M. A. Thiriat", 'Mr Owen Poulain', "Dr. Arnab Dasgupta", "Dr. D. Dasgupta"]
    list2 = ["Guidance, Teaching and Support","Trust & Tactical Advice", "Tactical Advice", "Tactical Advice", "Adoptee and Support", "Support", "Teaching, Advice and Support", "Technical Advisory, Training and Tactical knowhow", "Inspiration and Mentorship", "Support, Inspiration and Guidance",'Partner in Crime', "Hard Guidance, Advisory and observatorship", "Observatorship & Moderating"]
    
    st.header("The Ledgr Community")
    contri1 = pd.DataFrame({"Name or CallSign": list1,
                            'Contribution': list2})
    contri1

st.write("  ---------------------------------------------------------------  ")
column1, column2, column3, column4, column5 = st.columns([1,1,1,2,1])
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
t9, t10, t11 = st.columns([1, 5, 1])
with t9:
    st.write(" ")
with t10:
    st.caption(": | 2024 - 2025 | All Rights Resrved  ©  Ledgr Inc. | www.alphaLedgr.com | alphaLedgr Technologies Ltd. :")
with t11:
    st.write(" ")
