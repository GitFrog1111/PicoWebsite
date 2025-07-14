import streamlit as st
from streamlit_extras.stylable_container import stylable_container



st.set_page_config(page_title='Pachonotes',
                   page_icon='app/static/Images/Logos/Badge_Tiny.png',
                   layout='wide')

# force itim font
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Itim&display=swap');
body {
    font-family: 'Itim', sans-serif;
}     
</style>
""", unsafe_allow_html=True)

hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)




def Header():
    links = {
        'blank': 'blank',
        'blank2': 'blank2',
        'Home': 'https://picopacho.com',
        'Start Game': 'app.picopacho.com',
        'PachoNotes': 'pages/pachonotes.py',
        'Leaderboard': 'pages/leaderboard.py'
    }

    with stylable_container(
        key="header_container",
        css_styles="""
        {
            margin-top: -108px;
        }
        """
    ):
        #             logo p home start game patchnotes leaderboard
        Headercols = st.columns([1, 2, 1, 1, 1, 1, 3])
        with Headercols[0]:
            st.markdown("<img src='app/static/Images/Logos/Logo_Med.png' style='margin-top: 0px;'>", unsafe_allow_html=True)

        
        with Headercols[2]:
            if st.button(list(links.keys())[2], links[list(links.keys())[2]], type = 'tertiary', use_container_width=True):
                st.switch_page('app.py')

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

def Footer():
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
            st.link_button("Start Game", url='https://app.picopacho.com', type="tertiary")
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

    


def Main():
    Header()

    Post1()

    Footer()

def Post1():
    R = st.container(border=False)
    with R:
        st.markdown(f"<img src='app/static/Images/PachoNotes/DesertMarktBanner.png' style='width: 100%; height: 500px; object-fit: cover; object-position: top; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        with st.container(border=True):
            st.title('Pico Public Beta Ver 0.9.0')
            st.caption('July 15, 2025')
            st.markdown("""
<p>
Hallo, Wie geht's?
We are excited to announce that PICOPACHO has now entered public beta! This is a huge milestone and we are super grateful for your support.

### So what is PICOPACHO?

PICOPACHO is a game that helps you learn languages by speaking with AI.

### Why build this?

I have been living in Thailand for around 9 months now with many false starts when it comes to learning Thai. I have tried the apps, including the new ones that are all 'speak with an AI tutor'. What I've found is that they don't work very well - for me at least. They feel like I am back at school, trudging through an endless stream of rules I just have to memorise one after another when really that is not what I need, I want to understand and be understood, that's it.

I had a lightbulb moment during this time, the way I was most effectively remembering Thai was through the memories I attached to each word. If I wanted to say spicy, my head pings with that first time I said it at a noodle shop (and they corrected me). If I want to say 'chicken' I cannot help but think of that one time I ordered chicken wings from this guy outside the supermarket near me.

Looking into this I came across the 'Automatic language growth' community - now it was clear this was the way. If you're interested in the real reasons why this stuff works, check out https://beyondlanguagelearning.com/about-beyond-language-learning/ and specifically the story of J. Marvin Brown. Great video here: https://www.youtube.com/watch?v=984rkMbvp-w&list=LL&index=8

It just so happened I was building a game to do tabletop RPG with AI, nice UI, missions, encounters etc. By some miracle I realised that actually what I was building was the perfect way to learn a language.

### How does it work?

Back to basics - babies learn through 'comprehensible input'. This is the combo of what is happening and what is being said... like dogs - If you say 'Walkies' once before a walk it means nothing, but that second time, they know exactly what's coming. Babies do not use Duolingo, they map sounds to experiences, and build understanding unconsciously. The thing is, this method does not go away, we just don’t consider it as adults, we prefer to work with what we know, rules and defined paths and correctness - schooling. It's kind of ridiculous.

PICOPACHO is founded on this idea, the best way to learn is attaching sounds to encounters. Your brain has incredible built-in circuits, spatial memory, facial recognition, motion detection - and yes, language acquisition - Nature however did not build this circuit from textbooks and conscious study, so why make it hard on yourself? PICOPACHO makes it fun, and actually faster, to learn a language. If you like what you see, join the discord and help shape the future of PICOPACHO.

We have a lot of features planned for the future and we are excited to share them with you over the coming months. We are also working on a lot of bug fixes and improvements - if you run into a bug please drop a report in the discord.

Best,
yaml
</p>
                """, unsafe_allow_html=True)

    return R



def Postplaceholder():
    R = st.container()
    with R:
        st.write('this is the post 1 page')
    
    return R

Main()