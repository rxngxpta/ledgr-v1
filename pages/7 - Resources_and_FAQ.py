import pandas as pd
import datetime as dt
import streamlit as st
import os
import base64
import urllib
# Page Setup ##################################################################
st.set_page_config(page_title='Ledgr | Resources & FAQ',
                   layout="wide", initial_sidebar_state="expanded")
direc = os.getcwd()
st.write(direc)
logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
st.logo(logofile, size="medium", link='https://alphaledgr.com/Blog/',
        icon_image=logofile)
with st.sidebar:
    st.image(logofile, use_container_width=True)
    st.caption("Your unified Fintelligence Portal!")
    st.markdown("Get References, FAQs, and more...")

# Icons and Links ###########################
ytube = f'{direc}/pages/appdata/imgs/ytube.svg'
fbook = f'{direc}/pages/appdata/imgs/fbook.svg'
insta = f'{direc}/pages/appdata/imgs/insta.svg'
linkedin = f'{direc}/pages/appdata/imgs/linkedin.svg'
ledgrblog = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F1.png'
dpiit = f'{direc}/pages/appdata/imgs/DIPP182133_ALPHA_LEDGR_TECHNOLOGIES_PRIVATE_LIMITED_RECOGNITION_7640740676963066085.png'
# #############################################################################
nx1, nx2, nx3 = st.columns([1, 4, 1])
with nx1:
    st.write(" ")
with nx2:
    st.title(":FAQ, Resources, Links etc:")
with nx3:
    st.write(" ")
nn12, nn13, nn14 = st.columns([2, 6, 2])
with nn12:
    st.write(" ")
with nn13:
    st.write("Find FAQs, Documentation & Slide Decks etc.")
    st.write("Get Visuals, Videos and of course, grab the LedgrMerch here!!")
with nn14:
    st.write(" ")
st.write(" ------------------------------------------------------------------------------------------------------------------ ")

# ###############################
st.header("1. Frequently Asked Questions")
with st.container():
    st.subheader("1.1. FAQs and Queries")
    st.write("**a. How does Ledgr look to integrate with the existing players?**")
    st.markdown("Ledgr's Value and Service Offerings are different, so are Ledgr's principles of User-driven outlook.")
    st.markdown("Ledgr seeks to integrate and strengthen Users and Markets and therefore seeks to not cannibalize on the Market Capitalization of any Firm in the same sector. The reason is rather simple. Ledgr seeks to ensure Efficient, Knowledge based Decision making processes of Users. The onus of implimenting the insights are on the User. Ledgr's job is to present a lucid, transparent, customizable platform to Users as explained in our Blog Section.")
    st.write("**b. Does one have to know hardcore finance to use Ledgr?**")
    st.markdown("The short answer is No. For cases otherwise, worry not, Ledgr has a dedicated module and shall develop wikis on every component with references.")
    st.markdown("Ledgr aims to make people aware, thereby enabling them to make their independant decisions.")
    st.write("c. **How does one make sustainable wealth with Ledgr?**")
    st.markdown("One can find detailed tutorials and 'How-Tos' in our 'Blog', or the 'About and Tutorials' pages.")
    st.write("**d. What is the Ledgr and how do I access it?**")
    st.markdown(""" Ledgr is an integral of 3 entities. 1. The alphaLedgr.com
               website has all the relevant information, signup and
               access links and also hosts the blog, documentation,
               contacts etc. LedgrApp is a Web3.0 platform which
               is trust independent. This demands a network which is secure
               by design aka the LedgrExchange and a transaction framework
               which hosts both fiat and digital transactions,
               with a Digital Wallet System aka the LedgrWallet.
               They are integrated, the records are immutable to promote
               transparency while being future-proof, auditable by authorities,
               is easy to use and is globally scalable.""")
    st.markdown("""The Website hosts the LedgrApp Link on the Homepage.
               The LedgrExchange and the LedgrWallet also have Signup and
               Registration Links. Ledgr's overall integration makes the
               User experience seamless, engaging, and collaborative.""")
    st.write("**e. Where can one find the Product Details and Manuals?**")
    st.markdown("""There are dedicated sections for each in both the 'Blog'
               and the 'App' """)
    st.write("**f. How can one accrue wealth using the InvestmentLab?**")
    st.markdown("""This is a venture into the InvestmentLab.
                There's a tutorial video for creating a portfolio""")
    st.write("**g. Are LedgrTokens cryptocurrency?**")
    st.markdown("""No. Blockchains are frameworks and tokens are components
                which make the Firm, its Engines and their auxilliaries
                enable seamless in-house operations primarily.
                There are security measures involved as per standard protocol,
                but no transparency issues.
                Ledgr Tokens, if the situation calls for it,
                can and may be audited but only by Authorized Personnel
                from the Reserve Bank or the Regulatory Authorities
                exclusively, for ensuring transparent audits
                and Official Reporting. Ledgr also shall feature a
                Subscription Model. The User is free to choose.""")
    st.write("**h. How do I know that my money is safe with Ledgr?**")
    st.markdown(""" Ledgr operates on Blockchain Utility Tokens,
                just akin to the ones we used in the banks.
                These tokens are immutable, thereby ensuring the validity
                and security of every transaction. Tokens can be exchanged
                against fiat-money at the LedgrExchange Portal and get
                stored in your LedgrWallet. Whatever the invested amount be,
                it is going to be insured to protect all parties. And secondly,
                the Tokens, are purchased as per the Users' requirement as
                Ledgr believes in reducing redundant costs
                to the Users themselves.""")

