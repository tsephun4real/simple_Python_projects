#write a program to create a dictionary containing names of competition winnner students as keys
# and number of their wins as values

zahl_schueler=int(input("wie viele teilnehmer gibt es?: "))
wett_gewinner={}
for schu in range(zahl_schueler):
    key=input("wie heisst der Teinehmer?: ")
    value=int(input("wie viel hat er/sie gewonnen?: "))
    wett_gewinner[key]=value

print("the dictionary now is: ")
print(wett_gewinner)
print(key,"hat den ersten Platz mit Gewinnzahl",max(wett_gewinner[key]))