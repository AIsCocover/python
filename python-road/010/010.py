#! E:\codeprojects\python\pythonEveryDay\010
# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string

def randomChar() :                                                                                                          # 随机字符 a~z A~Z 0~9
    dictionary = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return random.choice(dictionary)

def randomColor1() :                                                                                                        # 随机颜色1
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def randomColor2() :                                                                                                        # 随机颜色2
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

width = 60 * 4                                                                                                                 # 图片大小
height = 60 
image = Image.new('RGB', (width, height), (255, 255, 255))                                                # 图片格式
font = ImageFont.truetype('Roboto-Black.ttf', 36)                                                            # 字体格式
draw = ImageDraw.Draw(image)                                                                                        # 绘制图片

for x in range(width) :
    for y in range(height) :
        draw.point( (x, y), fill=randomColor1() )                                                                     # 填充像素点

for t in range(4) :
    draw.text( (60*t+10, 10), randomChar(), font=font, fill=randomColor2() )                        # 绘制字符

image = image.filter(ImageFilter.BLUR)                                                                             # 模糊处理
image.save('vertification code.jpg','jpeg')                                                                          # 保存图片为ipeg格式
