# Edinburgh Postnatal Depression Scale (EDPS)

# quetions
question1 = 'Ich konnte lachen und die komische Seite des Lebens sehen:'
question2 = 'Ich habe mich auf Dinge gefreut:'
question3 = 'Ich habe mir die Schuld gegeben, wenn etwas schief gelaufen ist:'
question4 = 'Ich war grundlos ängstlich oder besorgt:'
question5 = 'Ich hatte Angst oder Panik ohne richtigen Grund:'
question6 = 'Mir ist alles zu viel geworden:'
question7 = 'Ich war so unglücklich, dass ich Schlafprobleme hatte:'
question8 = 'Ich fühlte mich müde oder elend:'
question9 = 'Ich war so unglücklich, dass ich geweint habe:'
question10 = 'Ich habe daran gedacht, mir etwas anzutun:'

# answers
answer1a = 'So wie immer'
answer1b = 'Nicht ganz so wie sonst'
answer1c = 'Eindeutig nicht so wie sonst'
answer1d = 'Gar nicht'

answer2a = answer1a
answer2b = 'Eher weniger als sonst'
answer2c = 'Auf jeden Fall weniger'
answer2d = 'Fast gar nicht'

answer3a = 'Ja, meistens'
answer3b = 'Ja, manchmal'
answer3c = 'Nicht sehr oft'
answer3d = 'Nein, nie'

answer4a = 'Nein, gar nicht'
answer4b = 'Fast nie'
answer4c = 'Ja, manchmal'
answer4d = 'Ja, sehr oft'

answer5a = 'Ja, ziemlich oft'
answer5b = answer3b
answer5c = 'Nein, nicht oft'
answer5d = answer4a

answer6a = 'Ja, die meiste Zeit bin ich überhaupt nicht zurechtgekommen'
answer6b = 'Ja, manchmal bin ich nicht so gut zurechtgekommen wie sonst'
answer6c = 'Nein, die meiste Zeit bin ich gut zurechtgekommen'
answer6d = 'Nein, ich bin so gut zurechtgekommen wie immer'

answer7a = answer3a
answer7b = answer3b
answer7c = 'Nein, nicht sehr oft'
answer7d = answer4a

answer8a = answer3a
answer8b = answer5a
answer8c = 'Nein, nicht sehr oft'
answer8d = answer5d

answer9a = answer3a
answer9b = answer5a
answer9c = 'Nur gelegentlich'
answer9d = 'Nein, nie'

answer10a = answer5a
answer10b = 'Manchmal'
answer10c = 'Fast nie'
answer10d = 'Nie'

# Convert the 0 into a number so we can add scores
score = 0
score = int(score)

# Ask user for their name
name = input("Wie heißen Sie?\n")
name = name.title()
print("""\nHallo {}, Sie haben kürzlich ein Baby bekommen. 
Wir möchten wissen, wie Sie sich fühlen.
Bitte geben Sie jeweils die Antwort (a,b,c oder d), die Ihren Gefühlen 
in den vergangenen sieben Tagen am nächsten kommt, nicht nur wie Sie sich heute fühlen.
Vielen Dank.""".format(name))

# Question1
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question1, answer1a, answer1b, answer1c, answer1d))

response1 = input("Ihre Antwort lautet : ")

if response1 == answer1a or response1 == 'a':
    score = score
elif response1 == answer1b or response1 == 'b':
    score = score + 1
elif response1 == answer1c or response1 == 'c':
    score = score + 2
elif response1 == answer1d or response1 == 'd':
    score = score + 3
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question2
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question2, answer2a, answer2b, answer2c, answer2d))

response2 = input("Ihre Antwort lautet : ")

if response2 == answer2a or response2 == 'a':
    score = score
elif response2 == answer2b or response2 == 'b':
    score = score + 1
elif response2 == answer2c or response2 == 'c':
    score = score + 2
elif response2 == answer2d or response2 == 'd':
    score = score + 3
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question3
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question3, answer3a, answer3b, answer3c, answer3d))

