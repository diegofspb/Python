print('#'*30)
print(' '*10,'Tabuada')
print('#'*30)
print('\n')

for numero1 in range(1,10,1):
    for numero2 in range(1,11,1):
        print(f'{numero1} x {numero2} =',numero1*numero2)
    print('\n','<->'*10,'\n')