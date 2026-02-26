file_input, file_output = [x for x in input().split()]

with open(f"{file_input}", 'r', encoding='utf-8') as text_file:
    text = text_file.read()
    temp = []
    for elem in text:
        if not ((65 <= ord(elem) <= 90) or (97 <= ord(elem) <= 122)):
            if elem not in temp:
                temp.append(elem)
        elif 97 <= ord(elem) <= 122:
            text = text.replace(elem, chr(ord(elem) - 32))
    for err in temp:
        text = text.replace(err, ' ')
    text = text.split()
    text = ''.join(text)
    print(text)

with open(f"{file_output}", 'w') as output:
    output.write(text)