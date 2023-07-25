import argparse
import json
import streamlit as st

def tell_format(data):
    try:
        arts = data["articles"]
    except:
        return False

    for art in arts:
        if "title" not in art or "article" not in art or "hints" not in art:
            return False
    
    return True

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="These parameters are available:",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件地址", required=True)
    parser.add_argument("-a", "--article", help="文章标题", required=False)
    # TODO: 添加更多参数
    
    args = parser.parse_args()
    return args

def default_file():
    data = {}
    data["article"] = []
    data["article"].append({"title": "贵系日常", "article": "我们都爱{{1}}这门课程。这门课程是多么的{{2}}，以至于所有人都在课程上认真地{{3}}。在设计数字电路时,我们需要运用到逻辑门、半导体存储器等知识。这些内容相互联系,共同构成复杂的数字电路。这门课能启发我们的逻辑思维能力和科学思考能力。通过为难我们的练习和作业,我们的理解能力和解决问题的能力得到了提高。这些将对今后的{{4}}和工作有很大益处。", "hints": ["教材名称", "形容词", "动词，与学生相关", "你最喜欢做的事情"]})
    with open("./mondai/default.json", 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return data

def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not tell_format(data):
                    raise Exception("JsonFormatError")
            except:
                raise Exception("JsonFormatError")
    except Exception as e:
        if e.args[0] == "JsonFormatError":
            st.warning("Json format error! Default file loaded.")
        else:
            st.warning("File not found! Default file loaded.")
        data = default_file()
    
    return data

def load():
    args = parser_data()
    data = read_articles(args.file)
    return (data["articles"], args)