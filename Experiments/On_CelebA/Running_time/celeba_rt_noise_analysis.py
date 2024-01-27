

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5, 6]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['0', '0.2', '0.4', '0.6', '0.8', '1']
# unl_org = [97.77, 97.55, 97.35, 97.29, 97.21, 97.21]

unl_mib_ss = [0, 0, 0, 0, 0, 0]
unl_mib_ms = [1332.5829 + 300, 1299.058+ 300, 1408.4009+ 300, 1319.058+ 300, 1399.058+ 300, 1359.058+ 300]

# unl_hess_r = [96.6, 96.66, 96.04, 95.94, 95.85, 97.21]
unl_muv = [31.22, 32.52, 31.997, 32.033, 31.977498, 31.22]

unl_muv_ms = [19.59866, 20.0211, 20.207, 19.8380, 19.7739, 19.924] #[191.235, 191.2713, 193.1833, 190.910802, 191.14087, 224]
# unl_ss_wo = [94.32, 94.53, 94.78, 93.38, 94.04, 97.21]

for i in range(len(x)):
    unl_mib_ss[i] = unl_mib_ss[i]/1000
    unl_mib_ms[i] = unl_mib_ms[i]/1000
    unl_muv[i] = unl_muv[i] / 1000
    unl_muv_ms[i] = unl_muv_ms[i]/1000

plt.style.use('seaborn')
plt.figure(figsize=(5.5, 5.3))
l_w=5
m_s=15
marker_s = 3
markevery=1
#plt.figure(figsize=(8, 5.3))
#plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=l_w, markersize=m_s)
# plt.plot(x, unl_muv_includes, linestyle='-', color='b', marker='o', fillstyle='none', markevery=markevery,
#          label='MUV (SS)', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

plt.plot(x, unl_muv, linestyle='-', color='#797BB7', marker='o', fillstyle='full', markevery=markevery,
         label='UEV (SS)', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

#plt.plot(x, unl_ss_w, color='g',  marker='*',  label='PriMU$_{w}$',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_muv_ms, linestyle='--', color='#9BC985',  marker='s', fillstyle='full', markevery=markevery,
         label='UEV (MS)',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

# plt.plot(x, unl_mib, linestyle='-.', color='k',  marker='D', fillstyle='none', markevery=markevery,
#          label='MIB (SS-B)',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)



# plt.plot(x, unl_mib_ss, linestyle='-.', color='#2A5522',  marker='D', fillstyle='full', markevery=markevery,
#          label='MIB (SS-B)',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)


plt.plot(x, unl_mib_ms, linestyle=':', color='#E07B54',  marker='^', fillstyle='full', markevery=markevery,
         label='MIB (MS-B)', linewidth=l_w,  markersize=m_s, markeredgewidth=marker_s)





#plt.plot(x, unl_vibu, color='silver',  marker='d',  label='VIBU',linewidth=4,  markersize=10)

# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Running Time' ,fontsize=24)
my_y_ticks = np.arange(0, 1.5, 0.2)
plt.yticks(my_y_ticks,fontsize=20)
plt.xlabel('Noise Ratio' ,fontsize=20)

plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')

plt.annotate(r"1e3", xy=(0.1, 1.01), xycoords='axes fraction', xytext=(-10, 10),
             textcoords='offset points', ha='right', va='center', fontsize=15)


# plt.title('(c) Utility Preservation', fontsize=24)
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('celeba_running_time_noise_analysis.pdf', format='pdf', dpi=200)
plt.show()