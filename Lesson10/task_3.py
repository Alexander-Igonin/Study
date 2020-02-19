'''
Дан словарь ключами которого являются английские слова, а занчениями - списки латинских слов.
Необходимо развеннуть словарь.
Другими словани, необходимо, на основании заданного словаря, создать новый словарь, у которого в качестве ключей будут
 взяты латинские слова, из первого словаря, а значениями будут, соответствующие им, английские слова.
d = {
    	'apple': ['malum', 'pomum', 'popula'],
    	'fruit': ['baca', 'bacca', 'popum'],
    	'punishment': ['malum', 'multa']
}
'''



d = {
    	'apple': ['malum', 'pomum', 'popula'],
    	'fruit': ['baca', 'bacca', 'popum'],
    	'punishment': ['malum', 'multa']
}

new_d = {}
lst_keys = list(dict.fromkeys(d))

for i in range(len(d)):
	for _ in d[lst_keys[i]]:
		new_d[_] = lst_keys[i]

print(new_d)

