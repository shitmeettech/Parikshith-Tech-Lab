name=input('enter ur name')
total=0
for i in range(3):
    hrs=float(input(f'enter the number of hrs u studied in day{i+1}'))
    total= total + hrs
print(name)
print(total)
if total>=7:
    print("excellent")
elif total>=5:
    print('very good')
else:
    print('good')
