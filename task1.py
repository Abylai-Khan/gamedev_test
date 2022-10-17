1-Вариант 
text = input().lower()
ready_text = ''

for i in text:
	if text.count(i) == 1 or i == ')':
		ready_text += '('
	else: 
		ready_text += ')'
print(ready_text)


2-Вариант 
inp = input().lower()
inp2 = inp
dic = []
for letter in inp:
    if letter not in dic:
        if inp.count(letter) == 1:
            inp = inp.replace(letter, '(')
        else:
            inp = inp.replace(letter, ')')
    else:
        inp = inp.replace(letter, ')')
    dic.append(letter)
print(inp)