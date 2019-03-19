# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError
from PIL import ImageGrab

import datetime
import os
import sys
import logging
import pyperclip #复制字符串到剪贴板
import win32clipboard 
import win32con


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括secret_id, secret_key, region
# appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
secret_id = '******'     # 替换为你自己的secret_id
secret_key = '******'     # 替换你自己的secret_key
region = 'ap-chengdu'    # 替换为你的的region
token = None               # 使用临时秘钥需要传入Token，默认为空,可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)

# 保存截图到本地
# 使用时间戳来命名文件
now = datetime.datetime.now()
t = now.strftime("%Y%m%d%H%M%S")
image_name=str(t) +'.png' # 保存图片命名
print (image_name)
save_path='D:\\image\\'+image_name # 保存图片的地址
get_image = ImageGrab.grabclipboard()
get_image.save(save_path)

# 上传文件
response1 = client.upload_file(
    Bucket='graph-bed-1256708472',# 修改为你自己的存储桶ID
    LocalFilePath=save_path,
    Key=image_name,
    PartSize=10,
    MAXThread=10
)
# 复制图片链接(推荐第一种)
# - 使用https://graph-bed-1256708472.cos.ap-chengdu.myqcloud.com+'文件名' //其中的网址你上传一张图片，复制链接应该就看得到
# - 使用官方获取方法
r = '![]('+'https://graph-bed-1256708472.cos.ap-chengdu.myqcloud.com/'+image_name+')'
# response2 = client.get_presigned_download_url(
#    Bucket='graph-bed-1256708472',# 修改为你自己的存储桶ID
#    Key=image_name
# )
# r='![]('+response2+')'

# 复制链接字符串到剪贴板
pyperclip.copy(r)
spam = pyperclip.paste()