st.subheader("1.3. Resources & Links")
ss2, ss3, ss4 = st.columns(3)
with ss2:
    st.markdown("'alphaledgr.com's dedicated blog and Ledgr's Whitepaper")
with ss3:
    st.write("The LedgrExchange Portal")
    st.link_button("Go to The LedgrExchange Portal", "https://alphaLedgr.com/")
with ss4:
    st.write("The LedgrWallet System")
    st.link_button("Go to The LedgrExchange Portal", "https://alphaLedgr.com/")
###############################################################################
file0A = f'{direc}/pages/appdata/imgs/Ledgr_Whitepaper_and_Business_Monograph.pdf'
file0 = f'{direc}/pages/appdata/imgs/AlphaLedgr Certificate of Recognition Startup India.pdf'
file1 = f'{direc}/pages/appdata/imgs/Udyam_Registration_Certificate_Final.pdf'

st.header("2. Documentation")
with st.container():
    st.subheader("2.1. Docs and Manuals")
    st.write("2.1.1. Value Proposition, Vision, and Service Proposal")
    st.video(f"{direc}/pages/appdata/imgs/LP1.mp4")
    gl1, gl2, gl3 = st.columns([2, 2, 2])
    with gl1:
        st.write(" ")
    with gl2:
        st.link_button("Value Proposition, Vision, and Service Proposal",
                       "https://www.alphaledgr.com/blog/ledgr-the-firm/business-model")
    with gl3:
        st.write(' ')
    
with st.container():


    st.write("2.1.2. Product Offering")
    st.link_button("Ledgr's Whitepaper", "https://www.alphaledgr.com/blog/ledgr-the-firm/app-architecture")
    

    gi1, gi2, gi3 = st.columns([2, 2, 2])
    with gi1:
        st.write(" ")
    with gi2:
        st.link_button("B. Ledgr's Product Architecture",
                       "https://www.alphaledgr.com/blog/how-ledgr-works/app-architecture")
    with gi3:
        st.write(' ')


    

