import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0', '5', '10', '15', '20', '25']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]


TaPD_ss=[143, 220.52 - 77, 221.997 - 77, 211.033 - 77, 201.977498 - 77, 220.22- 77]

TaPS_ms = [116.90, 119.52, 118.997, 116.033, 116.977498, 117.22]
MIB =[988.985 -370-3, 1016.633-370-2, 988.6431-370-3, 986.6597-370-1, 988.985-370-1, 988.985-370-2]


unl_mib_ss = [988.985 -370-3, 1016.633-370-2, 988.6431-370-3, 986.6597-370-1, 988.985-370-1, 988.985-370-2]
unl_mib_ms = [988.985 -370, 1016.633-370, 988.6431-370, 986.6597-370, 988.985-370, 988.985-370]

# unl_hess_r = [96.6, 96.66, 96.04, 95.94, 95.85, 97.21]
unl_muv_ms = [116.90, 119.52, 118.997, 116.033, 116.977498, 117.22]

unl_muv = [143, 220.52 - 77, 221.997 - 77, 211.033 - 77, 201.977498 - 77, 220.22- 77] #[191.235, 191.2713, 193.1833, 190.910802, 191.14087, 224]
# unl_ss_wo = [94.32, 94.53, 94.78, 93.38, 94.04, 97.21]

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

my_y_ticks = np.arange(0, 1000.1, 200)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)
plt.legend(loc='upper left', fontsize=20)
plt.xlabel('Perturbation Limit' ,fontsize=24)
# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
plt.title("On MNIST", fontsize= 24)
plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('mnist_runningtime_noise_analysis_bar.pdf', format='pdf', dpi=200)
plt.show()
