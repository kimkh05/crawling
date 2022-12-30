import matplotlib.pylab as plt
import numpy as np

job_title: str = ["Frontend", "Backend", "Android", "IOS", "OS", "Embedded", "Full-stack", "AI"]
c = []
for k, v in job.items():
  c.append(v)

cv = np.array(c)
x = np.arange(len(c))
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', "#A1B5DC", "#B6B6B6", "#3EAF0E", "#79DAE0"]
wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
plt.pie(cv, labels=job_title, autopct='%.1f%%', counterclock=False, startangle=260, colors=colors, wedgeprops=wedgeprops)

plt.title("Developers")
plt.show() 

plt.bar(x, c)
plt.xticks(x, job_title, rotation=45)
plt.title("Developers")
plt.show()