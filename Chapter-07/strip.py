import re

char_to_be_removed = " "
input_str = "   Hey I am Swayam   "

pattern = re.compile(r'^[\s' + re.escape(char_to_be_removed) + r']+|[\s' + re.escape(char_to_be_removed) + r']+$')
result = re.sub(pattern, '', input_str)

print(result)

