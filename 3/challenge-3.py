import re

with open('in-text.txt', 'r') as in_text:
    data = in_text.read().replace('\n','')

little_brothers = re.findall('(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', data)

print(''.join(little_brothers))