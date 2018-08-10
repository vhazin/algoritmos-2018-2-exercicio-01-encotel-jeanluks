frase = input("Digite uma frase: ").strip().upper()
num = ""
for c in range(len(frase)):
    if frase[c] == "A" or frase[c] == "B" or frase[c] == "C":
        num+= "2"
    elif frase[c] == "D" or frase[c] == "E" or frase[c] == "F":
        num+= "3"
    elif frase[c] == "G" or frase[c] == "H" or frase[c] == "I":
        num+= "4"
    elif frase[c] == "J" or frase[c] == "K" or frase[c] == "L":
        num+= "5"
    elif frase[c] == "M" or frase[c] == "N" or frase[c] == "O":
        num+= "6"
    elif frase[c] == "P" or frase[c] == "Q" or frase[c] == "R" or frase[c] == "S":
        num+= "7"
    elif frase[c] == "T" or frase[c] == "U" or frase[c] == "V":
        num+= "8"
    elif frase[c] == "W" or frase[c] == "X" or frase[c] == "Y" or frase[c] == "Z":
        num+= "9"
    elif frase[c] == "-":
        num +="-"
        print(frase)
print(num)