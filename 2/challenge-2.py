import re

with open('in-text.txt', 'r') as in_text:
    data = in_text.read().replace('\n','')

special_chars = re.findall('[A-Za-z0-9]', data)

print(''.join(special_chars))