import matplotlib.pyplot as plt
import math

x = 0       #x er antall minutter
xverdier = [] #tid/min som starter på 13:41 som er x-verdi 0
yverdier = [369.15,350.15,347.15,346.65,343.25,340.35,337.85,
            335.25,333.25,331.55,329.75,328.55,326.95,325.55,
            324.25,322.75,322.05,321.05,320.05,319.25,318.25,
            314.35,311.45,309.05,306.75,304.95,301.15,298.75,
            296.05] #temperatur som er målt, omgjort til K


while x <= 20:
    xverdier.append(x)
    x = x + 1                   #antall minutter mellom hver måling
    
while x <= 45 and x >= 20:
    xverdier.append(x)
    x = x + 5                   #antall minutter mellom hver måling
    
while x <= 90 and x >= 45:
    xverdier.append(x)
    x = x + 15                  #antall minutter mellom hver måling

print(f"x-verider: {xverdier}")
print(f"y-verdier: {yverdier}")

y_teoretiske_verdier= []

def T(x):
    return 35.904*(math.exp(-1.129*x))+295

for i in range(len(xverdier)):
    y = T(xverdier[i])
    print(T(xverdier[i]))
    y_teoretiske_verdier.append(y)
    
print(y_teoretiske_verdier)


plt.plot(xverdier,yverdier, label="T(x) målinger")
plt.plot(xverdier,y_teoretiske_verdier, label="T(x) teoretisk")
plt.legend()
plt.grid()
plt.show()
