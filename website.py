import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

# Inserting Images
ytb = Image.open('images/yti.ico')
img1 = Image.open('images/1.PNG')
img2 = Image.open('images/2.PNG')
img3 = Image.open('images/3.PNG')
img4 = Image.open('images/4.PNG')
img5 = Image.open('images/5.PNG')
img6 = Image.open('images/6.PNG')
img7 = Image.open('images/7.PNG')


# Website Settings
st.set_page_config(page_title="Youtube Shorts/Videos Watcher", page_icon=ytb, layout='wide')

# Inserting Lottiefile
def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)


ytplay = load_lottiefile('lottiefiles/ytplay.json')
ytlike = load_lottiefile('lottiefiles/ytlike.json')


# Removing Streamlit Watermark
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css('style/style.css')



# Website Body
with st.container():
    st.markdown("<h3 style='text-align: center; color: White;'>You have a Youtube channel and you need 4000 Hours?</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: White;'>Are you tired wasting time and energy sharing your videos link?</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: Red;'>We Created the Solution!</h2>", unsafe_allow_html=True)
    clm1, clm2, clm3 = st.columns(3)
    with clm1:
        st.write(' ')
    with clm2:
        st_lottie(ytplay, height=200)
    with clm3:
        st.write(' ')
st.write("---")
st.markdown("<h2 style='text-align: center; color: White;'>Every successful Youtube Channel out there struggled with this Youtube requirement once. But You my friend have the Ultimate Solution!</h2>", unsafe_allow_html=True)
st.write('##')
st.markdown("<h1 style='text-align: center; color: Red;'>Youtube Shorts/Videos Watcher</h1>", unsafe_allow_html=True)
cl1, cl2 = st.columns(2)
with cl1:
    st.write('##')
    st.write('##')
    st.write('Whether you want 4000 Public Watch Hours or 10M Public Shorts Views.')
    st.write('We got you covered my friend!')
with cl2:
    st_lottie(ytlike, height=200, width=200)

st.write("---")
st.markdown("<h1 style='text-align: center; color: Red;'>What is Youtube Shorts/Videos Watcher?</h1>", unsafe_allow_html=True)
st.write('''Youtube Shorts/Videos Watcher is a program that gets your Video link or links
and starts watching them for a given amount of time ( we give the exact time of the video so that it will not watch
videos non-stop).\n
Or we give the Channel link and the program will automatically click on the last short uploaded,
watch it then move to next, until he views all shorts.
''')
st.write('---')
st.markdown("<h1 style='text-align: center; color: Red;'>Images</h1>", unsafe_allow_html=True)
img1, img2, img3 = st.columns(3)
with img1:
    st.image('images/1.PNG')
with img2:
    st.image('images/2.PNG')
with img3:
    st.image('images/3.PNG')
img4, img5, img6, img7 = st.columns(4)
with img4:
    st.image('images/4.PNG')
with img5:
    st.image('images/5.PNG')
with img6:
    st.image('images/6.PNG')
with img7:
    st.image('images/7.PNG')

st.write("---")
st.markdown("<h1 style='text-align: center; color: Red;'>What are you waiting for?</h1>", unsafe_allow_html=True)
st.header("CONTACT FOR MORE INFO!")
cf = """
<form action="https://formsubmit.co/n0nyf0xy@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name here" required>
     <input type="email" name="email" placeholder="Your e-mail here" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(cf, unsafe_allow_html=True)
with right_column:
    st.empty()
