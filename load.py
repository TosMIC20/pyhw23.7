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
    with open("./mondai/default.json", 'r', encoding="utf-8") as f:
        return json.load(f)

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
    return (data["articles"], args.article)