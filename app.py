import streamlit as st
from streamlit_extras.star_rating import star_rating
from streamlit_extras.stylable_container import stylable_container
import time

from streamlit_javascript import st_javascript
from user_agents import parse



App_Link = "https://app.picopacho.com/"

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="PICOPACHO",
    page_icon="static/Images/Logos/Badge_Tiny.png",
    layout = 'wide',
    initial_sidebar_state="collapsed"
    
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
Base_url = "https://picopacho.com"


hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)

#hide anchors
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")


if 'Features' not in st.session_state:
    st.session_state.Features = {
        'From Start to Fluent': 'PICOPACHO dynamically adjusts to all skill levels.',
        'Missions': 'Set your own missions or ask around! Characters throw you into memorable encounters right from the start.',
        'Endless Encounters': 'Whether you\'re starting a cult or a new job, everything is generated with AI just for you.',
        'Leaderboard': 'Compete on a global leaderboard for in-game rewards!',
    }



def FakeStream(text):
    for char in text:
        time.sleep(0.02)
        yield char
        
def displayFAQs():

    with st.expander("What is PICOPACHO?"):
        st.text("""PICOPACHO is a language learning game, in an infinite AI-generated world.  Learning a language is extremely hard, and can take months of effort just to get up and running. Staring at a textbook is not memorable experience at all, but sailing across the Atlantic would be!\n\nBabies (and adults) remember experiences, not conjugations, so we've set up PICOPACHO to put you in memorable experiences right from the start!""")
    with st.expander("How does it work?"):
        st.text("PICOPACHO is a browser game, talk to characters in your target language, visit new locations, collect items, and set your own missions. The game is a true sandbox, You can direct the game to specific situations you want to practice, or let the game lead the way.\n\nPICOPACHO is free to play for ~25 moves per day. If you are finding it works for you, you can upgrade to a paid subscription to unlock unlimited playtime.")
    
    with st.expander("What languages are supported?"):
        st.write("Currently, PICOPACHO supports English, French and German. We are working on adding more languages soon!")

    with st.expander("Where can I play?"):
        st.write("Currently, PICOPACHO is only available on desktop. Click the Start Game button below to start playing!")




