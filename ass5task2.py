num=[]
for i in range(1,11):
    num.append(i)
print(f'original list:{num}')
forward=num[0:5]
print(f'extracted first five elements:{forward}')
forward.reverse()
print(f'extracted last five elements:{forward}')
input("press enter to exit")