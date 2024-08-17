import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0', '15', '30', '45', '60', '75']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]


TaPD_ss=[31.22, 32.52, 31.997, 32.033, 31.977498, 31.22]

TaPS_ms = [19.59866, 20.0211, 20.207, 19.8380, 19.7739, 19.924]
MIB =[1332.5829 + 300, 1299.058+ 300, 1408.4009+ 300, 1319.058+ 300, 1399.058+ 300, 1359.058+ 300]




x = np.arange(len(labels))  # the label locations
width = 0.76 # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

plt.style.use('seaborn')
plt.figure(figsize=(6.5, 5.3))
#plt.subplots(figsize=(8, 5.3))
#plt.bar(x - width / 2 - width / 8 + width / 8, unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
plt.bar(x - width / 3, TaPD_ss,   width=width / 3, label='TaPD (SS)', color='#797BB7', edgecolor='black', hatch='*')
plt.bar(x , TaPS_ms, width=width / 3, label='TaPD (MS)', color='#9BC985',edgecolor='black', hatch='\\')
plt.bar(x + width / 3, MIB, width=width / 3, label='MIB', color='#E58579', edgecolor='black', hatch='/')
#plt.bar(x + width / 2 - width / 8 + width / 16, unl_hess_r, width=0.168, label='HBFU', color='orange', hatch='\\')



# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=24)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 1600.1, 400)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)
plt.legend(loc='upper left', fontsize=20)
plt.xlabel('Perturbation Limit' ,fontsize=20)
# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
plt.title("On CelebA", fontsize= 20)
plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('celebA_runningtime_noise_analysis_bar.pdf', format='pdf', dpi=200)
plt.show()
