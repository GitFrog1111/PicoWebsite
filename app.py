import streamlit as st
from streamlit_extras.star_rating import star_rating
from streamlit_extras.stylable_container import stylable_container
import time

from streamlit_javascript import st_javascript
from user_agents import parse

App_Link = "https://picopedro.streamlit.app/"

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Pico Pedro",
    page_icon="static/Images/Logos/Badge_Tiny.png",
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
Base_url = "https://joinpicopedro.streamlit.app"

def FakeStream(text):
    for char in text:
        if char == 'K':
            time.sleep(3)
        yield char
        time.sleep(0.02)


# def RenderDesktop():
    
#     # --- HERO SECTION ---
#     with st.container():
#         cols = st.columns([1, 6, 1, 5, 1])
#         with cols[1]:
#             st.container(border = False, height = 85)
#             st.logo("static/Images/PicoLogo.png")
#             star_rating(5, color = "#FFD700")
#             st.markdown("<h1 style='text-align: left; font-size: 48px; font-weight: 600;margin-top: -50px;'>The #1 Way to Learn a Language is Through Play</h1>", unsafe_allow_html=True)
#             st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400;'>What all the other apps dont tell you: your streak, your boosts and all those levels won't make you fluent.</p>", unsafe_allow_html=True)
#             st.link_button("Enter World", url=App_Link, type = 'primary')

#         with cols[3]:
#             st.markdown(f"<img src='app/static/Images/Farm.png' style='margin-top: 0px; float: right;'>", unsafe_allow_html=True)
#             chatcols = st.columns([1, 1.8, 1])
#             with chatcols[1]:
#                 cssstyles = """
#                     {
#                         border: none;
#                         border-radius: 20px;
#                         background-color: #E7E7E7;
#                         height: 45px;
#                         padding: 10px;
#                         margin-left: 0px;
#                         margin-top: -15px;
#                         border: 1px solid rgb(211, 211, 211);
#                         border-radius: 5555px;
                        
#                     }
#                 """
#                 text = ['Open door', 'Locate the traitor', 'Go upstairs', 'Talk to manager', 'Demand refund', 'Go to bar', 'Go to the bathroom', 'Start fight', 'Get in car', 'Drive to border', 'Drop off goods', 'Stake out the warehouse', 'Run from police', 'Go to the bar', 'Buy Drink', 'Call safehouse', 'Switch license plates', 'Disable tracker', 'Erase footprints', 'Signal backup', 'Slip through crowd', 'Board ferry', 'Hide in cargo hold', 'Monitor radio traffic', 'Change clothes', 'Forge passport', 'Bribe official', 'Sneak past checkpoint', 'Retrieve dossier', 'Decode message', 'Plant bug', 'Tap phone line', 'Intercept courier', 'Follow target', 'Tail limousine', 'Hack security camera', 'Loop footage', 'Park down alley', 'Enter through skylight', 'Quiet the guard', 'Crack safe', 'Photograph files', 'Upload to cloud', 'Evade patrol', 'Scale back wall', 'Drop rope', 'Climb to roof', 'Jump across gap', 'Deploy parachute', 'Signal extraction', 'Meet contact', 'Exchange intel', 'Count bills', 'Stash loot', 'Burn evidence', 'Change vehicle', 'Cross desert', 'Ditch convoy', 'Reach oasis', 'Lay low', 'Boil water', 'Patch wounds', 'Memorize coordinates', 'Chart new route', 'Avoid highway', 'Use backroads', 'Buy snacks', 'Refill water bottle', 'Consult map', 'Mark safe zones', 'Test comms', 'Encrypt message', 'Reboot transceiver', 'Await instructions', 'Spot helicopter', 'Race to helipad', 'Disable rotor lock', 'Board chopper', 'Lift off', 'Fly under radar', 'Drop satellite beacon', 'Contact home base', 'Receive mission update', 'Smile wryly', 'Prepare for next move.']
#                 chatempty = st.empty()
            
#             with chatcols[2]:
#                 #send button
#                 with stylable_container(
#                     key="Chatbox2",
#                     css_styles="""
#                     button {
#                         border: none;
#                         border-radius: 20px;
#                         background-color:rgb(194, 194, 194);
#                         height: 45px;
#                         padding: 12px;
#                         margin-left: 0px;
#                         margin-top: -20px;
#                         border: 0px solid rgb(211, 211, 211);
#                         border-radius: 5555px;
#                         color: rgb(255, 255, 255);

