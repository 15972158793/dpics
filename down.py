

#down http url images

#!/usr/bin/python
# _*_ coding: utf-8 _*_

import urllib
import urllib2
import re
import os

# set download url, record\\
localDir = "C:\\Users\\Administrator\\Desktop\\zp\\"


#set urls
urlList = [
"http://www.kangtairunye.cn/Public/Home/images_new/BJ.png",
"http://www.kangtairunye.cn/Public/Home/images_new/btn5.png",
"http://www.kangtairunye.cn/Public/Home/images_new/closebtn.png",
"http://www.kangtairunye.cn/Public/Home/images_new/cz2.png",
"http://www.kangtairunye.cn/Public/Home/images_new/dl2.png",
"http://www.kangtairunye.cn/Public/Home/images_new/qcz.png",
"http://www.kangtairunye.cn/Public/Home/images_new/sy2.png",
"http://www.kangtairunye.cn/Public/Home/images_new/wd2.png",
"http://www.kangtairunye.cn/Public/Home/images_new/zp1.png",
"http://www.kangtairunye.cn/Public/Home/images_new/zp2.png",
"http://www.kangtairunye.cn/Public/Home/images_new/zp3.png"
]


# for each list
for everyFile in urlList:
    everyURL = everyFile
    # url split
    localFileName = everyURL.split('/')[-1]
    localFile = localDir  +  localFileName
#     print (localFile)    # test strings

    # download path
    try:            
      urllib.urlretrieve(everyURL, localFile)
    except Exception,e: 
      continue