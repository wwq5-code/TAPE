import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0', '15', '30', '45', '60', '75']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]


TaPD_ss=[79.81,79.676,79.6397, 79.556,  79.56, 79.54 ]

TaPS_ms = [74.90623, 74.560, 74.602, 74.621145, 74.545, 74.60]
MIB = [815.331, 815.710, 815.9786, 815.55814719, 815.45873, 815]


x = np.arange(len(labels))  # the label locations
width = 0.76 # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

plt.style.use('seaborn')
plt.figure(figsize=(6.5, 5.3))
#plt.subplots(figsize=(8, 5.3))
#plt.bar(x - width / 2 - width / 8 + width / 8, unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
plt.bar(x - width / 3, TaPD_ss,   width=width / 3, label='TAPE (SS)', color='#797BB7', edgecolor='black', hatch='*')
plt.bar(x , TaPS_ms, width=width / 3, label='TAPE (MS)', color='#9BC985',edgecolor='black', hatch='\\')
plt.bar(x + width / 3, MIB, width=width / 3, label='MIB (B-MS)', color='#E58579', edgecolor='black', hatch='/')
#plt.bar(x + width / 2 - width / 8 + width / 16, unl_hess_r, width=0.168, label='HBFU', color='orange', hatch='\\')



# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=24)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 1200.1, 200)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)
plt.legend(loc=(0.01, 0.68), fontsize=20)
plt.xlabel('Perturbation Limit' ,fontsize=22)
# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
plt.title("On STL-10", fontsize= 24)
plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('stl10_rt_noise_analysis_bar.pdf', format='pdf', dpi=200)
plt.show()
