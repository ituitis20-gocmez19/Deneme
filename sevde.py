
def var_mi_yok_mu(kelime):
    var_mi = False

    while(not var_mi): 
            inputt = raw_input(kelime + " var mi?")

            if (inputt == "yes" or inputt == "YES" or inputt == "Yes"):
                return True
            elif (inputt == "no" or inputt == "NO" or inputt == "No"):
                return False
            print("please enter yes or no")

def kac(kelime2):

    while (True):
        kac_yil = raw_input(kelime2)
        if (kac_yil.isdigit()):
            return int(kac_yil)

credit = 0

if (var_mi_yok_mu("ev")):
    credit += 5
if (var_mi_yok_mu("tel")):
    credit += 5
if (var_mi_yok_mu("mevduat")):
    credit += 5

yil1 = kac("ayni konut kac yil?")
if (yil1 > 1):
    if (yil1 > 4):
        credit += 5
    else:
        credit += 3

yil2 = kac("ayni is kac yil?")
if (yil2 > 1):
    if (yil2 > 4):
        credit += 5
    else:
        credit += 3

if (not var_mi_yok_mu("borc")):
    credit += 10
else:
    borc = kac("borcunuz kac?")
    gelir = kac("Geliriniz kac")

    if (borc < (gelir / 100) *  5):
        credit += 5
    elif (borc > (gelir / 100) * 25):
        credit -= 10

print(credit)