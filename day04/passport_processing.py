f = open('input.txt', 'r')
input = f.read()
input = input.split('\n\n') # Remove empty lines

# Remove line breaks, clean data
input_clean = []
for i in input:
    j = i.replace('\n', ' ')
    for item in j:
        k = j.split(' ')
    input_clean.append(k)

valid_count = 0
for item in input_clean:
    if len(item) == 8:
        valid_count += 1
    elif len(item) == 7 and not any('cid' in i for i in item):
        valid_count += 1
    else:
        pass

print(valid_count)