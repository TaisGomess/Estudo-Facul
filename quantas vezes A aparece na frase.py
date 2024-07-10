frase = input("Digite uma frase: ")
contador_a = 0

for letra in frase:
  if letra == "a" or letra == "A":
    contador_a += 1

# vai contar quantos A tem numa frase ou texto#

print(f"A letra 'a' aparece {contador_a} vezes na frase.")
