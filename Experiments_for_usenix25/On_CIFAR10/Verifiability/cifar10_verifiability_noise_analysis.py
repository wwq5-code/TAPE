

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5, 6]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['0', '5', '10', '15', '20', '25']
# unl_org = [97.77, 97.55, 97.35, 97.29, 97.21, 97.21]
unl_mib = [0, 0, 0, 0, 0, 0]
unl_mib_bck = [0, 0.5, 0.5, 1, 1, 1]


# unl_hess_r = [96.6, 96.66, 96.04, 95.94, 95.85, 97.21]
unl_muv_includes = [0.50, 0.8280, 0.9020, 0.9372, 0.9596, 0.98764]

unl_muv = [0.40, 0.5788, 0.7352, 0.8268, 0.9420, 0.974468]
# unl_ss_wo = [94.32, 94.53, 94.78, 93.38, 94.04, 97.21]

plt.style.use('seaborn')
plt.figure(figsize=(6.5, 5.3))
l_w=5
m_s=15
marker_s = 3
markevery=1
#plt.figure(figsize=(8, 5.3))
#plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_muv_includes, linestyle='-', color='#797BB7', marker='o', fillstyle='full', markevery=markevery,
         label='TAPE (SS)', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

#plt.plot(x, unl_ss_w, color='g',  marker='*',  label='PriMU$_{w}$',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_muv, linestyle='--', color='#9BC985',  marker='s', fillstyle='full', markevery=markevery,
         label='TAPE (MS)',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

plt.plot(x, unl_mib, linestyle='-.', color='#2A5522',  marker='D', fillstyle='full', markevery=markevery,
         label='MIB (B-SS)',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)


plt.plot(x, unl_mib_bck, linestyle=':', color='#E07B54',  marker='^', fillstyle='full', markevery=markevery,
         label='MIB (B-MS)', linewidth=l_w,  markersize=m_s, markeredgewidth=marker_s)





#plt.plot(x, unl_vibu, color='silver',  marker='d',  label='VIBU',linewidth=4,  markersize=10)

# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Verifiability' ,fontsize=24)
my_y_ticks = np.arange(0, 1.1, 0.2)
plt.yticks(my_y_ticks,fontsize=20)
plt.xlabel('Perturbation Limit' ,fontsize=24)

plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')

#plt.annotate(r"1e0", xy=(0.1, 1.01), xycoords='axes fraction', xytext=(-10, 10),textcoords='offset points', ha='right', va='center', fontsize=15)


# plt.title('On CIFAR10', fontsize=24)
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar10_verifiability_noise_analysis.pdf', format='pdf', dpi=200)
plt.show()