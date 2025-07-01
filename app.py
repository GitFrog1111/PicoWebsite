import streamlit as st
from streamlit_extras.star_rating import star_rating
from streamlit_extras.stylable_container import stylable_container
import time

App_Link = "https://picopedro.streamlit.app/"

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Pico Pedro",
    page_icon="static/Images/PicoLogo.png",
    layout = 'wide'
    
)

# force itim font
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Itim&display=swap');
body {
    font-family: 'Itim', sans-serif;
}     
</style>
""", unsafe_allow_html=True)


if 'RandomMessage' not in st.session_state:
    st.session_state.RandomMessage = 0

Base_url = "http://localhost:8501"

def FakeStream(text):
    for char in text:
        if char == 'K':
            time.sleep(3)
        yield char
        time.sleep(0.02)



# --- HERO SECTION ---
with st.container():
    cols = st.columns([1, 6, 1, 5, 1])
    with cols[1]:
        st.container(border = False, height = 85)
        st.logo("static/Images/PicoLogo.png")
        star_rating(5, color = "#FFD700")
        st.markdown("<h1 style='text-align: left; font-size: 48px; font-weight: 600;margin-top: -50px;'>The #1 Way to Learn a Language is Through Play</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400;'>What all the other apps dont tell you: your streak, your boosts and all those levels won't make you fluent.</p>", unsafe_allow_html=True)
        st.link_button("Enter World", url=App_Link, type = 'primary')

    with cols[3]:
        st.markdown(f"<img src='{Base_url}/app/static/Images/Farm.png' style='margin-top: 0px;'>", unsafe_allow_html=True)
        chatcols = st.columns([1, 1.8, 1])
        with chatcols[1]:
            cssstyles = """
                {
                    border: none;
                    border-radius: 20px;
                    background-color: #E7E7E7;
                    height: 45px;
                    padding: 10px;
                    margin-left: 0px;
                    margin-top: -15px;
                    border: 1px solid rgb(211, 211, 211);
                    border-radius: 5555px;
                    
                }
            """
            text = ['Open door', 'Locate the traitor', 'Go upstairs', 'Talk to manager', 'Demand refund', 'Go to bar', 'Go to the bathroom', 'Start fight', 'Get in car', 'Drive to border', 'Drop off goods', 'Stake out the warehouse', 'Run from police', 'Go to the bar', 'Buy Drink', 'Call safehouse', 'Switch license plates', 'Disable tracker', 'Erase footprints', 'Signal backup', 'Slip through crowd', 'Board ferry', 'Hide in cargo hold', 'Monitor radio traffic', 'Change clothes', 'Forge passport', 'Bribe official', 'Sneak past checkpoint', 'Retrieve dossier', 'Decode message', 'Plant bug', 'Tap phone line', 'Intercept courier', 'Follow target', 'Tail limousine', 'Hack security camera', 'Loop footage', 'Park down alley', 'Enter through skylight', 'Quiet the guard', 'Crack safe', 'Photograph files', 'Upload to cloud', 'Evade patrol', 'Scale back wall', 'Drop rope', 'Climb to roof', 'Jump across gap', 'Deploy parachute', 'Signal extraction', 'Meet contact', 'Exchange intel', 'Count bills', 'Stash loot', 'Burn evidence', 'Change vehicle', 'Cross desert', 'Ditch convoy', 'Reach oasis', 'Lay low', 'Boil water', 'Patch wounds', 'Memorize coordinates', 'Chart new route', 'Avoid highway', 'Use backroads', 'Buy snacks', 'Refill water bottle', 'Consult map', 'Mark safe zones', 'Test comms', 'Encrypt message', 'Reboot transceiver', 'Await instructions', 'Spot helicopter', 'Race to helipad', 'Disable rotor lock', 'Board chopper', 'Lift off', 'Fly under radar', 'Drop satellite beacon', 'Contact home base', 'Receive mission update', 'Smile wryly', 'Prepare for next move.']
            chatempty = st.empty()
          
        with chatcols[2]:
            #send button
            with stylable_container(
                key="Chatbox2",
                css_styles="""
                button {
                    border: none;
                    border-radius: 20px;
                    background-color:rgb(194, 194, 194);
                    height: 45px;
                    padding: 12px;
                    margin-left: 0px;
                    margin-top: -20px;
                    border: 0px solid rgb(211, 211, 211);
                    border-radius: 5555px;
                    color: rgb(255, 255, 255);

                }"""):
                if st.button("", icon = ':material/arrow_upward:', key="sendmessage", type = 'primary'):
                    st.session_state.RandomMessage += 1
                    if st.session_state.RandomMessage == len(text):
                        st.session_state.RandomMessage = 0
        
                
                with chatempty:
                    with stylable_container(
                        key="Chatbox1",
                        css_styles=cssstyles):
                        st.write(FakeStream(text[st.session_state.RandomMessage]))  
                

        
st.container(border = False, height = 32)
# --- GET FLUENT, FAST ---
with st.container():
    st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>Get Fluent, Fast</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 16px; font-weight: 400; margin-top: -10px;'>Studying sucks, the apps all suck, but this feels like magic.</p>", unsafe_allow_html=True)
    st.container(border = False, height = 32)


# --- FIND YOUR ADVENTURE ---
    cols = st.columns([1, 10, 1])
    with cols[1]:
        with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: none;
                border-radius: 20px;
                background-color: #FFFFFF;
                height: 500px;
                z-index: 1000;
            }
            """,):
        

        
        
            with st.container():
                content_cols = st.columns([1, 6, 6, 1])
                with content_cols[1]:
                    st.container(border = False, height = 32)
                    st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Find your adventure</h1>", unsafe_allow_html=True)
                    st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Set sail for a pirates paradise, or start a rebellion in a corporate cyberpunk world. Every word you learn is another tool to carve your own story.</p>", unsafe_allow_html=True)
                
                imagesizer = st.columns([1, 1])
                with imagesizer[1]:
                    #set z-index to 1000
                    st.markdown(f"<img src='{Base_url}/app/static/Images/Boatyard.png' style='margin-top: -250px; margin-left: 50px;'>", unsafe_allow_html=True)


