eng2sp = dict()
print(eng2sp)

eng2sp["one"] = "uno"
print(eng2sp)

eng2sp = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco",
    "six": "seis",
    "seven": "siete",
    "eight": "ocho",
    "nine": "nueve",
    "ten": "diez",
}
print(eng2sp["two"])

# Operador IN

print("uno"in eng2sp)

# Selecionar valore

valores = eng2sp.values()
print("one" in valores)