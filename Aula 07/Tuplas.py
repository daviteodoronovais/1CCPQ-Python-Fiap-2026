t = ('a', 'b', 'c', 'd', 'e')

print(t)
print(type(t))
print(t[0])

t1 = ('a',)
print(t1)
print()

t2 = tuple('fiap')
print(t2)
print(t2[1:3])

t2 = ('F',) + t2[1:]
print(t2)
print()

# Atribuição com tuplas

a = 5
b = 10

print(f"a: {a}, b: {b}")

temp = a
a = b
b = temp
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")
print()

enderecoEmail = "fulano@gmail.com"
usuario, dominio = enderecoEmail.split("@")
print(usuario)
print(dominio)