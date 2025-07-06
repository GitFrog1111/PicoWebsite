import streamlit as st
from streamlit_extras.star_rating import star_rating
from streamlit_extras.stylable_container import stylable_container
import time

from streamlit_js_eval import streamlit_js_eval

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



#test
Mobile = streamlit_js_eval(js_expressions="""
function() {
  let check = false;
  (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
  return check;
};
                  """)

st.write(Mobile)
time.sleep(10)




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
        st.markdown(f"<img src='app/static/Images/Farm.png' style='margin-top: 0px; float: right;'>", unsafe_allow_html=True)
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
                
                imagesizer = st.columns([1.2, 1])
                with imagesizer[1]:
                    #set z-index to 1000
                    st.markdown(f"<img src='app/static/Images/Boatyard.png' style='margin-top: -250px; float: right; margin-right: 10%;'>", unsafe_allow_html=True)


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
                    st.markdown(f"<img src='app/static/Images/PocketTutor.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
        
with col2:
    with stylable_container(
        key="container_with_border3",
        css_styles=cssstyles):
            with st.container():

                st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Infinite Characters</h1>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Negotiate hostage transfers with the chieftain of the northern tribes, or  just order a coffee. Level up your language skills without realising.</p>", unsafe_allow_html=True)
                st.container(border = False, height = 35)
                st.markdown(f"<img src='app/static/Images/Characters.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)




# --- WE MAKE SPEAKERS ---
with st.container():
    st.container(border = False, height = 100)
    st.markdown(f"<img src='app/static/Images/Lorals.png' style='margin-top: 0px; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
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
        st.markdown(f"<img src='app/static/Images/FromStartToFluent.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
        st.container(border = False, height = lowerpad)
        
        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>From start to fluent</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Take your experience to match you where you are. Pico Pedro dynamically adjusts to all skill levels.</p>", unsafe_allow_html=True)
with col2:
    with stylable_container(
        key="container_with_border5",
        css_styles=cssstyles):
        st.container(border = False, height = upperpad)
        st.markdown(f"<img src='app/static/Images/Missions.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
        st.container(border = False, height = lowerpad)
        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Missions</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Get your own mission or ask around! Characters will throw you into memorable encounters right from the start.</p>", unsafe_allow_html=True)
with col3:
    with stylable_container(
        key="container_with_border6",
        css_styles=cssstyles):
        st.container(border = False, height = upperpad)
        st.markdown(f"<img src='app/static/Images/EndlessEncounters.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
        st.container(border = False, height = lowerpad)
        st.markdown("<h1 style='text-align: left; font-size: 24px; font-weight: 600;'>Endless encounters</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 16px; font-weight: 400; margin-top: -10px;'>Whether you're starting a cult or a new job, everything is generated just for you.</p>", unsafe_allow_html=True)
with col4:
    with stylable_container(
        key="container_with_border7",
        css_styles=cssstyles):
        st.container(border = False, height = upperpad)
        st.markdown(f"<img src='app/static/Images/Leaderboard.png' style='margin-top: 0px; height: 30px;'>", unsafe_allow_html=True)
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
            st.link_button("Enter World",url=App_Link, type = 'primary')
        

# --- BETA NOW LIVE ---
st.container(border = False, height = 64)
cssstyles = """
            {
                border: none;
                background-image: url('app/static/Images/Purp2.png');
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

                st.markdown(f"<img src='app/static/Images/BetaGardens.png' style='margin-top: -120px; float: right;'>", unsafe_allow_html=True)
