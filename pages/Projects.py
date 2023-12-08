import streamlit as st

st.set_page_config(
    page_title="My blog",
    page_icon="favicon.png", 
    layout="wide"
)

style_file_path = "style/style.css"

with open(style_file_path, "r") as css_file:
    css = css_file.read()   
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    
st.markdown("""<h1 class="BOLD">Projects</h1>""",unsafe_allow_html=True)

st.markdown("""<h2 class="BOLD" id="MyProj">These are my projects</h2>""",unsafe_allow_html=True)

column1, column2, column3, column4 = st.columns(4)

with column1:
    st.markdown("""
    <img id="column_1_img" src="https://scontent.fmnl8-2.fna.fbcdn.net/v/t1.15752-9/370087655_316804891271106_9221092602182200389_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeEygpknPFKqJsXfaqJlMHx8j7kaU6gdFrSPuRpTqB0WtIsTwCH2O1JfpqvC-tJhfX2jOZYy73tE4x-9t3tB_OXJ&_nc_ohc=zlRz3qBo1FIAX_8KUYP&_nc_ht=scontent.fmnl8-2.fna&cb_e2o_trans=t&oh=03_AdTL0mrIcGLHWeMLSRUnpp6YrEomfHQonURr0Xh3GXNdwA&oe=6590A631">
    """,unsafe_allow_html=True)

    st.markdown("""
    <img id="column_2_img" src="https://scontent.fmnl8-1.fna.fbcdn.net/v/t1.15752-9/385550863_3721043308126593_3113214092202175756_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeGRtMjRj3ZNZB22KGaDw851kf1NOfLW-KSR_U058tb4pIeuxQV01Ou_FLGIPuZS1-K_7py2y5x-k3KtpK4TrCup&_nc_ohc=7WJlOkUDmF4AX-6l2Ov&_nc_ht=scontent.fmnl8-1.fna&cb_e2o_trans=t&oh=03_AdTQxU6vdN5VYh3OYW8gJf2V2UfcXvt74rpUELFgow6SPQ&oe=6590C321">
    """,unsafe_allow_html=True)

with column2:
    st.markdown("""
    <img id="column_3_img" src="https://steamuserimages-a.akamaihd.net/ugc/2000215800919995881/E198D28CBE64E207F3F7A3DF240A19D900E9DFFB/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false" height="300px">">
    """,unsafe_allow_html=True)

    st.markdown("""
    <img id="column_4_img" src="https://steamuserimages-a.akamaihd.net/ugc/2093669747578440993/48D030853B7EF29EC8C21FCC2CA83B402080A365/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false">
    """,unsafe_allow_html=True)

with column3:
    st.markdown("""
    <img id="column_5_img" src="https://scontent.fmnl8-2.fna.fbcdn.net/v/t1.15752-9/385536980_652349013774202_4312151579944546658_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeG8-10kEpRfFuc4DOp6VNt5h8XkEmqCVmGHxeQSaoJWYQZu8oRsO4dso2rKvWu3Mt4zL1uCentqoVbMFVPW4Gle&_nc_ohc=885K6L00Jc4AX_2ApKM&_nc_ht=scontent.fmnl8-2.fna&cb_e2o_trans=t&oh=03_AdTWDWloxbpH7lqlHqDmY2QDFU9fvXpaR6Nl2DB7_el7pQ&oe=6590A08B">
    """,unsafe_allow_html=True)

    st.markdown("""
    <img id="column_6_img" src="https://scontent.fdvo2-1.fna.fbcdn.net/v/t1.15752-9/386445509_3265372900275673_6281375046752245621_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeGIuiqj9nSSqfaUjMLGz5ZhOktR9fryCkM6S1H1-vIKQ4jHSB-LvisMsiHINrI9OO88GnWIC1uDczuyhbRVHWyX&_nc_ohc=ykwwy0yRH_MAX9cTXAE&_nc_ht=scontent.fdvo2-1.fna&oh=03_AdQPNTacrvJgEKsRqhojF7hijT5BS6CWQYgCBFXgpBunTg&oe=6596A3E7">
    """,unsafe_allow_html=True)

with column4:
    pass
