# Lists
list_lang = ['C#', 'Java', 'Python']
print(list_lang)

list_lang.append('PHP')
list_lang.remove('Java')
print('List: ' + ', '.join(list_lang))

for lang in list_lang:
    print("Language: " + lang)

for index, lang in enumerate(list_lang):
    print("Index: {0:d}, Language: {1:s}".format(index, lang))

# Tuples - can't change the value
tuple_lang = ('C#', 'Java', 'Python')
print('Tuple: ' + ', '.join(tuple_lang))

# Dictionaries
dic_lang = {'C#': '.NET language', 'C++': 'Native language', 'Python': 'Interpreted language'}
print(dic_lang)

dic_lang['PHP'] = 'Another interpreted language'
print(dic_lang)

print('C# is a ' + dic_lang['C#'])

del(dic_lang['PHP'])
if 'C#' in dic_lang:
    print('C# found!')
    del dic_lang['C#']
print(dic_lang)

removed = dic_lang.pop('PHP_NEW', None)

if removed is None:
    print('Not removed PHP_NEW')

removed = dic_lang.pop('C++', None)
print(dic_lang)

# iterate
dic_lang['Java'] = 'Java language'
for key, value in dic_lang.items():
    print(key + ': ' + value)