#                     }"""):
#                     if st.button("", icon = ':material/arrow_upward:', key="sendmessage", type = 'primary'):
#                         st.session_state.RandomMessage += 1
#                         if st.session_state.RandomMessage == len(text):
#                             st.session_state.RandomMessage = 0
            
                    
#                     with chatempty:
#                         with stylable_container(
#                             key="Chatbox1",
#                             css_styles=cssstyles):
#                             st.write(FakeStream(text[st.session_state.RandomMessage]))  
                    

            
#     st.container(border = False, height = 32)
#     # --- GET FLUENT, FAST ---
#     with st.container():
#         st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>Get Fluent, Fast</h1>", unsafe_allow_html=True)
#         st.markdown("<p style='text-align: center; font-size: 16px; font-weight: 400; margin-top: -10px;'>Studying sucks, the apps all suck, but this feels like magic.</p>", unsafe_allow_html=True)
#         st.container(border = False, height = 32)


#     # --- FIND YOUR ADVENTURE ---
#         cols = st.columns([1, 10, 1])
#         with cols[1]:
#             with stylable_container(
#             key="container_with_border",
#             css_styles="""
#                 {
#                     border: none;
#                     border-radius: 20px;
#                     background-color: #FFFFFF;
#                     height: 500px;
#                     z-index: 1000;
#                 }
#                 """,):
            
            
#                 with st.container():
#                     content_cols = st.columns([1, 6, 6, 1])
#                     with content_cols[1]:
#                         st.container(border = False, height = 32)
#                         st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Find your adventure</h1>", unsafe_allow_html=True)
#                         st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Set sail for a pirates paradise, or start a rebellion in a corporate cyberpunk world. Every word you learn is another tool to carve your own story.</p>", unsafe_allow_html=True)
                    
#                     imagesizer = st.columns([1.2, 1])
#                     with imagesizer[1]:
#                         #set z-index to 1000
#                         st.markdown(f"<img src='app/static/Images/Boatyard.png' style='margin-top: -250px; float: right; margin-right: 10%;'>", unsafe_allow_html=True)


#     st.container(border = False, height = 32)

#     cssstyles = """
#                 {
#                     border: none;
#                     border-radius: 20px;
#                     background-color: #FFFFFF;
#                     height: 700px;
#                     padding: 80px;
#                     margin-top: -50px;
#                 }
#                 """


#     # --- POCKET TUTOR & INFINITE CHARACTERS ---

#     _, col1, col2, __ = st.columns([1, 5, 5, 1])
#     with col1:
#             with stylable_container(
#             key="container_with_border2",
#             css_styles=cssstyles):
#                 with st.container():
                    
#                     st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Pocket Tutor</h1>", unsafe_allow_html=True)
#                     st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Your on-the-go personal tutor offers advice and key words to makelearning a language feel like magic.</p>", unsafe_allow_html=True)
#                     content_cols = st.columns([1,10, 1])
#                     with content_cols[1]:
#                         st.container(border = False, height = 45)
#                         st.markdown(f"<img src='app/static/Images/PocketTutor.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
            
#     with col2:
#         with stylable_container(
#             key="container_with_border3",
#             css_styles=cssstyles):
#                 with st.container():

#                     st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Infinite Characters</h1>", unsafe_allow_html=True)
#                     st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Negotiate hostage transfers with the chieftain of the northern tribes, or  just order a coffee. Level up your language skills without realising.</p>", unsafe_allow_html=True)
#                     st.container(border = False, height = 35)
#                     st.markdown(f"<img src='app/static/Images/Characters.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)




#     # --- WE MAKE SPEAKERS ---
#     with st.container():
#         st.container(border = False, height = 100)
#         st.markdown(f"<img src='app/static/Images/Lorals.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
#         cols = st.columns([1, 1.3, 1])
        
#         with cols[1]:
            
#             st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600; margin-top: -160px;'>We Make Speakers</h1>", unsafe_allow_html=True)
#             st.markdown("<p style='text-align: center; font-size: 16px; font-weight: 400; margin-top: -110px;'>The grammar, the verbs, the tenses are great late game, but all get in the way of step one, to understand and to be understood.</p>", unsafe_allow_html=True)
        