with st.container():
    st.subheader("2.2. Recognition & Certifications")
    
    st.write("**2.2.1. DPIIT Recognition**")
    with open(file0, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display0 = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="600" height="450" type="application/pdf">'
    st.markdown(pdf_display0, unsafe_allow_html=True)
    st.write(" --------- ")
    st.write("**2.2.2. UDYAM - MSME Certificate**")
    with open(file1, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="600" height="450" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

##############################################################################
# video_file = open(f'{direc}/appdata/imgs/F2B_Ledgrs_BMC.mp4', ''rb'')
# video_bytes = video_file.read()
# st.video(video_file, format="video/mp4", start_time=0,
#          loop=True, autoplay=False, muted=False)
# # with t2:
#     st.write("b. LedgrBase | Overseeing the Macros, grabbing the Micros")
#     video_file = open(f'{direc}/appdata/imgs/video_file_lbase.mp4', "rb')
#     video_bytes = video_file.read()
#     st.video(video_file_lbase, format="video/mp4", start_time=0,
#              loop=True, autoplay=False, muted=False)
# with t3:
#     st.write("c. Analyticsbox | Analyze a security and gather insights")
#     video_file = open(f"{direc}/appdata/imgs/video_file_abox.mp4", "rb")
#     video_bytes = video_file.read()
#     st.video(video_file_abox, format="video/mp4", start_time=0,
#              loop=True, autoplay=False, muted=False)
# with t4:
#     st.write("d. InvestmentLab | Create powerful, efficient portfolios.")
#     video_file = open(f"{direc}/appdata/imgs/video_file_Opt.mp4", "rb")
#     video_bytes = video_file.read()
#     st.video(video_file, format="video/mp4", start_time=0, loop=True,
#  autoplay=False, muted=False)
# with t5:
#     st.write("e. ForecastEngine | Make your own Forecast for any security.")
#     video_file = open(f"{direc}/appdata/imgs/video_file_FEngine.mp4", "rb")
#     video_bytes = video_file.read()
#     st.video(video_file_FEngine, format="video/mp4", start_time=0, loop=True,
# autoplay=False, muted=False)

# st.write(" -----------------------------------------------------------")
# t5A, t6, t7 = st.columns([2, 2, 3])

st.write(" ------------------------------------------------------------ ")
url = "https://shadystuffs.com"
st.write("Check them out here! [link](%s)" % url)
st.write(" ------------------------------------------------------------ ")
st.header("5. Useful Links")
with st.container():
    st.subheader("5.1. Partners who enable us to serve you.")
    st.write("Merch Partner - Shadystuff")
    st.subheader("5.2. Upcoming stuff - or - stuff-in-the-pipeline")

# Pagework2 ###################################################################
# st.write(" ------------------------------------------------------------- ")
# st.header("6. Ledgr Merch")
# with st.container():
#     st.write("Ledgr Worktools and Consumables")
#     st.write("The guys at [ShadyStuffs](%s) are our esteemed Merch Partners' % url)
#     st.markdown("Check them out here [https://shadystuffs.com](%s)")
#     st.write("a. Notebooks, Writing Pads and Stationery")
#     st.write("b. Giftables")
#     st.markdown("Cups & Mugs")
#     s12, s13 = st.columns(2)
#     with s12:
#         st.markdown("Re-cycled Stationery")
#     with s13:
#         st.markdown("Laptop & Cell-Phone Covers and Accessories")
#     st.write("c. Wearables")
#     w1, w2 = st.columns(2)
#     with w1:
#         st.markdown("T-Shirts")
#     with w2:
#         st.markdown("Hoodies & Jackets")
#     st.write("d. Printables")
#     g1, g2 = st.columns(2)
#     with g1:
#         st.markdown("Posters, Data Maps & Cheatsheets")
#     with g2:
#         st.markdown("Stickers, Infographs etc.")
#     st.write("e. Usables")
#     f1, f2, f3 = st.columns(3)
#     with f1:
#         st.markdown("Laptop Covers")
#     with f2:
#         st.markdown("Cellphone Covers and Accessories")
#     with f3:
#         st.markdown("Mousepads and Miscellaneous Accessories")

#     st.write("f. Ledgr Specials and Customizables')
#     j1, j2 = st.columns([2, 3])
#     with j1:
#         st.markdown("Ledgr Specials are rare and shall be featured here.")
#     with j2:
#         st.markdown('Customizable Merchandize Requests can be made here.
#                    This also helps Ledgr's esteemed partner, in particular.')
st.write(" -------------------------------------------------------------")
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
    st.write('')
with t10:
    st.markdown(''': 2024 - 2025 | All Rights Resrved  ©  Ledgr Inc. | www.alphaLedgr.com | alphaLedgr Technologies Ltd. :''' )
with t11:
    st.write("")
st.write(" ------------------------------------------------------------- ")
