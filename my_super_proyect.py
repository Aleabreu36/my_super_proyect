print('\nVälkommen till spelet sten-sax-påse')

# Testa ja/nej
svar=input('Är du redo att spela? (ja/nej"): ')
score=0
total_questions=3

if svar.lower()=='ja':
# Skriv ok
   svar=input('Reglerna är enkla: ')
if svar.lower()=='nej':
   svar=input('fel svar: ')

# Skriv ok
dator = input("Ange ett val (sten, sax eller påse): ")

Spel = {
    'spelaren': 'Jag',
    'enhet': "datorn"
}
print(Spel['spelaren'] + " ska spela mot " + (Spel['enhet']))

import random

mojliga_atgarder = ["sten", "sax", "påse"]
datorn_atgarder = random.choice(mojliga_atgarder)

# Datorn slumpar vilken av sten, sax eller påse den ska välja.
print(f"\ndatorn valde {datorn_atgarder}.\n")

# Spelaren väljer också sten, sax eller påse.
spelaren_atgerder = datorn_atgarder
if spelaren_atgerder == datorn_atgarder:
    print(f"spelaren valde {spelaren_atgerder}. Så det är oavgjort!")


# Datorn och spelaren visar sedan upp sina val samtidigt.

datorn_atgarder = random.choice(mojliga_atgarder)
print(f"\ndatorn visar {datorn_atgarder}, spelaren {spelaren_atgerder}.\n")

# Reglerna är enligt följande: sten vinner över sax, sax vinner över påse,
# och påse vinner över sten. Om båda väljer samma alternativ blir det oavgjort.

# Spelaren spelar tills hen vinner eller förlorar mot datorn.
class atgarder:
    sten = ""
    påse = ""
    sax = ""
atgarder.sten = "sten"
atgarder.påse = "påse"
atgarder.sax = "sax"

# Välj vinnaren
if spelaren_atgerder == datorn_atgarder:
    print(f"Det är avgjord,\nSpela en gång till")
elif spelaren_atgerder == atgarder.sten:
    if datorn_atgarder == atgarder.sax:
        print("sten vinner över sax! Spelaren vinner!")
    else:
        print("påse vinner över sten! Spelaren förlorar.")
elif spelaren_atgerder == atgarder.påse:
    if datorn_atgarder == atgarder.sten:
        print("påse vinner över sten! Spelaren vinner!")
    else:
        print("sax vinner över påse! Spelaren förlorar.")
elif spelaren_atgerder == atgarder.sax:
    if datorn_atgarder == atgarder.påse:
        print("sax vinner över påse! Spelaren vinner!")
    else:
        print("sten vinner över sax! Spelaren förlorar.")