#     # --- FEATURES ---
#     st.container(border = False, height = 32)

#     cssstyles = """
#                 {
#                     border: none;
#                     border-radius: 20px;
#                     background-color: #FFFFFF;
#                     height: 300px;
#                     padding: 30px;
#                 }
#                 """
#     col1, col2, col3, col4 = st.columns(4)

#     upperpad = 50
#     lowerpad = 1

#     with col1:
        
#         with stylable_container(
#             key="container_with_border4",
#             css_styles=cssstyles):
#             st.container(border = False, height = upperpad)
#             st.markdown(f"<img src='app/static/Images/FromStartToFluent.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
#             st.container(border = False, height = lowerpad)
            
#             st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>From start to fluent</h1>", unsafe_allow_html=True)
#             st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Take your experience to match you where you are. Pico Pedro dynamically adjusts to all skill levels.</p>", unsafe_allow_html=True)
#     with col2:
#         with stylable_container(
#             key="container_with_border5",
#             css_styles=cssstyles):
#             st.container(border = False, height = upperpad)
#             st.markdown(f"<img src='app/static/Images/Missions.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
#             st.container(border = False, height = lowerpad)
#             st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Missions</h1>", unsafe_allow_html=True)
#             st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Get your own mission or ask around! Characters will throw you into memorable encounters right from the start.</p>", unsafe_allow_html=True)
#     with col3:
#         with stylable_container(
#             key="container_with_border6",
#             css_styles=cssstyles):
#             st.container(border = False, height = upperpad)
#             st.markdown(f"<img src='app/static/Images/EndlessEncounters.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
#             st.container(border = False, height = lowerpad)
#             st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Endless encounters</h1>", unsafe_allow_html=True)
#             st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Whether you're starting a cult or a new job, everything is generated just for you.</p>", unsafe_allow_html=True)
#     with col4:
#         with stylable_container(
#             key="container_with_border7",
#             css_styles=cssstyles):
#             st.container(border = False, height = upperpad)
#             st.markdown(f"<img src='app/static/Images/Leaderboard.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
#             st.container(border = False, height = lowerpad)
#             st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Leaderboard</h1>", unsafe_allow_html=True)
#             st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Compete on a global leaderboard for in-game rewards!</p>", unsafe_allow_html=True)

#     # --- TESTIMONIALS ---

#     # st.container(border = False, height = 32)

#     # Testemonials = [
#     #     {
#     #         "image": "static/Images/Peachhee.png",
#     #         "name": "Peachhee",
#     #         "country": "🇺🇸",
#     #         "testimonial": "Absolute game changer 🙌"
#     #     },
#     #     {
#     #         "image": "static/Images/Jennifer.png",
#     #         "name": "Jennifer W",
#     #         "country": "🇬🇧",
#     #         "testimonial": "Never thought i'd get back into learning spanish, but this has been amazing fun!"
#     #     },
#     #     {
#     #         "image": "static/Images/Davixx.png",
#     #         "name": "Davixx",
#     #         "country": "🇫🇷",
#     #         "testimonial": "I cannot believe this isnt how it's taught in schools. I went from knowing 0 german to being able to hold a real conversation in under 2 weeks!"
#     #     }
#     # ]


#     # cssstyles = """
#     #             {
#     #                 border: none;
#     #                 border-radius: 20px;
#     #                 background-color: #E7E7E7;
#     #                 height: 400px;
#     #                 padding: 30px;
#     #             }
#     #             """
#     # testemonialcols = st.columns([1, 1, 1])

#     # for count, testimonial in enumerate(Testemonials):
#     #     with testemonialcols[count]:
#     #             with stylable_container(
#     #         key=f"container_with_border{count}{testimonial['name']}",
#     #         css_styles=cssstyles):
#     #                 st.container(border = False, height = 32)
#     #                 with st.container(border = False, height = 300):
#     #                     st.markdown(f"<p style='text-align: left; font-size: 20px; font-weight: 400; margin-top: 0px;'>{testimonial['testimonial']}</p>", unsafe_allow_html=True)
                    
#     #                 st.divider()


#     #                 st.markdown(f"<p style='text-align: left; font-size: 24px; font-weight: 400; margin-top: -10px;'>{testimonial['name']}</p>", unsafe_allow_html=True)
#     #                 st.markdown(f"<p style='text-align: left; font-size: 12px; font-weight: 400; margin-top: -10px;'>{testimonial['country']}</p>", unsafe_allow_html=True)


