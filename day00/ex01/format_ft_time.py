import time
import datetime


#need to do : add 4chiffre apres la virgule, ajouter date d,ajd et une notation 10 puissance
num = time.time()
print("Seconds since January 1, 1970:", f'{num :,.4f}', "or", f'{num:.2e}', "in scientific notation")
print(time.strftime("%b %d %Y"))