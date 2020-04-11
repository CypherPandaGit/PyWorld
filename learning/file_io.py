txt = open('ipsum.txt', 'r')

for line in txt:
    if 'bc' in line.lower():
        print(line, end=' ')

txt.close()
