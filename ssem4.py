#50-100 хүртэл тоон утга бүхий нэг хэмжээст массив
import numpy as np
x=np.arange(50,101)
print(x)


#Арван ширхэг 1, арван ширхэг 0, арван ширхэг 6 тоо бүхий нэг хэмжээст массив
x=np.repeat(1,10)
y=np.repeat(0,10)
z=np.repeat(6,10)
print(np.concatenate([x,y,z]))


#20-32 хүртэл тоон утга бүхий 3x4 хэмжээтэй массив
import numpy as np
x=np.arange(20,32)
a=np.reshape(x, (3,4), 'F')
print(a)



#Диагональ нь 1-ийн тоо, бусад нь 0 байх 3x3 хэмжээтэй массив
import numpy as np
ar = np.array([1, 1, 1])
res = np.diag(ar)
print(res)


#Диагональ нь 1-5 хүртэл тоо, бусад нь 0 байх 5х5 хэмжээтэй массив
import numpy as np
ar = np.array([1,2,3,4,5])
res = np.diag(ar)
print(res)


import numpy as np
mass=np.array([[9,8,7],[4,5,6]])
print("нийт нийлбэр:", mass.sum())
print("баганын дагуух нийлбэр:", mass.sum(axis=0))
print("мөрийн дагуух нийлбэр:", mass.sum(axis=1))



import numpy as np

#Salaries
PauloDybala_Salary = [717557,800704,4785167,5808621,13867908,13912783,13567342,14908661,15890551,16970114]
LionellMessi_Salary = [23491345,33971002,42065102,75012667,73081672,78901335,80913631,76135012,64509137,60664137]
CristianoRonaldo_Salary = [36901775,32861308,31859114,38071778,61085771,65081629,60761344,70147891,60715371,60644400]
MohamedSalah_Salary = [3713640,4694041,3041250,4410581,5779912,12149243,13518574,12450000,12407474,12458000]
KarimBenzema_Salary = [11493160,15806720,15061274,17758000,17202590,19647180,18091770,18536360,17513178,19436271]
HarryKane_Salary = [348000,3235220,3455000,6410581, 4779912,6500000,6022500,12545000,12067500,12644400]
Neymar_Salary = [13144240,12380160,19615960,14574189,33520500,40940153,46359805,57779458,58668431,60068563]
LukaModric_Salary = [9044813,8671363,8171200,8484040,15796880,16053663,15506632,20669630,20832627,20995624]
AntoineGriezmann_Salary = [1051774,5113656,7508704,8822800,23184480,49546160,36993708,36402500,27632688,28862875]
WayneRooney_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]

Salary = np.array([PauloDybala_Salary, LionellMessi_Salary, CristianoRonaldo_Salary, MohamedSalah_Salary, KarimBenzema_Salary, HarryKane_Salary, Neymar_Salary, LukaModric_Salary, AntoineGriezmann_Salary, WayneRooney_Salary])

print("цалингийн баганын дагуух нийлбэр:", Salary.sum(axis=0))
print("цалингийн мөрийн дагуух нийлбэр:", Salary.sum(axis=1))

#Games 
PauloDybala_G = [33,43,40,29,35,32,37,40,36,45]
LionellMessi_G = [52,34,55,32,44,45,39,40,41,45]
CristianoRonaldo_G = [50,55,45,61,46,39,42,36,37,29]
MohamedSalah_G = [40,33,37,26,34,27,25,17,37,20]
KarimBenzema_G = [32,12,22,46,32,28,34,16,31,29]
HarryKane_G = [30,29,37,37,40,17,37,24,39,34]
Neymar_G = [18,34,40,28,35,40,20,40,22,42]
LukaModric_G = [35,35,20,24,22,28,26,21,31,17]
AntoineGriezmann_G = [20,20,21,24,33,13,31,30,40,35]
WayneRooney_G = [32,30,21,29,27,26,39,29,24,22]

Games = np.array([PauloDybala_G, LionellMessi_G, CristianoRonaldo_G, MohamedSalah_G, KarimBenzema_G, HarryKane_G, Neymar_G, LukaModric_G, AntoineGriezmann_G, WayneRooney_G])

print("тоглолтын баганын дагуух нийлбэр:", Games.sum(axis=0))
print("тоглолтын мөрийн дагуух нийлбэр:", Games.sum(axis=1))

#Goals
PauloDybala_PTS = [24,25,25,29,20,36,33,29,38,28]
LionellMessi_PTS = [54,45,55,49,40,56,43,39,28,32]
CristianoRonaldo_PTS = [50,65,55,59,60,45,33,29,32,30]
MohamedSalah_PTS = [34,44,42,32,20,26,33,34,35,29]
KarimBenzema_PTS = [43,23,52,24,41,35,32,42,32,24]
HarryKane_PTS = [16,34,24,35,41,50,23,35,46,30]
Neymar_PTS = [34,44,36,44,42,54,30,39,24,40]
LukaModric_PTS = [40,24,53,43,44,53,34,35,35,29]
AntoineGriezmann_PTS = [38,45,52,35,45,35,41,36,30,42]
WayneRooney_PTS = [33,47,50,41,40,34,44,29,30,29]

Points = np.array([PauloDybala_PTS, LionellMessi_PTS, CristianoRonaldo_PTS, MohamedSalah_PTS, KarimBenzema_PTS, HarryKane_PTS, Neymar_PTS, LukaModric_PTS, AntoineGriezmann_PTS, WayneRooney_PTS])
                  
print("гоалын баганын дагуух нийлбэр:", Points.sum(axis=0))
print("гоалын мөрийн дагуух нийлбэр:", Points.sum(axis=1))
