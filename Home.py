# !/usr/bin/env python310
# -*- coding: utf-8 -*-
# __author__ = 'R. Sengupta | r_xn'
# __copyright__ = 'Copyright 2023, Ledgr | www.alphaLedgr.com'
# __credits__ = ['r_xn, s.sengupta,  adasgupta@gmail.com']
# __license__ = 'Ledgr | alphaledgr.com'
# __version__ = '01.02.04'
# __maintainer__ = 'r_xn@alphaledgr.com'
# __emails__ = 'r_xn@alphaledgr.com / response@alphaledgr.com'
# __status__ = 'In active development'

import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
import os

# import html

st.set_page_config(page_title="Home | Ledgr", page_icon=None,
                   layout="centered", initial_sidebar_state="expanded")
direc = os.getcwd()
##################################################################
logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
st.logo(logofile, size="medium", link='https://alphaledgr.com/Blog/',
        icon_image=logofile)
with st.sidebar:
    st.image(logofile, use_container_width=True)
    st.caption("Your unified Fintelligence Portal!")

# #######################################
# Icons and Links ###########################
ytube = f'{direc}/pages/appdata/imgs/ytube.svg'
fbook = f'{direc}/pages/appdata/imgs/fbook.svg'
insta = f'{direc}/pages/appdata/imgs/insta.svg'
linkedin = f'{direc}/pages/appdata/imgs/linkedin.svg'
ledgrblog = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F1.png'

# Hardcoded credentials (just for demo purposes)
#USERNAME = 'user'
#PASSWORD = 'password123'


# Function for login
#@st.cache_resource
#def authenticate(username, password):
#    if username == USERNAME and password == PASSWORD:
 #       return True
#    else:
#        st.stop()
 #       return False


# Main app function
#def main():
    # Streamlit sidebar for navigation
#    st.sidebar.subheader("Authentication and Homepage.")

    # Show login form if not authenticated
 #   if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
 #       st.title("Please Log In or Sign Up!")

        # Get the user's input
#        username = st.text_input("Username")
#        password = st.text_input("Password", type='password')

        # Authenticate on form submission
 #       if st.button("Log In"):
 #           if authenticate(username, password):
  #              st.session_state['authenticated'] = True
 #               st.success("Successfully logged in!")
   #             st.rerun()  # Rerun to load the authenticated page
   #         else:
    #            st.error("Invalid credentials. Please try again.")
     #           st.stop()
      #  else:
       #     st.stop()
 #   else:
  #      st.title("Welcome to the Dashboard")
  #      st.write("You have successfully logged in!")
   #     pass

        # Add functionality for logged-in users, e.g., displaying content, etc.
    #    st.button("Log out", on_click=logout)


# Logout function to clear session state

#def logout():
#    st.session_state['authenticated'] = False
#    st.rerun()  # Rerun to show the login page again


# Run the main function
#if __name__ == "__main__":
#    main()

icon_size = 100
# Main Streamlit app starts here

# link = '[GitHub](http://github.com)'
# icon_size = 100
# logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo.png'
st.markdown(''' <div align="center"><h1>Hello! Welcome to Ledgr.</h1></div>''',
            unsafe_allow_html=True)
st.markdown('''
            <div align="center">
            <h3>Learn how to get started on the platform!</h3></div>''',
            unsafe_allow_html=True)
st.markdown(''' <div align="center"><h3>See below for details</h3></div>''',
            unsafe_allow_html=True)
st.image(f'{direc}/pages/appdata/imgs/The alphaLedgr Web3 Platform.png', use_container_width=True)
with st.container():
    a1, a2 = st.columns([1, 5])
    with a1:
        st.image(f'{direc}/pages/appdata/imgs/LedgrBase.svg',
                 caption='Your Unified Wealth Dashboard')
    with a2:
        st.subheader("Part I: Ledgrbase")
        st.write("Map your existing asset holdings and portfolios.")
        st.write("Review and note their overall performance till date.")

    b1, b2 = st.columns([5, 1])
    with b1:
        st.subheader("Part II: MarketBoard")
        st.write("Calculate Returns from SIPs, Explore ETFs and Mutual Funds.")
    with b2:
        st.image(f'{direc}/pages/appdata/imgs/MarketBoard.png',
                 caption='Market Profiles, Plots and Instruments')
st.write("-------------------------------------------------------------------")
with st.container():
    c1, c2 = st.columns([1, 5])
    with c1:
        st.image(f'{direc}/pages/appdata/imgs/AnalyticsBox.png',
                 caption='Analytics and Information')
    with c2:
        st.subheader("AnalyticsBox")
        st.write("Analyze a Security In-Depth. Visualize Metrics & Indicators")
        st.write("Gather comprehensive knowhow on a selected Security.")
st.write("-------------------------------------------------------------------")
with st.container():
    d1, d2 = st.columns([5, 1])
    with d1:
        st.subheader("InvestmentLab")
        st.write("Optimize Investment Allocations.")
        st.write("Generate Efficient Portfolios to Maximize Returns.")
        st.write("Input assets and amount.")
        st.write(" Select any from 5 Optimized portfolios presented.")
    with d2:
        st.image(f'{direc}/pages/appdata/imgs/InvestmentLab.png',
                 caption='Generate Optimal Portfolios')
st.write("-------------------------------------------------------------------")
with st.container():
    e1, e2 = st.columns([1, 5])

    with e1:
        st.image(f'{direc}/pages/appdata/imgs/ForecastEngine.png',
                 'Forecast Price Ranges using your own inputs.')
    with e2:
        st.subheader("[ForecastEngine]")
        st.write("Train Ledgr's AI")
        st.write("Generate price forecasts for any securities or currencies.")
        st.write("Observe overall trend plots aover multiple timescales")
        st.write("Use the docs and the posts on our Blog to commence!")
        st.write("Please do not forget to drop in your feedback")
st.write("-------------------------------------------------------------------")
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
    st.caption("Our Documentation and Tutorials")
with column5:
    st.image(insta, 'Ledgr @ Instagram')
ft1, ft2, ft3 = st.columns([1, 6, 1])
with ft1:
    st.write(" ")
with ft2:
    st.caption(": 2024 - 2025 | All Rights Resrved  ©  www.alphaLedgr.com | alphaLedgr Technologies Ltd. :")
with ft3:
    st.write(" ")

