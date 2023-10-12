numbers = list(range(1,10))
print(numbers)

print (str("pular linha"))

numbers_2 = list(range(2,11,2))
print(numbers_2)
#O valor 2 é somado repetidamente até o valor final, que é 11, ser alcançado ou ultrapassado, e  
#o resultado a seguir é gerado: [2, 4, 6, 8, 10] 

print (str("pular linha"))
squares = []
for value in range (1,11):
    squares.append(value**2)
    print(squares)
    
#Meno número em uma lista:

digits=[1,2,3,4,5,6,7,8,9,0]
print (min(digits))
print(max(digits))
print(sum(digits))

print(str("Exercicio 1"))

numbers_3= list(range(1,21))
print(numbers_3)

print("Exercicio 2")

numbers_4= list(range(1,1000001))
print (min(numbers_4))
print(max(numbers_4))
print(sum(numbers_4))

print("Exercicio 3")

numbers_impares=list(range(1,20,2))
print(numbers_impares)

print("Exercicio 4")

laco_for=[value for value in range (1,1000001)]
print(min(laco_for))
print(max(laco_for))
print(sum(laco_for))

print("Exercicio 5")

exercicio5=[value for value in range (1,20,2)]
print(exercicio5)

print("Exercicio 6")

ex6=[value for value in range (0,30,3)]
print(ex6)

print("Exercicio 7 Cubo")
ex7=[value **3 for value in range (1,10)]
print(ex7)
