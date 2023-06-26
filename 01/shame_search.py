import sys

BASE_URL = 'https://www.youtube.com/results?search_query='
VALUES = []
NEW_URL = [BASE_URL]

for i,j in enumerate(sys.argv):
    if i > 0:
        VALUES.append(j)

values_plus = '+'.join(VALUES)
NEW_URL.append(values_plus)
y = ''.join(NEW_URL)
print(y)


