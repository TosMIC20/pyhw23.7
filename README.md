# sast2023 word game

## 环境配置

使用 Streamlit 构建图形界面，已经写入 requirements.txt.
Streamlit 官方建议在虚拟环境中安装 Streamlit.

## 使用设置

请在存在 Strealit 的环境下运行以下指令启动，并打开显示的网页：

``` shell
streamlit run main.py
```

约定以下参数：  （注：Streamlit 要求在这些参数之前再加 `--` 以表示这些是传给程序的参数而不是传给 Streamlit 的参数）

```shell
--help -h 命令行查看参数说明
--file  -f  接文章的路径
--article -a 接文章的标题（可选）
```

~~*事实上，制作了选择文章功能，所以选文章的命令参数没什么用，只会改变进入游戏时的默认选中文章*~~

文章使用 JSON 存储，格式如下：

```json
{
    "articles": [
        {
            "title": "标题示例",
            "article": "正文示例，空示例{{1}}.",
            "hints": ["提示示例"]
        }
    ]
}
```



## 游戏功能

打开网页后，有两种模式可以选择，Creat 和 Play.

### Creat 模式

即出题模式，按照提示将文章和标题输入过后，先点击 Submit 按钮提交，然后可以选择保存到新文件或者添加到当前打开的文件的文章列表之后；

### Play 模式

即核心玩法，点击 Play 后，会弹出一系列提示，按照提示填入词语，填空完毕后会显示生成的文章；