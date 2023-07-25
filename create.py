import streamlit as st
import re
import json

def collect_text():
    if st.session_state["title"] != "" and st.session_state["text_area"] != "":
        st.session_state["article"] = {"title": st.session_state["title"], "article": st.session_state["text_area"]}
        st.session_state["title"] = ""
        st.session_state["text_area"] = ""
    else:
        st.session_state["article"] = {}

def produce_article():
    article = {}

    article["title"] = st.session_state["article"]["title"]

    st.session_state["count"] = 0

    def number(matched):
        st.session_state["count"] += 1
        return "{{"+str(st.session_state["count"])+"}}"
    
    article["article"] = re.sub(r"{{\w+}}", number, st.session_state["article"]["article"])

    article["hints"] = [hint[1] for hint in re.findall(r"({{)(\w+)(}})", st.session_state["article"]["article"])]

    return article

def create(filename):
    st.markdown("To create new problems, you can put the article you want in the text box below. Where a blank is desired, place a string like `{{Hint_text}}`.")

    if "article" not in st.session_state:
        st.session_state["article"] = {}

    st.text_input("Title:", key="title", placeholder="Enter the title", label_visibility="collapsed")

    st.text_area("Text area:",key="text_area", placeholder="Type your article here.", label_visibility="collapsed")

    st.button("Submit", on_click = collect_text)

    if st.session_state["article"]:

        article = produce_article()

        st.radio("Save to:", ("New file", "Current file"), key="saveMode", horizontal=True)

        if st.session_state["saveMode"] == "New file":
            st.text_input("Enter", key="filepath", placeholder="Enter new file 'path/name', suggest you put it in './mondai/'", label_visibility="collapsed")
        
        if st.button("Save"):
            if st.session_state["saveMode"] == "Current file":
                with open(filename, 'r', encoding="utf-8") as f:
                    data = json.load(f)
                data["articles"].append(article)
                with open(filename, 'w', encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            elif st.session_state["saveMode"] == "New file":
                data = {"articles": [article]}
                with open(st.session_state["filepath"], 'w', encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
