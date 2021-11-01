import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('activity-export-DailyStep_Calle_Studietur.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Weather Data")
  
plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()

import matplotlib.backends.backend_pdfimport 
matplotlib.pyplot as pltimport randomdef chunks(l, n):    
"""Yield successive n-sized chunks from l."""    
for i in range(0, len(l), n):        yield l[i:i + n]# settingsout_pdf = r'C:\GeoNet\Profiles2PDF\test3.pdf'# some random datadata = []for i in range(0, 5000):    data.append([i, float(i + random.randrange(-50, 50))/100, 5])pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)cnt = 0figs = plt.figure()for data_chunk in chunks(data, 600):    plot_num = 321    fig = plt.figure(figsize=(10, 10)) # inches    for sub_chunk in chunks(data_chunk, 100):        cnt += 1        d = [a[0] for a in sub_chunk]        z = [a[1] for a in sub_chunk]        zv = [a[2] for a in sub_chunk]        print plot_num        plt.subplot(plot_num)        # plot profile, define styles        plt.plot(d,z,'r',linewidth=0.75)        plt.plot(d,z,'ro',alpha=0.3, markersize=3)        plt.plot(d,zv,'k--',linewidth=0.5)        plt.xlabel('Distance from start')        plt.ylabel('Elevation')        plt.title('Profile {0} using Python matplotlib'.format(cnt))        # change font size        plt.rcParams.update({'font.size': 8})        plot_num += 1    pdf.savefig(fig)pdf.close()‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