#     # --- FAQ ---
#     st.container(border = False, height = 64)
#     with st.container():
#         st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>FAQ</h1>", unsafe_allow_html=True)
#         faqcols = st.columns([1, 3.32, 1])
#         with faqcols[1]:
#             with st.expander("What is Pico Pedro?"):
#                 st.write("Learning a language is traditionally extremely hard, and takes months of concious effort to get up and running. PicoPedro flips this on its head by incentivsing you to learn as a byproduct of a great time. Staring at a textbook is not memorable experience at all, but sailing across the atlantic is. We've set up PicoPedro to make you learn like a baby, no grammar, no tenses, no conjugations, Your brain unconciously maps sounds to experiences!")
#             with st.expander("How does it work?"):
#                 st.write("PicoPedro is a browser game, (app coming soon!). The game is a true sandbox, You can set your own missions and adventures, or let the game lead the way. The game is free to play, however it is limited use per day. You can upgrade to a paid subscription to unlock unlimited playtime.")
#             with st.expander("How do I get started?"):
#                 st.write("Click the button, sign in, and start playing!")
#                 st.link_button("Enter World",url=App_Link, type = 'primary')
            

#     # --- BETA NOW LIVE ---
#     st.container(border = False, height = 64)
#     cssstyles = """
#                 {
#                     border: none;
#                     background-image: url('app/static/Images/Purp2.png');
#                     background-size: cover;
#                     background-position: center;
#                     background-repeat: no-repeat;
#                     border-radius: 20px;
                    
#                     height: 400px;
#                     padding: 30px;
#                 }
#                 """

#     cols = st.columns([1, 10, 1])
#     with cols[1]:
#         with stylable_container(
#             key="container_with_border8",
#             css_styles=cssstyles):
#             with st.container():
#                 contentcols = st.columns([3, 5, 12, 1])
#                 with contentcols[1]:
#                     st.container(border = False, height = 96)
#                     st.markdown("<h1 style='text-align: left; font-size: 32px; font-weight: 600;'>Beta Now Live!</h1>", unsafe_allow_html=True)
#                     st.link_button("Enter World", url=App_Link, type = 'primary')

#                 with contentcols[2]:

#                     st.markdown(f"<img src='app/static/Images/BetaGardens.png' style='margin-top: -120px; float: right;'>", unsafe_allow_html=True)



