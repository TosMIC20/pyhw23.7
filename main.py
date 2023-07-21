import argparse
import json
import re

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="python(3) main.py",
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
            # 用 json 解析文件 f 里面的内容，存储到 data 中
            try:
                data = json.load(f)
            except Exception:
                raise Exception("Json")
    except Exception as e:
        if e.args[0] == "Json":
            print("json file format error! Check it out! Default file is loaded.")
        else:
            print("Target file not found! Default file is loaded.")
        data = default_file()
    
    return data

def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        ans = input(f"请输入{hint}：")
        keys.append(ans)
        # TODO: 读取一个用户输入并且存储到 keys 当中

    return keys

def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    def key(matched):
        return keys[int(matched.groups()[1])-1]
    article["article"] = re.sub("(\{\{)([0-9])(\}\})", key, article["article"])

        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换

    return article

def decide_article(args, articles):
    if args.article is not None:
        for article in articles:
            if article["title"] == args.article:
                return article
    else:
        return ask_for_article(articles)
    
def ask_for_article(articles):
    pass
    
if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)

    try:
        articles = data["articles"]
    except Exception as e:
        if e.args[0] == "articles":
            print("json file format error! Check it out! Default file is loaded.")
            data = default_file()
            articles = data["articles"]

    if articles:
        article = decide_article(args, articles)
    else:
        print("No articles found! Create one instead?[y/n]")

    keys = get_inputs(article["hints"])
    article = replace(article, keys)
    print(article["article"])

        # TODO: 根据参数或随机从 articles 中选择一篇文章
        # TODO: 给出合适的输出，提示用户输入
        # TODO: 获取用户输入并进行替换
        # TODO: 给出结果
