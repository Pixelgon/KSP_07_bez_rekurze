# -----------------------------------------------------------
# KSP 07 bez rekurze
# Vytvoril Matej Matejka
# -----------------------------------------------------------

# Nacteme cisla
origin = open("01.in", "r")
out = open("01.txt", "w")
numA = int(origin.readline())
numB = int(origin.readline())
origin.close()
# Nejvetsi spolecny delitel, ktery deli obe cisla beze zbytku
def greatest_div(nA, nB):
    # Nacteme mensi cislo do promnene last
    if nA > nB:
        last = nB
    else:
        last = nA
    div = 1
    # Pro i od 2 do last + 1
    for i in range(2, last+1):
        # Pokud i deli nA a nB beze zbytku
        if nA % i == 0 and nB % i == 0:
            div = i
    return div

# Nejmensi spolecny nasobek
def least_multiple(nA, nB):
    # Nacteme vetsi cislo do promene greater
    if nA > nB:
        greater = nA
    else:
        greater = nB

# Dokud plati, ze nA a nB je delitelem greater
    while True:
        if greater % nA == 0 and greater % nB == 0:
            multiple = greater
            break
        greater += 1
    return multiple

# Printneme odpovedi
print("Největší společný dělitel:", greatest_div(numA, numB))
print("Nejmenší společný násobek:", least_multiple(numA, numB))

# Zapiseme odpovedi do souboru
out.write(str(greatest_div(numA, numB)) + '\n' + str(least_multiple(numA, numB)))
out.close()