def RenderMobile():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # --- HERO SECTION ---
    
    
    # Header
    #st.logo("static/Images/Logos/Logo_Med.png")

    st.markdown("<img src='app/static/Images/Logos/Logo_Med.png' style='margin-top: -200px; width: 100px;'>", unsafe_allow_html=True) 

    with stylable_container(
        key="menu_button",
        css_styles="""
        button {
            border: none;
            border-radius: 20px;
            background-color: transparent;
            margin-left: 100px;
            margin-top: -130px;
            float: right;
            
        }
        """):
        with st.popover(" ", icon = ":material/menu:"):
            with st.container(border = False, height = 1):
                st.container(border = False, height = 50)

                st.image("static/Images/White.png", width = 1000)
            
            with stylable_container(
                key="link_buttons",
                css_styles="""
                a {
                    border: none;
                    border-radius: 20px;
                    text-align: right;
                    float: right;
                                        
                }
                """):

                st.link_button("Home", 'https://www.picopedro.com', type="tertiary")
                st.container(border=False, height=1)
                st.link_button("Start Game", url=App_Link, type="tertiary")
                st.link_button("PachoNotes", 'https://www.picopedro.com', type="tertiary")
                st.link_button("Leaderboard", 'https://www.picopedro.com', type="tertiary")
            
        
        
    
    st.container(border=False, height=50)

    # Title
    st.markdown("<h1 style='text-align: center; font-size: 48px; font-weight: 600; line-height: 1.1'>The #1 way to learn a language is</h1>", unsafe_allow_html=True)

    
    st.markdown("<img src='app/static/Images/GreenPlay.png' style='margin-top: 0px;'>", unsafe_allow_html=True)
    
    # Start Game Button
    with stylable_container(
        key="start_game_button",
        css_styles="""
        button {
            
            background-image: url('app/static/Images/StartGameGradient.png');
            background-size: cover;
            border-radius: 100px;
            border: none;
            text-align: center;
            font-size: 48px;
            padding-top: 10px;
            padding-bottom: 10px;
            margin-left: 25%;
            width: 50%;
            height: 70px;
            box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
            border: 1px solid rgb(211, 211, 211);
            float: inherit;
            color: #FFFFFF;
            
            
            
        }
        button:hover {
            background-image: None;
            background-color: #FFFFFF;
            box-shadow: 0px 0px 6px rgba(157, 78, 221, 0.2);
            text-color: #000000;
        """
    ):
        st.button("Play Now", type = "tertiary", use_container_width=True)

    st.container(border=False, height=30)

    # Farm Image
    st.markdown("<img src='app/static/Images/Farm.png' style='margin-top: 0px; display: flex; justify-content: center;'>", unsafe_allow_html=True)

    # Input Field

    cssstyles = """
            {
                border: none;
                border-radius: 20px;
                background-color: #EAE7E7;
                height: 45px;
                padding: 10px;
                margin-left: 0px;
                margin-top: -15px;
                border: 5px solid rgb(211, 211, 211);
                border-radius: 5555px;
            }
        """
    text = ['Open door', 'Locate the traitor', 'Go upstairs', 'Talk to manager', 'Demand refund', 'Go to bar', 'Go to the bathroom', 'Start fight', 'Get in car', 'Drive to border', 'Drop off goods', 'Stake out the warehouse', 'Run from police', 'Go to the bar', 'Buy Drink', 'Call safehouse', 'Switch license plates', 'Disable tracker', 'Erase footprints', 'Signal backup', 'Slip through crowd', 'Board ferry', 'Hide in cargo hold', 'Monitor radio traffic', 'Change clothes', 'Forge passport', 'Bribe official', 'Sneak past checkpoint', 'Retrieve dossier', 'Decode message', 'Plant bug', 'Tap phone line', 'Intercept courier', 'Follow target', 'Tail limousine', 'Hack security camera', 'Loop footage', 'Park down alley', 'Enter through skylight', 'Quiet the guard', 'Crack safe', 'Photograph files', 'Upload to cloud', 'Evade patrol', 'Scale back wall', 'Drop rope', 'Climb to roof', 'Jump across gap', 'Deploy parachute', 'Signal extraction', 'Meet contact', 'Exchange intel', 'Count bills', 'Stash loot', 'Burn evidence', 'Change vehicle', 'Cross desert', 'Ditch convoy', 'Reach oasis', 'Lay low', 'Boil water', 'Patch wounds', 'Memorize coordinates', 'Chart new route', 'Avoid highway', 'Use backroads', 'Buy snacks', 'Refill water bottle', 'Consult map', 'Mark safe zones', 'Test comms', 'Encrypt message', 'Reboot transceiver', 'Await instructions', 'Spot helicopter', 'Race to helipad', 'Disable rotor lock', 'Board chopper', 'Lift off', 'Fly under radar', 'Drop satellite beacon', 'Contact home base', 'Assess situation', 'Cheeky wink to camera', 'Prepare for next move.']
    
    chatempty = st.empty()
    def renderchat():
        cssstyles = """
            {
                border: 1px solid rgb(211, 211, 211);
                border-radius: 20px;
                background-color: #E7E7E7;
                height: 45px;
                width: 50%;
                padding-top: 10px;
                padding-left: 20px;
                margin-left: 100px;
                margin-top: -55px;
                border: 1px solid rgb(211, 211, 211);
            }
            """
        e = stylable_container(
            key="chat_message",
            css_styles=cssstyles)
        with e:
            #st.markdown(f"<p style='text-align: left; font-size: 16px; font-weight: 400; margin-left: 10px;'>{text[st.session_state.RandomMessage]}</p>", unsafe_allow_html=True)
            st.write(FakeStream(text[st.session_state.RandomMessage]))

        return e
    
    #send button
    with chatempty:
        renderchat()
        st.session_state.RandomMessage += 1
        if st.session_state.RandomMessage == len(text):
            st.session_state.RandomMessage = 0

    cssstyles = """
        button {
                border: none;
                border-radius: 20px;
                background-color: #E7E7E7;
                padding: 10px;
                margin-right: 50px;
                margin-top: -70px;
                border: 1px solid rgb(211, 211, 211);
                border-radius: 5555px;
                float: right;
            }
        """
    with stylable_container(
        key="chat_send",
        css_styles=cssstyles):
        st.button("", icon = ":material/keyboard_arrow_up:", key="chat_send", type="tertiary")

            
    st.container(border=False, height=50)
    # --- GET FLUENT, FAST ---
    # with st.container():
    #     st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>Get Fluent, Fast</h1>", unsafe_allow_html=True)
    #     st.markdown("<p style='text-align: center; font-size: 16px; font-weight: 400; margin-top: -10px;'>Studying sucks, the apps all suck, but this feels like magic.</p>", unsafe_allow_html=True)
    #     st.markdown("<img src='app/static/Images/BlueFast.png' style='margin-top: -130px;'>", unsafe_allow_html=True)
    #     st.container(border = False, height = 32)

    with st.container():
        #center the image
        st.markdown("<div style='display: flex; justify-content: center;'><img src='app/static/Images/GetFluentFast.png' style='margin-top: 0px; width: 100%; max-width: 900px;'></div>", unsafe_allow_html=True)



    # --- CARDS ---
    st.markdown("<img src='app/static/Images/Cards/StartYourAdventure.png' style='margin-top: 0px;'>", unsafe_allow_html=True)

    #st.container(border=False, height=20)
    
    st.markdown("<img src='app/static/Images/Cards/InfiniteCastofCharacters.png' style='margin-top: 0px;'>", unsafe_allow_html=True)

    #st.container(border=False, height=20)

    st.markdown("<img src='app/static/Images/Cards/ProfessorPacho.png' style='margin-top: 0px;'>", unsafe_allow_html=True)

    st.container(border=False, height=50)

    # --- WE MAKE SPEAKERS ---
    # with st.container():
    #     st.markdown("<img src='app/static/Images/PurpleSpeakers.png' style='margin-top: 0px; width :80%;float:right; padding-right: 100px;'>", unsafe_allow_html=True)
    #     st.markdown("<img src='app/static/Images/Lorals.png' style='margin-top: -100px;'>", unsafe_allow_html=True)
    #     st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600; margin-top: -120px;'>We Make Speakers</h1>", unsafe_allow_html=True)
    #     st.markdown("<p style='text-align: center; font-size: 16px; font-weight: 400;'>Focus on understanding and being understood.</p>", unsafe_allow_html=True)
    
    with st.container():
        
        st.markdown("<div style='display: flex; justify-content: center;'><img src='app/static/Images/SpeakersMadeHere.png' style='margin-top: 0px; width: 100%; max-width: 900px;'></div>", unsafe_allow_html=True)

    st.container(border=False, height=30)
    
    # --- FEATURES ---
    features = [
        {"icon": "static/Images/Icons/StartToFluent.png", "title": "From start to fluent", "text": "Take your experience to match you where you are. Pico Pedro dynamically adjusts to all skill levels."},
        {"icon": "static/Images/Icons/Missions.png", "title": "Missions", "text": "Get your own mission or ask around! Characters will throw you into memorable encounters right from the start."},
        {"icon": "static/Images/Icons/EndlessEncounters.png", "title": "Endless encounters", "text": "Whether you're starting a cult or a new job, everything is generated just for you."},
        {"icon": "static/Images/Icons/Leaderboard.png", "title": "Leaderboard", "text": "Compete on a global leaderboard for in-game rewards!"}]

    for feature in features:
        with st.container():
            cols = st.columns([1, 4])
            with cols[0]:
                st.image(feature["icon"], width=64)
            with cols[1]:
                st.markdown(f"<h4>{feature['title']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p>{feature['text']}</p>", unsafe_allow_html=True)
        st.container(border=False, height=20)


    # --- FAQ ---
    st.container(border=False, height=64)
    with st.container():
        st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>FAQ</h1>", unsafe_allow_html=True)
        with st.expander("What is Pico Pedro?"):
            st.text("""PicoPacho is a language learning game, in an infinite AI-generated world.  Learning a language is extremely hard, and can take months of effort just to get up and running. Staring at a textbook is not memorable experience at all, but sailing across the Atlantic would be!\n\nBabies (and adults) remember experiences, not conjugations, so we've set up PicoPacho to put you in memorable experiences right from the start!""")
        with st.expander("How does it work?"):
            st.text("PicoPacho is a browser game, (app coming soon!). Talk to characters in your target language, visit new locations, collect items, and set your own missions. The game is a true sandbox, You can direct the game to specific situations you want to practice, or let the game lead the way.\n\nPicoPacho is free to play for ~25 moves per day. If you are finding it works for you, you can upgrade to a paid subscription to unlock unlimited playtime.")
        
        with st.expander("What languages are supported?"):
            st.write("Currently, PicoPacho supports English, French and German. We are working on adding more languages soon!")

        with st.expander("Where can I play?"):
            st.write("Currently, PicoPacho is only available on desktop. Try for free by clicking the button below to start playing!")
            #st.markdown("<p style='text-align: center; font-size: 16px; font-weight: 400;'>Click the button below and start playing!</p>", unsafe_allow_html=True)
            st.link_button("Start Game", url=App_Link, type='secondary')
            
    # --- PLAY FOR FREE ---
    st.container(border=False, height=64)
    
    st.markdown("<img src='app/static/Images/PlayForFree.png' style='margin-top: 0px;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600; margin-top: -100px;'>Play For Free</h1>", unsafe_allow_html=True)
    
    with stylable_container(
        key="play_for_free_start_button",
        css_styles="""
        a {
            background-color: #FFFFFF;
            border-radius: 5555px;
            text-align: center;
            padding-top: 10px;
            padding-bottom: 10px;
            margin-left: 35%;
            width: 30%;
            box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
            border: 0px;
            float: inherit;
        }
        button:hover {
            box-shadow: 0px 0px 6px rgba(157, 78, 221, 0.2);
        }
        """
    ):
        st.link_button("Start Game", url=App_Link, type="secondary")
    

    # --- FOOTER ---
    st.container(border=False, height=30)
    st.markdown("<img src='app/static/Images/WindmillFooter.png' style='margin-top: 0px; width :500px;'>", unsafe_allow_html=True)
    st.container(border=False, height=10)

    with stylable_container(
        key="whitebox",
        css_styles="""
        div {
            background-color: #FFFFFF;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px -5px 10px 0px rgba(0, 0, 0, 0.1);
        }
        """):


        st.container(border=False, height=180)
        st.markdown("<img src='app/static/Images/Logos/Logo_Blackout_Med.png' style='margin-top: 0px; width: 200px;'>", unsafe_allow_html=True)
        st.container(border=False, height=20)

        st.markdown("<p style='text-align: left; color: #A4A9BA; font-size: 12px; font-weight: 400; padding-left: 20px;'>S i t e</p>", unsafe_allow_html=True)
        
        cssstyles = """
            a {
                border: none;
                background-color: transparent;
                font-size: 16px;
                font-weight: 400;
                padding-left: 20px;
                padding-right: 20px;
                
            }
            """
        with stylable_container(
            key="footer_links",
            css_styles=cssstyles):
            st.link_button("Home", 'https://www.picopedro.com', type="tertiary")
            st.link_button("Start Game", url=App_Link, type="tertiary")
            st.link_button("PachoNotes", 'https://www.picopedro.com', type="tertiary")
            st.link_button("Leaderboard", 'https://www.picopedro.com', type="tertiary")
            st.link_button("Invite to Earn", 'https://www.picopedro.com', type="tertiary")
            st.link_button("Give Feedback", 'https://www.picopedro.com', type="tertiary")
        
        st.container(border=False, height=20)

        st.markdown("<p style='text-align: left; color: #A4A9BA; font-size: 12px; font-weight: 400; padding-left: 20px;'>C o m m u n i t y</p>", unsafe_allow_html=True)

        with stylable_container(
            key="footer_community_links",
            css_styles=cssstyles):
            st.link_button("Discord", 'https://www.picopedro.com', type="tertiary")
            st.link_button("Youtube", 'https://www.picopedro.com', type="tertiary")
            st.link_button("Twitter/X", 'https://www.picopedro.com', type="tertiary")

        
        
    

# ua_string = str(st_javascript("""window.navigator.userAgent;"""))
# user_agent = (parse(ua_string))
# st.session_state.is_session_pc = bool(user_agent.is_pc)
# time.sleep(1)
# if st.session_state.is_session_pc:
#     RenderDesktop()
# else:
#     RenderMobile()

RenderMobile()

