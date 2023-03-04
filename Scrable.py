latters_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}

word = input().upper()

li =[]

for i in word:
    for key, value in latters_en.items():
        if i in value:
            li.append(key)
print(sum(li))

latters_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}

word = input().upper()

li =[]

for i in word:
    for key, value in latters_ru.items():
        if i in value:
            li.append(key)
print(sum(li))