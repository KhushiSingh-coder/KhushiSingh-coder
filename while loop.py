#for

l = ['USA','UK','INDIA','China','Nepal']
print(l)

for i in l:
    print(i)
print('---------------------------------')
for i in l:
    if i =='China':
        break
    print(i)

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
for i in l:
    if i =='China':
        continue
    print(i)



for i in range(20):
    if i%2==0:
        print(i,'This is even Number')
    else:
        print(i,'This is odd number')




for i in range(20):
    if i==10:
        break
    print(i,'This is even Number')



for i in range(12,121,12):
    print(i)

#While

i=0
while i<10:
    print(i)
    i+=1