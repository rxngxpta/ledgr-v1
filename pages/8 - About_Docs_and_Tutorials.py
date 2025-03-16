# !/usr/bin/env python310
# -*- coding: utf-8 -*-
# __author__ = 'R. Sengupta | r_xn'
# __copyright__ = 'Copyright 2023, Ledgr | www.alphaLedgr.com'
# __credits__ = ['r_xn, s.sengupta, adasgupta@gmail.com']
# __license__ = 'Ledgr | alphaledgr.com'
# __version__ = '01.02.04'
# __maintainer__ = 'r_xn@alphaledgr.com'
# __emails__ = 'r_xn@alphaledgr.com / response@alphaledgr.com'
# __status__ = 'In active development'

# Imports #####################################################################
import numpy as np
import pandas as pd
import streamlit as st
# import base64
import os
# from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title='Ledgr | About & Tutorials', layout="wide",
                   initial_sidebar_state="expanded")
direc = os.getcwd()
logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
st.logo(logofile, size="medium", link='https://alphaledgr.com/Blog/',
        icon_image=logofile)
with st.sidebar:
    st.image(logofile, use_container_width=True)
    st.caption("Your unified Fintelligence Portal!")
    st.caption("The How-to's, Docs, Demos and your Queries")
# Icons and Links ###########################
ytube = f'{direc}/pages/appdata/imgs/ytube.svg'
fbook = f'{direc}/pages/appdata/imgs/fbook.svg'
insta = f'{direc}/pages/appdata/imgs/insta.svg'
linkedin = f'{direc}/pages/appdata/imgs/linkedin.svg'
ledgrblog = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F1.png'
n1, n2, n3 = st.columns([2, 6, 2])
with n1:
    st.write(" ")
with n2:
    st.title("About & Documentation")
with n3:
    st.write(" ")
n12, n13, n14 = st.columns([2, 4, 2])
with n12:
    st.write(" ")
with n13:
    st.header("How does Ledgr work")
with n14:
    st.write(" ")
st.write("  ------  ")
with st.container():
    j1, j2, j3 = st.columns([1, 6, 1])
    with j1:
        st.write(' ')
    with j2:
        st.write("Value Proposition, Business Model & Product Architecture")
        video_file = open(f"{direc}/pages/appdata/imgs/F2A.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_file, format="mp4", start_time=0,
                 loop=True, autoplay=False, muted=False)
    with j3:
        st.write(' ')
st.write("-------------------------------------------------------------------")
m1, m2 = st. columns(2)
with m1:
    st.header("Navigate using the Sidebar!!")
    st.markdown(
        """
    - Each app has its unique functionality and presents unique information.

    - Find out more by clicking on them!! Choose any via the Sidebar > .

    - On each page -

        (a) input relevant details,

        (b) authorize the access fee payment

        (c) click submit!!. That's it.

    """)
with m2:
    st.header("Each module is a vending machine!!")
    st.markdown(
        """
    - Assess information, data, plots and signals.

    - Gather overviews, access in-depth analyses on markets & instruments.

    - Get a comprehensive picture of your total wealth,
    \n along with in-depth insights as you navigate through the app-engines.

    - Use LedgrTokens to activate engines and modules as you would like.
    \n Analyze, assess and access the data as a download file.

    """)

st.write("  ---------------------------------------------------------------  ")
uu2, uu3 = st.columns([2, 5])
with uu2:
    st.subheader(":LedgrBase:")
    st.caption("Map your investment portfolios here!")
    st.markdown(
        """
    - Organize all your expenses at the LedgrBase, which your homepage.

    - Unify your asset holdings here.

    - Visualize everything in a set of convenient, interactive dashboards.

    - Build a new Portfolio [For new Users], save it to your profile or share.

    - Track each portfolio at the LedgrBase.

    - Add other asset holdings to 'Your Locker'.

    - Asset classes accepted are currently Securities.

    - Derivatives, Bonds, ETFs & MFs, Crypto & Fiat Money are in development.

    - Provisions for other classes viz Derivatives etc will be included.

    - Trace Performance, Returns due, and gain a clear summary of your Wealth,
    """)
with uu3:
    img12 = f"{direc}/pages/appdata/imgs/Users-Assets.png"
    st.image(img12, use_container_width=True)
    vf1 = open(f"{direc}/pages/appdata/imgs/LP1.mp4", "rb")
    vb1 = vf1.read()
st.write("  ---------------------------------------------------------------  ")
vv23, vv33 = st.columns([2, 5])
with vv23:
    st.image(f"{direc}/pages/appdata/imgs/MarketBoard1.png")
with vv33:
    st.subheader(":MarketBoard:")
    st.caption("Follow Markets, Explore Funds & SIPs and more... ")
    st.markdown(
        """
            - Follow Markets, trace Market Indices.

            - Track their performances over time along with other Markets & Exchanges.

            - Visualize their comparative performance on the opening chart.

            - Navigate through the tabs for specific economies/indices.

            - Explore ETFs and MFs. Get quotes & information summaries.

            - Calculate SIP Returns on the SIP Calculator.

            - Find out your next Returns by inputting relevant data.

            - Know about Performers, Sectoral Activities and commodities.

            - Data from Crypto-currencies like BTC, ETH etc. demand inclusion.

            - Get info on Derivatives like Futures and Option Chains.

            - Get exchange rates and track Volatility indices like India VIX.

            - Know Treasury Rates to gauge the Markets condition holistically.
                """)
