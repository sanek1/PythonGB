
vilositi = int(input('please enter a speed: '))
distnce = int(input('please enter a distance: '))


res = distnce// vilositi
remaind = distnce%vilositi
if remaind != 0 :
    res +=1


print(f'n={vilositi}, m ={distnce} -> {res}')