# 惊雷！我通天修为天塌地陷紫金锤...

## 功能介绍

鉴于近日沉迷喊麦神曲洗脑，在知乎上看了众多关于喊麦作品艺术性的分析，打算做一个tiny project来分析一下目前我所知道的喊麦作品集的常用字词。

- 生成高频词云
- 高频词柱状图
- 词频列表
  
### TODO

- 常用字嵌入向量，可视化
- 简单人为规则生成喊麦曲
- 基于机器学习生成喊麦曲（捂脸）
- 推广到仙侠修真小说范围
- 推广到女频小说范围QwQ
- 推广到各类小说范围

## 使用说明

### 2020-04-22 初版本说明

在src目录下打开命令行输入：

    python main.py

运行即可自动产生output目录并生成两张图和一个文档啦！

可在data文件夹中放入自己喜欢的utf-8编码的任何txt格式文本文件，**只支持中文**（跳过了所有ascii码在0-255的字符QwQ）。

test.jpg 为词云模版，可以替换成任何背景为白色、核心图像不为白色的图片。（应该是吧。。？）

# 欢迎大家来提建议和意见，喜欢的请务必一键三连支持卑微程序员QwQ