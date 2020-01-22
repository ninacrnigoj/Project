import math
import xml.etree.ElementTree as ET
import time 
import subprocess


# Podatki
R = 6371 #Radij Zemlje

##########################################################################
#TOČKA A

#Zapis geografske širine (s)

zapis_s_A = input("Podaj geografsko širino točke A (s m sek):")
razdeli_s_A = zapis_s_A.split()  #razdeli glede presledkov

s_s_A = float(razdeli_s_A[0])
m_s_A = float(razdeli_s_A[1])
sek_s_A = float(razdeli_s_A[2])

# Zapis geografske dolžine (d)

zapis_d_A = input("Podaj geografsko dolžino točke A (s m sek):")
razdeli_d_A = zapis_d_A.split()  #razdeli glede presledkov

s_d_A = float(razdeli_d_A[0])
m_d_A = float(razdeli_d_A[1])
sek_d_A = float(razdeli_d_A[2])

# Izpis Fi in Lambda točke A
Fi_A = math.radians(s_s_A + m_s_A/60 + sek_s_A/3600)
Lambda_A = math.radians(s_d_A + m_d_A/60 + sek_d_A/3600)

# koordinate točk
x1 = (s_s_A + m_s_A/60 + sek_s_A/3600)
x2 = (s_d_A + m_d_A/60 + sek_d_A/3600)

##########################################################################
#TOČKA B

#Zapis geografske širine (s)

zapis_s_B = input("Podaj geografsko širino točke B (s m sek):")
razdeli_s_B = zapis_s_B.split()  #razdeli glede presledkov

s_s_B = float(razdeli_s_B[0])
m_s_B = float(razdeli_s_B[1])
sek_s_B = float(razdeli_s_B[2])

# Zapis geografske dolžine (d)

zapis_d_B = input("Podaj geografsko dolžino točke B (s m sek):")
razdeli_d_B = zapis_d_B.split()  #razdeli glede presledkov

s_d_B = float(razdeli_d_B[0])
m_d_B = float(razdeli_d_B[1])
sek_d_B = float(razdeli_d_B[2])

# Izpis Fi in Lambda točke B
Fi_B = math.radians(s_s_B + m_s_B/60 + sek_s_B/3600)
Lambda_B = math.radians(s_d_B + m_d_B/60 + sek_d_B/3600)

y1 = (s_s_B + m_s_B/60 + sek_s_B/3600)
y2 = (s_d_B + m_d_B/60 + sek_d_B/3600)


# Višina

z1 = 0
z2 = 0

##########################################################################

Delta_Lambda = abs(Lambda_A-Lambda_B)
Delta_Lambda_x = (Lambda_A+Lambda_B)/2

# Azimut loksodrome
stevec = math.tan(math.radians(45)+(Fi_B/2))
imenovalec = math.tan(math.radians(45)+Fi_A/2);
Leva_stran = float(1/Delta_Lambda * math.log(stevec/imenovalec));
Azimut = math.atan(1/Leva_stran);
Azimut_2_kvadrant = Azimut + math.pi;
D_loks_km = abs((R)*(Fi_B-Fi_A)/math.cos(Azimut_2_kvadrant))

print('Dolžina loksodrome: ', D_loks_km,' m')

##########################################################################

sx1 = str(x1) +","
sy1 = str(y1) +","
sz1 = str(z1) +" "

sx2 = str(x2) +","
sy2 = str(y2) +","
sz2 = str(z2) +" "



if y2 >0:
    sy2p = y2+0.2
else:
    sy2p = y2-0.2

if y1 >0:
    sy1p = y1+0.2
else:
    sy1p = y1-0.2

if x2 >0:
    sx2p = x2+0.2
else:
    sx2p = x2-0.2

if x1 >0:
    sx1p = x1+0.2
else:
    sx1p = x1-0.2


sy2pp = str(sy2p) +","
sy1pp = str(sy1p) +","
sx2pp = str(sx2p) +","
sx1pp = str(sx1p) +","


podatek = sx2 + sx1 + sz2 + sy2 + sy1 + sz1 + sy2pp + sy1pp +sz2 + sx2pp + sx1pp + sz1



##########################################################################

tree = ET.parse('LoksXML.kml')
root = tree.getroot()



root[0][2][3][1][0][0].text = podatek

tree.write("output.kml")

##########################################################################
time.sleep (5)
subprocess.call(["C:/Program Files/Google/Google Earth Pro/client/googleearth.exe", "C:/Users/Nina/Desktop/Projekt/output.kml"])







