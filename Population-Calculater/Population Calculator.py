yıl = int (input("Kaç yıl sonra: "))
birth = (365 * 24 * 60 * 60) / 7
death = (365 * 24 * 60 * 60) / 13
immigrant = (365 * 24 * 60 * 60) / 35
population = round(yıl * (329466236 + (immigrant + birth) - (death)))
print(population)
