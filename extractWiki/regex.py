import re

""""
print("merged-file.txt:")
fh = open('merged-file.txt','r').read()
unique_chars1 = set(fh)
unique_chars1 = sorted(unique_chars1)
print(len(unique_chars1))
print(unique_chars1)

print("input:")
fh = open('input.txt','r').read()
unique_chars2 = set(fh)
unique_chars2 = sorted(unique_chars2)
print(len(unique_chars2))
print(unique_chars2)

print("Remove:")
l3 = [x for x in unique_chars1 if x not in unique_chars2]
print(l3)

"""
with open('new_file.txt', 'w') as f:
    f.write("")

i = 0
unique_chars = set()
whitelist = set(' !"#\'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÄäÖÜßöü')
with open('input.txt','r') as myfile:
    for line in myfile:
        if i%10000 == 0:
            print('line:',i)
        i = i + 1
        line = re.sub(r'“', '"', line)
        line = re.sub(r'\\', '', line)
        line = re.sub(r'„', '"', line)
        line = re.sub(r'<[\S]*>', '', line)
        line = re.sub(r'<[\S, ]*>', '###', line)
        answer = ''.join(filter(whitelist.__contains__, line))
        if len(answer) > 0:
            answer = answer + '\n'
            unique_chars = set(list(unique_chars) + list(set(answer)))
            with open('new_file.txt', 'a') as f:
                f.write(answer)
print(sorted(unique_chars))
unique_chars_text = ''.join(sorted(unique_chars))
print('in set:',unique_chars_text)
whitelist.add('\n')
whitelist_text = ''.join(sorted(whitelist))
print('whitelist:',whitelist_text)
mybool = whitelist_text == unique_chars_text
print('all chars in set:', mybool)