response3 = input("Ihre Antwort lautet : ")

if response3 == answer3a or response3 == 'a':
    score = score + 3
elif response3 == answer3b or response3 == 'b':
    score = score + 2
elif response3 == answer3c or response3 == 'c':
    score = score + 1
elif response3 == answer3d or response3 == 'd':
    score = score
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question4
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question4, answer4a, answer4b, answer4c, answer4d))

response4 = input("Ihre Antwort lautet : ")

if response4 == answer4a or response4 == 'a':
    score = score
elif response4 == answer4b or response4 == 'b':
    score = score + 1
elif response4 == answer4c or response4 == 'c':
    score = score + 2
elif response4 == answer4d or response4 == 'd':
    score = score + 3
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question5
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question5, answer5a, answer5b, answer5c, answer5d))

response5 = input("Ihre Antwort lautet : ")

if response5 == answer5a or response5 == 'a':
    score = score + 3
elif response5 == answer5b or response5 == 'b':
    score = score + 2
elif response5 == answer5c or response5 == 'c':
    score = score + 1
elif response5 == answer5d or response5 == 'd':
    score = score
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question6
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question6, answer6a, answer6b, answer6c, answer6d))

response6 = input("Ihre Antwort lautet :")

if response6 == answer6a or response6 == 'a':
    score = score + 3
elif response6 == answer6b or response6 == 'b':
    score = score + 2
elif response6 == answer6c or response6 == 'c':
    score = score + 1
elif response6 == answer6d or response6 == 'd':
    score = score
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question7
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question7, answer7a, answer7b, answer7c, answer7d))

response7 = input("Ihre Antwort lautet :")

if response7 == answer7a or response7 == 'a':
    score = score + 3
elif response7 == answer7b or response7 == 'b':
    score = score + 2
elif response7 == answer7c or response7 == 'c':
    score = score + 1
elif response7 == answer7d or response7 == 'd':
    score = score
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question8
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question8, answer8a, answer8b, answer8c, answer8d))

response8 = input("Ihre Antwort lautet :")

if response8 == answer8a or response8 == 'a':
    score = score + 3
elif response8 == answer8b or response8 == 'b':
    score = score + 2
elif response8 == answer8c or response8 == 'c':
    score = score + 1
elif response8 == answer8d or response8 == 'd':
    score = score
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question9
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question9, answer9a, answer9b, answer9c, answer9d))

response9 = input("Ihre Antwort lautet :")

if response9 == answer9a or response9 == 'a':
    score = score + 3
elif response9 == answer9b or response9 == 'b':
    score = score + 2
elif response9 == answer9c or response9 == 'c':
    score = score + 1
elif response9 == answer9d or response9 == 'd':
    score = score
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

# Question10
print("""\n{} \na. {}\nb. {}\nc. {}\nd. {}\n""".format(question10, answer10a, answer10b, answer10c, answer10d))

response10 = input("Ihre Antwort lautet :")

if response10 == answer10a or response10 == 'a':
    score = score + 3
elif response10 == answer10b or response10 == 'b':
    score = score + 2
elif response10 == answer10c or response10 == 'c':
    score = score + 1
elif response10 == answer10d or response10 == 'd':
    score = score
else:
    print('Ups. Da ist wohl ein Fehler passiert. Bitte geben Sie eine der Antwortmöglichkeiten an.\n')

print("\nSie haben einen Gesamtscore von " + str(score) + " Punkten.")

if score <= 9:
    print("Die Wahrscheinlichkeit für eine Depression ist gering.")
elif score > 9 and score <= 12:
    print("Die Wahrscheinlichkeit für eine Depression ist mäßig vorhanden.")
elif score >= 13:
    print("Die Wahrscheinlichkeit für eine Depression ist hoch.\nBitte kontaktieren Sie ihre Hebamme.")
else:
    print("Fehlermeldung: Bitte Entwickler Bescheid geben.")

print("Vielen Dank für ihre Teilnahme, {}.".format(name))
