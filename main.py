import streamlit as st
import load as ld
import create as cr
import play as pl

def initial_choice(arga, articles):
    for ind in range(len(articles)):
        if articles[ind]["title"] == arga:
            return ind
    else:
        return 0

def get_title(article):
    return article["title"]

if __name__ == "__main__":
    st.title("Article Filling-in Game")
    
    # Load from file
    (articles, args) = ld.load()
    if len(articles) == 0:
        st.warning("No article detected in file! Create one!")
        
    # Select mode
    st.radio("Mode:", ("Create", "Play"), key="mode", horizontal=True)

    # Start
    if st.session_state["mode"] == "Create":
        cr.create(args.file)
    elif st.session_state["mode"] == "Play":
        col1, col2 = st.columns(2)
        st.write("Choose one article from above!")
        if "play" not in st.session_state:
            st.session_state["play"] = False
        with col1:
            st.selectbox("Articles", articles, initial_choice(args.article, articles), get_title, key="artSelect", label_visibility="collapsed")
        with col2:
            if st.button("Play"):
                st.session_state["play"] = True
                st.session_state["Input"] = []
        
        if st.session_state["play"] and len(articles) != 0:
            pl.play(st.session_state["artSelect"])
    