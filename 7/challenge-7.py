from PIL import Image
import re

oxygen = Image.open("oxygen.png").convert('L')

values = []

for i in range((oxygen.width - 14) // 7):
    values.append(oxygen.getpixel((i*7, 47)))

result = ''.join(chr(i) for i in values)

print(result)

numArray = re.findall(r'(\d{2,3})(?=,|])', result)

print(''.join(chr(int(i)) for i in numArray))