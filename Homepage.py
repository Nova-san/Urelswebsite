import streamlit as st

st.set_page_config(
    page_title="The Phansite",
    page_icon="favicon.png", 
    layout="wide"
)

style_file_path = "style/style.css"

with open(style_file_path, "r") as css_file:
    css = css_file.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown("""<h1 class="BOLD">Urel Chua's Phansite</h1>""",unsafe_allow_html=True)

st.markdown("""

    <div class="Introduction">
            
    <p>Hey there! I'm Urel Chua, A first year student from SNSU and I'm on a thrilling journey in the world of programming and digital creativity. I breathe life into my ideas through the magic of coding and the art of Source Filmmaker (SFM) renders.</p>

    <img class="Introduction" src="https://scontent.fdvo2-1.fna.fbcdn.net/v/t39.30808-6/350683496_173631855664466_2841319463707368727_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=9c7eae&_nc_eui2=AeGaFWNRrsBOJO7Xq2FRY5Srx0lBasO18JzHSUFqw7XwnO38OuwQIjlQKAVh55Hg319cHCwRdlyQvKdDsbWXTGqB&_nc_ohc=3kKPZBGGB1UAX_1Hn0O&_nc_ht=scontent.fdvo2-1.fna&oh=00_AfBevngNGAsUN9x0B64saz8o_2DIzw5j1MCjz7QhL9d9hQ&oe=65783FCF"
            width="450" 
            height="450"/>
            
    <p>Passionate Programmer:</p>
            
    <div>

    <img class="PasProg" src="https://64.media.tumblr.com/106e4a7ae6ec718d2d7d319248483302/tumblr_oquizfBkfn1v89ei5o1_500.gif">

    </div>

            

    <p>My love for programming goes beyond lines of code; it's about crafting solutions, solving puzzles, and turning concepts into reality. From tinkering with algorithms to developing sleek applications, I find joy in the ever-evolving world of software development.</p>

    <p>SFM Maestro:</p>
            
    <div>

    <img class="PasProg" src="https://c.tenor.com/RkFcfe95kYwAAAAd/source-filmmaker.gif">

    </div>


    <p>When I'm not immersed in code, you'll find me lost in the virtual realm of Source Filmmaker. I'm passionate about creating stunning renders that tell stories, evoke emotions, and capture the essence of imagination. SFM is my canvas, and every project is a new opportunity to blend technology with artistic expression.</p>

    <p>Why SFM?
            
    <div>

    <img class="PasProg" src="https://media.tenor.com/b3xW7DQjtc0AAAAC/futaba-sakura.gif">
    </div>




    <p>Source Filmmaker, with its powerful tools and endless possibilities, allows me to merge my programming mindset with my artistic soul. It's not just about rendering scenes; it's about crafting visual narratives that resonate with people and leave a lasting impression.</p>

    <p>Beyond the Screen:
            
    <div>

    <img class="PasProg" src="https://media.tenor.com/t2D1EKGneG0AAAAd/joker-persona.gif">
    </div>
            
    <p>While I'm most at home in the digital realm, I also thrive in real-life adventures. Whether it's exploring the latest trends in technology or seeking inspiration from diverse sources, I'm always on the lookout for ways to expand my horizons.</p>

    </div>
""",unsafe_allow_html=True)