def RenderDesktop():
    links = {
        'blank': 'blank',
        'blank2': 'blank2',
        'Home': '/',
        'Start Game': App_Link,
        'PachoNotes': 'pages/pachonotes.py',
        'Leaderboard': 'pages/leaderboard.py'
    }

    with stylable_container(
        key="header_container",
        css_styles="""
        {
            margin-top: -150px;
        }
        """
    ):
        #             logo p home start game patchnotes leaderboard
        Headercols = st.columns([1, 2, 1, 1, 1, 1, 3])
        with Headercols[0]:
            st.markdown("<img src='app/static/Images/Logos/Logo_Med.png' style='margin-top: 0px;'>", unsafe_allow_html=True)

        
        with Headercols[2]:
            with stylable_container(
                key="header_button",
                css_styles="""
                a:hover{
                    background-color: transparent;
                }
                """):
                st.link_button(list(links.keys())[2], links[list(links.keys())[2]], type = 'tertiary', use_container_width=True)
        with Headercols[3]:
            with stylable_container(
                key="header_button2",
                css_styles="""
                a:hover{
                    background-color: transparent;
                }
                """):
                st.link_button(list(links.keys())[3], links[list(links.keys())[3]], type = 'tertiary', use_container_width=True)

        with Headercols[4]:
            if st.button(list(links.keys())[4], type = 'tertiary', use_container_width=True):
                st.switch_page('pages/pachonotes.py')
        with Headercols[5]:
            if st.button(list(links.keys())[5], type = 'tertiary', use_container_width=True):
                st.switch_page('pages/leaderboard.py')


    # --- HERO SECTION ---
    with st.container():
        cols = st.columns([1, 6, 1, 5, 1])
        with cols[1]:
            st.container(border = False, height = 85)
            
            star_rating(5, color = "#D9D9D9")
            st.container(border = False, height = 1)
            st.markdown("<h1 style='text-align: left; font-size: 48px; font-weight: 600;margin-top: -50px;'>The #1 Way to Learn a Language is Through Play</h1>", unsafe_allow_html=True)
            
            st.markdown(
                """
                <p style="
                    text-align: left;
                    font-size: 16px;
                    font-weight: 400;
                    margin-top: -10px;
                    max-width: 70%;
                ">
                    "Enjoy what you do, and you'll never work a day in your life." - Mark Twain
                </p>
                """,
                unsafe_allow_html=True
            )

            
            with stylable_container(
                key="start_game_button",
                css_styles="""
                a {
                    border: none;
                    border-radius: 5555px;
                    color: #FFFFFF;
                    background-image: url('app/static/Images/StartGameGradient.png');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    height: 45px;
                    padding: 20px;
                    margin-left: 0s%;
                    margin-top: -15px;
                    border: 1px solid rgb(255, 255, 255, 0.1);
                    border-radius: 5555px;
                }
                a:hover {
                    background-color: #FFFFFF;
                    background-image: none;
                    border: 1px solid rgb(211, 211, 211);
                    border-radius: 5555px;
                }
                a:focus {
                    background-color: #FFFFFF;
                    background-image: none;
                    border: 1px solid rgb(211, 211, 211);
                    border-radius: 5555px;
                }
                """):
                st.container(border = False, height = 10)
                st.link_button("Start Game", url=App_Link, type = 'secondary')

        with cols[3]:
            st.markdown(f"<img src='app/static/Images/Farm.png' style='margin-top: 50px; float: right;'>", unsafe_allow_html=True)
            chatcols = st.columns([1, 1.8, 1])
            with chatcols[1]:
                cssstyles = """
                    {
                        border: none;
                        border-radius: 20px;
                        background-color: #E7E7E7;
                        height: 45px;
                        padding: 10px;
                        padding-left: 20px;
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
                    

            
    st.container(border = False, height = 64)
    # --- GET FLUENT, FAST ---
    with st.container():
        st.markdown("<img src='app/static/Images/GetFluentFast.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto; width: 30%;'>", unsafe_allow_html=True)
        st.container(border = False, height = 32)


    # --- FIND YOUR ADVENTURE ---
        cols = st.columns([1, 10, 1])
        with cols[1]:
            with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgb(238, 239, 241);
                    border-radius: 20px;
                    background-color: #FFFFFF;
                    box-shadow: 0px 0px 100px -60px rgba(0, 0, 0, 0.2);
                    z-index: 1000;
                }
                """,):
            
            
                with st.container():
                    content_cols = st.columns([1, 6, 6, 1])
                    with content_cols[1]:
                        st.container(border = False, height = 32)
                        st.markdown("<p style='text-align: left; font-size: 12px; font-weight: 400; margin-top: 0px; color: #A4A9BA;'>Explore</p>", unsafe_allow_html=True)
                        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600; margin-top: -20px;'>Start your adventure</h1>", unsafe_allow_html=True)
                        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Full realism, or play through your favorite movie? Every word you learn becomes another tool to carve your story.</p>", unsafe_allow_html=True)
                    with content_cols[2]:
                        #set z-index to 1000
                        st.markdown(f"<img src='app/static/Images/AdventureDesktop.png' style='margin-top: 0px; float: right; margin-right: -16%;width: 100%; height:100%;'>", unsafe_allow_html=True)


    st.container(border = False, height = 32)

    cssstylesPK = """
                {
                    border: 1px solid rgb(238, 239, 241);
                    border-radius: 20px;
                    background-image: url('app/static/Images/D_ProfessorPachoBG.png');
                    background-size: cover;
                    height: 700px;
                    padding: 80px;
                    margin-top: -50px;
                    box-shadow: 0px 0px 100px -60px rgba(0, 0, 0, 0.2);
                }
                """
    cssstylesChar = """
                {
                    border: 1px solid rgb(238, 239, 241);
                    background-image: url('app/static/Images/D_CharactersCardBG.png');
                    background-size: cover;
                    background-position: bottom;
                    height: 700px;
                    border-radius: 20px;
                    height: 700px;
                    padding: 80px;
                    margin-top: -50px;
                    box-shadow: 0px 0px 100px -60px rgba(0, 0, 0, 0.2);
                }
                """


    # --- POCKET TUTOR & INFINITE CHARACTERS ---

    _, col1, col2, __ = st.columns([1, 5, 5, 1])
    with col1:
            with stylable_container(
            key="container_with_border2",
            css_styles=cssstylesPK):
                with st.container():
                    st.markdown("<p style='text-align: left; font-size: 12px; font-weight: 400; margin-top: 0px; color: #A4A9BA;'>Learn</p>", unsafe_allow_html=True)
                    st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600; margin-top: -20px;'>Professor Pacho</h1>", unsafe_allow_html=True)
                    st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Your 24/7 tutor is ready to take you to the next level! Hot tips and questions answered.</p>", unsafe_allow_html=True)
                    st.container(border = False, height = 90)
                    content_cols = st.columns([1, 10, 1])
                    with content_cols[1]:
                        
                        st.markdown(f"<img src='app/static/Images/D_ProfessorPacho.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
                    st.container(border = False, height = 16)
            
    with col2:
        with stylable_container(
            key="container_with_border3",
            css_styles=cssstylesChar):
                with st.container():
                    st.markdown("<p style='text-align: left; font-size: 12px; font-weight: 400; margin-top: 0px; color: #A4A9BA;'>Discover</p>", unsafe_allow_html=True)

                    st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600; margin-top: -20px;'>Infinite Cast of Characters</h1>", unsafe_allow_html=True)
                    st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Scheme with your fellow rebels, or order a coffee - level up your language without even realizing.</p>", unsafe_allow_html=True)
                    st.container(border = False, height = 90)
                    st.markdown(f"<img src='app/static/Images/D_Characters.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
                    st.container(border = False, height = 48)




    # --- WE MAKE SPEAKERS ---
    st.container(border = False, height = 128)
    with st.container():
        st.markdown("<img src='app/static/Images/SpeakersMadeHere.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto; width: 30%;'>", unsafe_allow_html=True)
        
    # --- FEATURES ---
    st.container(border = False, height = 32)

    cssstyles = """
                {
                    border: none;
                    border-radius: 20px;
                    background-color: #FFFFFF;
                    height: 350px;
                    padding: 30px;
                    box-shadow: 0px 0px 100px -60px rgba(0, 0, 0, 0.2);
                }
                a:hover{
                    background-color: #000000;
                    border: 1px solid rgb(211, 211, 211);
                    border-radius: 20px;
                    box-shadow: 0px 0px 12px 0px rgba(157, 78, 221, 0.5);
                    color: #000000;
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
            st.markdown(f"<img src='app/static/Images/Icons/StartToFluent.png' style='margin-top: 0px; width: 20px;'>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>From Start to Fluent</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>{st.session_state.Features['From Start to Fluent']}</p>", unsafe_allow_html=True)
    with col2:
        with stylable_container(
            key="container_with_border5",
            css_styles=cssstyles):
            st.container(border = False, height = upperpad)
            st.markdown(f"<img src='app/static/Images/Icons/Missions.png' style='margin-top: 0px;'>", unsafe_allow_html=True)

            st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Missions</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>{st.session_state.Features['Missions']}</p>", unsafe_allow_html=True)
    with col3:
        with stylable_container(
            key="container_with_border6",
            css_styles=cssstyles):
            st.container(border = False, height = upperpad)
            st.markdown(f"<img src='app/static/Images/Icons/EndlessEncounters.png' style='margin-top: 0px;'>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Endless Encounters</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>{st.session_state.Features['Endless Encounters']}</p>", unsafe_allow_html=True)
    with col4:
        with stylable_container(
            key="container_with_border7",
            css_styles=cssstyles):
            st.container(border = False, height = upperpad)
            st.markdown(f"<img src='app/static/Images/Icons/Leaderboard.png' style='margin-top: 0px;'>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Leaderboard</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>{st.session_state.Features['Leaderboard']}</p>", unsafe_allow_html=True)


    # --- FAQ ---
    st.container(border = False, height = 64)
    with st.container():
        st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>FAQ</h1>", unsafe_allow_html=True)
        cols = st.columns([1, 2, 1])
        with cols[1]:
            displayFAQs()


    # #windmill footer
    st.container(border = False, height = 150)
    cols = st.columns([1, 4, 6, 1])
    with cols[1]:
        st.container(border = False, height = 64)
        st.markdown("<img src='app/static/Images/PlayForFree.png' style='margin-top: -50px; display: block; margin-left: auto; margin-right: auto; width: 100%;'>", unsafe_allow_html=True)

        st.container(border = False, height = 32)

        #start game button
        with stylable_container(
            key="start_game_button_white_desktop",
            css_styles="""
            a {
                background-color: #FFFFFF;
                border-radius: 100px;
                border: 1px solid rgb(211, 211, 211);
                color: #000000;
                padding-top: 10px;
                padding-bottom: 10px;
                height: 70px;
                box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
                border: none;
                float: inherit;
            }
            a:hover{
                background-image: None;
                background-color: #FFFFFF;
                box-shadow: 0px 0px 12px 0px rgba(157, 78, 221, 0.5);
                color: #000000;
            }

            """
        ):
            butcols = st.columns([5, 8, 5])
            with butcols[1]:
                st.link_button("Start Game", url=App_Link, type = "tertiary", use_container_width=True)





    with cols[2]:
        st.markdown(f"<img src='app/static/Images/WindmillFooterLargeCropped.png' style='margin-top: 0px; float: right; margin-right: 10%; margin-bottom: -15px;'>", unsafe_allow_html=True)
    
    #white background
    cssstyles = """
    {
    background-color: #FFFFFF;
    height: 100%;
    width: 100%;
    margin-top: 0px;
    box-shadow: 0px 500px 0px 500px rgba(255, 255, 255, 1);
    }
    a:hover{
        box-shadow: none;
        border: none;
    }
    """
    with stylable_container(
        key="footer_container",
        css_styles=cssstyles):
        

        st.container(border=False, height=180)
        st.markdown("<img src='app/static/Images/Logos/Logo_Blackout_Med.png' style='margin-top: 0px; width: 200px;'>", unsafe_allow_html=True)
        st.container(border=False, height=20)

        st.markdown("<p style='text-align: left; color: #A4A9BA; font-size: 12px; font-weight: 400; padding-left: 20px; letter-spacing: 0.6em;'>Site</p>", unsafe_allow_html=True)
        
        cssstyles_footerlinks = """
            a {
                padding-left: 20px;
            }
            """
        cssstyles_footerlinks2 = """
                button {
                padding-left: 20px;
            }
            """
        
        with stylable_container(
            key="footer_links",
            css_styles=cssstyles_footerlinks):
            st.link_button("Home", '/', type="tertiary")
            st.container(border=False, height=1)
            st.link_button("Start Game", url=App_Link, type="tertiary")
        with stylable_container(
            key="footer_links2",
            css_styles=cssstyles_footerlinks2):
            if st.button("PachoNotes", type="tertiary"):
                st.switch_page('pages/pachonotes.py')
            st.container(border=False, height=1)
            if st.button("Leaderboard", type="tertiary"):
                st.switch_page('pages/leaderboard.py')
        #st.link_button("Invite to Earn", 'www.joinpicopacho.streamlit.app', type="tertiary")
        #st.link_button("Give Feedback", 'www.joinpicopacho.streamlit.app', type="tertiary")
        
        st.container(border=False, height=20)

        st.markdown("<p style='text-align: left; color: #A4A9BA; font-size: 12px; font-weight: 400; padding-left: 20px; letter-spacing: 0.6em;'>Community</p>", unsafe_allow_html=True)

        with stylable_container(
            key="footer_community_links",
            css_styles=cssstyles_footerlinks):
            st.link_button("Discord", 'https://discord.gg', type="tertiary")
            st.container(border=False, height=1)
            st.link_button("Youtube", 'https://www.youtube.com', type="tertiary")
            st.link_button("Twitter/X", 'https://x.com', type="tertiary")

    




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
                button{
                    border: none;
                    border-radius: 20px;
                    text-align: right;
                    float: right;
                }
                """):

                st.link_button("Home", '/', type="tertiary")
                st.container(border=False, height=1)
                st.link_button("Start Game", url=App_Link, type="tertiary")
                if st.button("PachoNotes", type="tertiary"):
                    st.switch_page('pages/pachonotes.py')
                if st.button("Leaderboard", type="tertiary"):
                    st.switch_page('pages/leaderboard.py')
            
        
        
    

    # Stars
    st.markdown("<img src='app/static/Images/Icons/Stars.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto; width: 30%;'>", unsafe_allow_html=True)

    # Title Text
    st.markdown("<h1 style='text-align: center; font-size: 48px; font-weight: 600; line-height: 1.1; margin-top: -20px;'>The #1 way to learn a language is</h1>", unsafe_allow_html=True)

    # Play Text
    st.markdown("<img src='app/static/Images/GreenPlay.png' style='margin-top: 0px;'>", unsafe_allow_html=True)
    
    # Start Game Button
    with stylable_container(
        key="start_game_button",
        css_styles="""
        a {
            
            background-image: url('app/static/Images/StartGameGradient.png');
            background-size: cover;
            border-radius: 100px;
            border: none;
            text-align: center;
            font-size: 64;
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
        a:hover {
            background-image: None;
            background-color: #FFFFFF;
            box-shadow: 0px 0px 12px 0px rgba(157, 78, 221, 0.5);
            text-color: #000000;
            

        """
    ):
        st.link_button("Play Now", url=App_Link, type = "secondary")
            

    st.container(border=False, height=30)

    # Farm Image
    st.markdown("<img src='app/static/Images/Farm.png' style='margin-top: 0px; display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.container(border=False, height=5)

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
                width: 75%;
                padding-top: 10px;
                padding-left: 20px;
                margin-left: 20px;
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
                margin-right: 20px;
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
    
    st.container(border=False, height=70)
    with st.container():
        
        st.markdown("<div style='display: flex; justify-content: center;'><img src='app/static/Images/SpeakersMadeHere.png' style='margin-top: 0px; width: 100%; max-width: 900px;'></div>", unsafe_allow_html=True)

    st.container(border=False, height=30)
    
    # --- FEATURES ---
    features = [
        {"icon": "static/Images/Icons/StartToFluent.png", "title": "From start to fluent", "text": "Take your experience to match you where you are. PICOPACHO dynamically adjusts to all skill levels."},
        {"icon": "static/Images/Icons/Missions.png", "title": "Missions", "text": "Get your own mission or ask around! Characters will throw you into memorable encounters right from the start."},
        {"icon": "static/Images/Icons/EndlessEncounters.png", "title": "Endless encounters", "text": "Whether you're starting a cult or a new job, everything is generated just for you."},
        {"icon": "static/Images/Icons/Leaderboard.png", "title": "Leaderboard", "text": "Compete on a global leaderboard for in-game rewards!"}]

    for feature in features:
        with st.container():
            st.markdown(f"<img src='app/{feature['icon']}' style='margin-top: 0px; width: 64px;'>", unsafe_allow_html=True)
        
            st.markdown(f"<h4 style='margin-top: -10px;'>{feature['title']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p>{feature['text']}</p>", unsafe_allow_html=True)
        st.container(border=False, height=20)


    # --- FAQ ---
    st.container(border=False, height=64)
    with st.container():
        st.markdown("<h1 style='text-align: center; font-size: 38px; font-weight: 600;'>FAQ</h1>", unsafe_allow_html=True)
        displayFAQs()

            
    # --- PLAY FOR FREE ---
    st.container(border=False, height=64)
    
    st.markdown("<img src='app/static/Images/PlayForFree.png' style='margin-top: 0px;'>", unsafe_allow_html=True)
    
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
            border: 1px;
            float: inherit;
            text-color: #000000;
            font-size: 24px;
        }
        a:hover {
            background-image: None;
            background-color: #FFFFFF;
            box-shadow: 0px 0px 12px 0px rgba(157, 78, 221, 0.5);
            text-color: #000000;
        }
        """
    ):
        st.container(border=False, height=10)
        st.link_button("Start Game", url=App_Link, type = "secondary")

    # --- FOOTER Image ---
    st.container(border=False, height=30)
    st.markdown("<img src='app/static/Images/WindmillFooter.png' style='margin-top: 0px; width :500px; display: block; margin-left: auto; margin-right: auto; border-radius: 20px;'>", unsafe_allow_html=True)
    st.container(border=False, height=180)








    # --- FOOTER ---
    st.markdown("<img src='app/static/Images/Logos/Logo_Blackout_Med.png' style='margin-top: 0px; width: 200px;'>", unsafe_allow_html=True)
    st.container(border=False, height=20)

    st.markdown("<p style='text-align: left; color: #A4A9BA; font-size: 12px; font-weight: 400; padding-left: 20px; letter-spacing: 0.6em;'>Site</p>", unsafe_allow_html=True)
    
    cssstyles_footerlinks = """
        a {
            padding-left: 20px;
        }
        a:hover{
            background-color: transparent;
            box-shadow: none;
        }
        """
    cssstyles_footerlinks2 = """
            button {
            padding-left: 20px;
            float:left;
        }
        a{
            float:left;
        }
        """
    
    with stylable_container(
        key="footer_links",
        css_styles=cssstyles_footerlinks):
        st.link_button("Home", '/', type="tertiary")
        st.container(border=False, height=1)
        st.link_button("Start Game", url=App_Link, type="tertiary")
    with stylable_container(
        key="footer_links2",
        css_styles=cssstyles_footerlinks2):
        if st.button("PachoNotes", type="tertiary", key="footer_pachonotes_button"):
            st.switch_page('pages/pachonotes.py')
        st.container(border=False, height=1)
        if st.button("Leaderboard", type="tertiary", key="footer_leaderboard_button"):
            st.switch_page('pages/leaderboard.py')
    #st.link_button("Invite to Earn", 'www.joinpicopacho.streamlit.app', type="tertiary")
    #st.link_button("Give Feedback", 'www.joinpicopacho.streamlit.app', type="tertiary")
    
    st.container(border=False, height=20)

    st.markdown("<p style='text-align: left; color: #A4A9BA; font-size: 12px; font-weight: 400; padding-left: 20px; letter-spacing: 0.6em;'>Community</p>", unsafe_allow_html=True)

    with stylable_container(
        key="footer_community_links",
        css_styles=cssstyles_footerlinks):
        st.link_button("Discord", 'https://discord.gg', type="tertiary")
        st.container(border=False, height=1)
        st.link_button("Youtube", 'https://www.youtube.com', type="tertiary")
        st.link_button("Twitter/X", 'https://x.com', type="tertiary")



ua_string = None
while ua_string is None or ua_string == "None":
    ua_string = str(st_javascript("""window.navigator.userAgent;"""))
    time.sleep(0.9)
user_agent = parse(ua_string)
st.session_state.is_session_pc = bool(user_agent.is_pc)
print('here: ')
print(st.session_state.is_session_pc)
if st.session_state.is_session_pc == True:
    RenderDesktop()
    #RenderMobile()
else:
    RenderMobile()

#RenderMobile()