st.write("  ---------------------------------------------------------------  ")
vfile = open(f"{direc}/pages/appdata/imgs/F2B_Ledgr's_BMC.mp4", "rb")
vbytes = vfile.read()
st.video(vbytes)
st.write("  ------  ")
va23, va33 = st.columns([3, 5])
with va23:
    st.image(f"{direc}/pages/appdata/imgs/Analytics1.png")
with va33:
    st.subheader(":AnalyticsBox:")
    st.caption("Explore Securities In Depth, Analyze KPIs and Signals!!")
    st.markdown(
        """
        - Get OHLC Price Charts, Volume plots and all relevant info.
        - Access 42+ technical indicators, peruse stochastic signals.
        - Perform complex analyses on Securities with reported data.
        - Generate data reports and download calculated data.
        - Follow Price Movements and other KPIs.
        - Gain insights essential to make informed decisions and ensure maximum returns for your trades or investments.
        """)
    st.image(f"{direc}/pages/appdata/imgs/ANALYZING-AN-ASSET.png", use_container_width=False)

st.write("  ---------------------------------------------------------------  ")
vg23, vg33 = st.columns([3, 5])
with vg23:
    st.image(f"{direc}/pages/appdata/imgs/InvestLab1.png")
with vg33:
    st.subheader(":InvestmentLab:")
    st.caption("Optimize Portfolios, generate efficient allocations. Enjoy greater ROI.")
    st.markdown(
        """
    - Optimize your Investments! Start with a new perspective.
    - Input Securities to include in your Portfolio.
    - Indicate the total amount that you would be willing to allocate !!
    - Drop in the access fees and click submit !!
    - Users with Cashcards have their token automatically deducted from their connected LedgrWallets.*
    - InvestmentLab presents 5 different sets of optimally allocated portfolios with expected outcomes as per your inputs.
    - Choose any one and invest effectively using the InvestmentLab.
    - Alternatively, one may select allocations which Minimizes the Risk Exposure.
    - Or, try out many other combinations of stocks and explore possibilities!
    """)
    st.image(f"{direc}/pages/appdata/imgs/Reasons-for-using-the-portfolio-optimizer.png")# use_container_width=True)

st.write("  ---------------------------------------------------------------  ")
vv23, vv33 = st.columns([3, 5])
with vv23:
    st.image(f"{direc}/pages/appdata/imgs/Forecast1.png")
with vv33:
    st.subheader(":ForecastEngine:")
    st.caption("Train ML-AI Engines, Predict Prices and gather intelligence")
    st.markdown(
        """
    - Predict future price points for any asset or security with Ledgr's AI ForecastingEngines.
    - Get Price Forecasts & Sentimental Analyses on specific securites, overall Markets or specific Market Segments!!
    - Assess yearly, monthly as well as weekly motion of the prices.
    - Explore how security prices move through selected timespan.
    - Run it yourself, by your own rules. Use Ledgr's LSTM, ARIMA or any one of Ledgr's AI Models, input information and then adjust parameters of the engine suiting your requirement, prior to running the algorithms.
    - Please note that on your instruction, the AI model will execute in real-time.
    *Hence, sometimes it may seem to be taking long or the browser may have stalled. However, in reality the AI is running in the back-end.*
    - On completion, predicted prices are presented along with a set of other information.

    """)
    st.image(f"{direc}/pages/appdata/imgs/Forecasting-an-Asset.png")

st.write("  ---------------------------------------------------------------  ")

st.subheader("DiscussionRow")
st.write("In current Design & Development")
st.markdown(
    '''
    - Discuss about your Portfolio, or your Wealth Journey at DiscussionRow forums.

    - Share your Portfolios and or holdings, share opinions, observations, knowledge and most importantly, memes and degeneracy.

    - Content is organized by topics and threads, Users interact via Likes/Dislikes, Comments, shares and posts.

    - Users can build profiles, have friends and interact via the global "DiscussionWall" or across threads, groups, etc.

    - Users can earn LedgrTokens in a few ways other than purchasing them from the LedgrExchange portal.

    They are -

    (a) as initial rewards, intermittent grants and random AirDrops

    (b) by interacting on the platform and performing specific tasks [KYC, Referrals, Subscriptions to sub-plans etc.]

    (c) by participating in collab-work protocols, due-diligence-dropoffs for eg.

    - Threads are moderated, and some moderators shall be selected from active Users, to work along with experts.

    - Get great curated info, news, links, updates etc along with a variety of other content and resources.

    - Build the community, get engaged, grow together.
''')
st.write("-------------------------------------------------------------------")
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
    st.caption(": | 2025 - 2026 | All Rights Resrved  ©  Ledgr Inc. | www.alphaLedgr.com | alphaLedgr Technologies Ltd. :")
with t11:
    st.write(" ")