st.container(border = False, height = 32)

cssstyles = """
            {
                border: none;
                border-radius: 20px;
                background-color: #FFFFFF;
                height: 700px;
                padding: 80px;
                margin-top: -50px;
            }
            """


# --- POCKET TUTOR & INFINITE CHARACTERS ---

_, col1, col2, __ = st.columns([1, 5, 5, 1])
with col1:
        with stylable_container(
        key="container_with_border2",
        css_styles=cssstyles):
            with st.container():
                
                st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Pocket Tutor</h1>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Your on-the-go personal tutor offers advice and key words to makelearning a language feel like magic.</p>", unsafe_allow_html=True)
                content_cols = st.columns([1,10, 1])
                with content_cols[1]:
                    st.container(border = False, height = 45)
                    st.markdown(f"<img src='{Base_url}/app/static/Images/PocketTutor.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        
with col2:
    with stylable_container(
        key="container_with_border3",
        css_styles=cssstyles):
            with st.container():

                st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Infinite Characters</h1>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Negotiate hostage transfers with the chieftain of the northern tribes, or  just order a coffee. Level up your language skills without realising.</p>", unsafe_allow_html=True)
                st.container(border = False, height = 35)
                st.image("static/Images/Characters.png")




# --- WE MAKE SPEAKERS ---
with st.container():
    st.container(border = False, height = 100)
    st.markdown(f"<img src='{Base_url}/app/static/Images/Lorals.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    cols = st.columns([1, 1.3, 1])
    
    with cols[1]:
        
        st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600; margin-top: -160px;'>We Make Speakers</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 16px; font-weight: 400; margin-top: -110px;'>The grammar, the verbs, the tenses are great late game, but all get in the way of step one, to understand and to be understood.</p>", unsafe_allow_html=True)
    
# --- FEATURES ---
st.container(border = False, height = 32)

cssstyles = """
            {
                border: none;
                border-radius: 20px;
                background-color: #FFFFFF;
                height: 300px;
                padding: 30px;
            }
            """
col1, col2, col3, col4 = st.columns(4)

upperpad = 50
lowerpad = 1

with col1:
    
    with stylable_container(
        key="container_with_border4",
        css_styles=cssstyles):
        st.container(border = False, height = upperpad)
        st.markdown(f"<img src='{Base_url}/app/static/Images/FromStartToFluent.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
        st.container(border = False, height = lowerpad)
        
        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>From start to fluent</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Take your experience to match you where you are. Pico Pedro dynamically adjusts to all skill levels.</p>", unsafe_allow_html=True)
with col2:
    with stylable_container(
        key="container_with_border5",
        css_styles=cssstyles):
        st.container(border = False, height = upperpad)
        st.markdown(f"<img src='{Base_url}/app/static/Images/Missions.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
        st.container(border = False, height = lowerpad)
        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Missions</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Get your own mission or ask around! Characters will throw you into memorable encounters right from the start.</p>", unsafe_allow_html=True)
with col3:
    with stylable_container(
        key="container_with_border6",
        css_styles=cssstyles):
        st.container(border = False, height = upperpad)
        st.markdown(f"<img src='{Base_url}/app/static/Images/EndlessEncounters.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
        st.container(border = False, height = lowerpad)
        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Endless encounters</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Whether you're starting a cult or a new job, everything is generated just for you.</p>", unsafe_allow_html=True)
with col4:
    with stylable_container(
        key="container_with_border7",
        css_styles=cssstyles):
        st.container(border = False, height = upperpad)
        st.markdown(f"<img src='{Base_url}/app/static/Images/Leaderboard.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
        st.container(border = False, height = lowerpad)
        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Leaderboard</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Compete on a global leaderboard for in-game rewards!</p>", unsafe_allow_html=True)

# --- TESTIMONIALS ---

# st.container(border = False, height = 32)

# Testemonials = [
#     {
#         "image": "static/Images/Peachhee.png",
#         "name": "Peachhee",
#         "country": "🇺🇸",
#         "testimonial": "Absolute game changer 🙌"
#     },
#     {
#         "image": "static/Images/Jennifer.png",
#         "name": "Jennifer W",
#         "country": "🇬🇧",
#         "testimonial": "Never thought i'd get back into learning spanish, but this has been amazing fun!"
#     },
#     {
#         "image": "static/Images/Davixx.png",
#         "name": "Davixx",
#         "country": "🇫🇷",
#         "testimonial": "I cannot believe this isnt how it's taught in schools. I went from knowing 0 german to being able to hold a real conversation in under 2 weeks!"
#     }
# ]


# cssstyles = """
#             {
#                 border: none;
#                 border-radius: 20px;
#                 background-color: #E7E7E7;
#                 height: 400px;
#                 padding: 30px;
#             }
#             """
# testemonialcols = st.columns([1, 1, 1])

# for count, testimonial in enumerate(Testemonials):
#     with testemonialcols[count]:
#             with stylable_container(
#         key=f"container_with_border{count}{testimonial['name']}",
#         css_styles=cssstyles):
#                 st.container(border = False, height = 32)
#                 with st.container(border = False, height = 300):
#                     st.markdown(f"<p style='text-align: left; font-size: 20px; font-weight: 400; margin-top: 0px;'>{testimonial['testimonial']}</p>", unsafe_allow_html=True)
                
#                 st.divider()


#                 st.markdown(f"<p style='text-align: left; font-size: 24px; font-weight: 400; margin-top: -10px;'>{testimonial['name']}</p>", unsafe_allow_html=True)
#                 st.markdown(f"<p style='text-align: left; font-size: 12px; font-weight: 400; margin-top: -10px;'>{testimonial['country']}</p>", unsafe_allow_html=True)


# --- FAQ ---
st.container(border = False, height = 64)
with st.container():
    st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>FAQ</h1>", unsafe_allow_html=True)
    faqcols = st.columns([1, 3.32, 1])
    with faqcols[1]:
        with st.expander("What is Pico Pedro?"):
            st.write("Learning a language is traditionally extremely hard, and takes months of concious effort to get up and running. PicoPedro flips this on its head by incentivsing you to learn as a byproduct of a great time. Staring at a textbook is not memorable experience at all, but sailing across the atlantic is. We've set up PicoPedro to make you learn like a baby, no grammar, no tenses, no conjugations, Your brain unconciously maps sounds to experiences!")
        with st.expander("How does it work?"):
            st.write("PicoPedro is a browser game, (app coming soon!). The game is a true sandbox, You can set your own missions and adventures, or let the game lead the way. The game is free to play, however it is limited use per day. You can upgrade to a paid subscription to unlock unlimited playtime.")
        with st.expander("How do I get started?"):
            st.write("Click the button, sign in, and start playing!")
            st.link_button("Enter World", key="FAQ_enter", type = 'primary')
        

# --- BETA NOW LIVE ---
st.container(border = False, height = 32)
cssstyles = """
            {
                border: none;
                background-image: url('http://localhost:8501/app/static/Images/Purp.png');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                border-radius: 20px;
                
                height: 400px;
                padding: 30px;
            }
            """
cols = st.columns([1, 10, 1])
with cols[1]:
    with stylable_container(
        key="container_with_border8",
        css_styles=cssstyles):
        with st.container():
            contentcols = st.columns([3, 5, 12, 1])
            with contentcols[1]:
                st.container(border = False, height = 96)
                st.markdown("<h1 style='text-align: left; font-size: 32px; font-weight: 600;'>Beta Now Live!</h1>", unsafe_allow_html=True)
                st.link_button("Enter World", url=App_Link, type = 'primary')

            with contentcols[2]:
                st.markdown(f"<img src='{Base_url}/app/static/Images/BetaGardens.png' style='margin-top: -120px; margin-left: 90px;'>", unsafe_allow_html=True)
