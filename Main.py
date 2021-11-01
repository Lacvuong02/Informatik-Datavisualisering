import matplotlib.pyplot as plt
import csv
  
a = []
b = []
c = []
d = []
e = []
  
with open('activity-export-DailyStep_Calle_Studieturv2.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        a.append(row[0])
        b.append(int(row[1]))
        c.append(int(row[2]))
        d.append(bool(row[3]))
        e.append(int(row[4]))
  
plt.plot(a, b, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Skridt på studietur")

plt.plot(c, color = 'r', linestyle = 'dashed',
         marker = 'o',label = "Varighed i sekunder")
  
plt.plot(d, color = 'y', linestyle = 'dashed',
         marker = 'o',label = "Afstand i meter") 

plt.plot(e, color = 'b', linestyle = 'dashed',
         marker = 'o',label = "Kalorier i kcal") 

plt.xticks(rotation = 25)
plt.xlabel('Dato')
plt.ylabel('Skridt')
plt.title('Data gennem studieturen', fontsize = 20)
plt.grid()
plt.legend()
plt.show()