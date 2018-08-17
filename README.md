# Markdown-Picture-loopback
一个Markdown实用工具

### 自动化实现流程：
- 从剪贴板获取截图并保存在本地
- 上传本地图片并返回链接 
- 粘贴链接为markdown格式

### 具体实现请看 `upload_get.py` 文件

准备工作
- 我们需要先安装第三方库，这里我给出一个脚本文件，运行能直接安装学习
python所需要的大多数库，具体请看 `library_installation.py` 文件
- 截图工具
  这里我推荐[snipaste](https://zh.snipaste.com/),下载之后F1直接截图
- 我们还可以安装剪贴板工具,便于排查错误.(网上随便下一个就行)

### 使用过程
- F1截图并复制
- 打开 `upload_get.py` 文件并运行，修改其中一些东西，文件中注释详细说明
- Ctrl+V 粘贴即可

### demo GIF

![](https://res.cloudinary.com/dc15efw34/image/upload/v1534466014/8.17/demo.gif)