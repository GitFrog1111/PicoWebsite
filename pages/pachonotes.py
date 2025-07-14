import streamlit as st

st.set_page_config(page_title='Pachonotes',
                   page_icon='app/static/Images/Logos/Badge_Tiny.png',
                   layout='wide')


def Main():
    Post1()

def Post1():
    R = st.container(border=True)
    with R:
        st.markdown(f"<img src='app/static/Images/WindmillFooterLargeCropped.png' style='width: 50%; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        st.title('Pico Public Beta')
        st.caption('July 15, 2025')
        st.text("""Hallo, Wie geht's?
                We are excited to announce that PICOPACHO has now entered public beta! This is a huge milestone and we are super grateful for your support.
                
                ##So what is PICOPACHO?##
                PICOPACHO is a game that helps you learn languages by speaking with AI.
                
                ##Why build this?##
                I have been living in Thailand for around 9 months now with many false starts when it comes to learning Thai. I have tried the apps, including the new ones that are all 'speak with an AI tutor'. What I've found is that they don't work very well - for me at least. They feel like I am back at school, trudging through an endless stream of rules I just have to memorise one after another when really that is not what I need, I want to understand and be understood, that's it.
                
                I had a lightbulb moment during this time, the way I was most effectively remembering Thai was through the memories I attached to each word. If I wanted to say spicy, my head pings with that first time I said it at a noodle shop (and they corrected me). If I want to say 'chicken' I cannot help but think of that one time I ordered chicken wings from this guy outside the supermarket near me.
                
                Looking into this I came across the 'Automatic language growth' community - now it was clear this was the way. If you're interested in the real reasons why this stuff works, check out https://beyondlanguagelearning.com/about-beyond-language-learning/ and specifically the story of J. Marvin Brown. Great video here: https://www.youtube.com/watch?v=984rkMbvp-w&list=LL&index=8
                
                It just so happened I was building a game to do tabletop RPG with AI, nice UI, missions, encounters etc. By some miracle I realised that actually what I was building was the perfect way to learn a language.
                
                ##How does it work?##
                Back to basics - babies learn through 'comprehensible input'. This is the combo of what is happening and what is being said... like dogs - If you say 'Walkies' once before a walk it means nothing, but that seconds time, they know exactly whats coming. Babies do not use Duolingo, they map sounds to experiences, and build understanding unconsciously. The thing is, this method does not go away, we just don’t consider it as adults, we prefer what we know to work with rules and defined paths and correctness - schooling. It's absolute wash.
                
                PICOPACHO is founded on this idea, the best way to learn is attaching sounds to encounters. Your brain has incredible built-in circuits, spatial memory, facial recognition, motion detection - and yes, language acquisition - Nature however did not build this circuit from textbooks and conscious study, so why make it hard on yourself? PICOPACHO makes it fun, and actually faster, to learn a language. If you like what you see, join the discord and help shape the future of PICOPACHO.
                
                We have a lot of features planned for the future and we are excited to share them with you over the coming months. We are also working on a lot of bug fixes and improvements - if you run into a bug please drop a report in the discord.

                Best,
                yaml
                """)
    
    return R



def Postplaceholder():
    R = st.container()
    with R:
        st.write('this is the post 1 page')
    
    return R

Main()