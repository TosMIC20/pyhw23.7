# sast2023 word game

## 环境配置

目前没有第三方依赖项

## 使用设置

约定以下参数：  

```
--help -h 命令行查看参数说明
--file  -f  接文章的路径
--article -a 接文章的标题（可选）
```

文章使用 JSON 存储，的格式如下：
```
{
    "language": "zh",
    "articles": [
        {
            "title": "标题示例",
            "article": "正文示例，空示例{{1}}；",
            "hints": ["提示示例"]
        }
    ]
}
```

## 游戏功能

