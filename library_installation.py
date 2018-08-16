# 这是一个安装第三方库的脚本，几乎都是学习python过程需要的,可以直接运行脚本全部安装
# 如果已经安装过cos-python-sdk-v5的请升级到最新版本
# 使用  pip install -U cos-python-sdk-v5 # 其中 u 代表 update
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame",\
        'pywin32','pyperclip','pillow','iamge','dateime','cos-python-sdk-v5'}
try:
    for lib in libs:
        os.system("pip install "+lib)
    print("Successful")
except:
    print("Failed Somehow")
