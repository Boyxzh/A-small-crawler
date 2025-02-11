
import requests
import re                                                                   # 导入re模块

from playsound import playsound
from bs4 import BeautifulSoup
from docx import Document                                      # 导入Document模块
from docx.shared import Pt



print('需要一首音乐？\n')

while True:
    # try:
    answer = input('请回答需要或不需要\n')
    if answer == '需要':
        print('1.飘向北方，2.等什么君，3.白羊\n')
        music = int(input('请选择一首歌,输入对应序号\n'))
        if music == 1:
            print('已播放')
            playsound('飘向北方.mp3')
        elif music == 2:
            print('已播放')
            playsound('等什么君.mp3')
            break
        elif music == 3:
            print('已播放')
            playsound('白羊.mp3')
            break
        else:
            print('请输入正确序号')

    elif answer == '不需要':
        break

    else:
        print('请输入正确回答')
        continue



