import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['1', '20', '40', '60', '80', '100']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]



unl_muv_MNIST = [141.4497, 116.9057  , 118.2206 , 119.850, 118.458, 116.92136]
unl_mib_MNIST = [986.6597 , 1011.42  , 988.6431 , 988.9856858, 1002, 999]

unl_muv_CIFAR = [133.75, 111.596  , 114.632 , 112.850, 109.458, 110.83 ]
unl_mib_CIFAR = [986.6597 , 1011.42  , 988.6431 , 988.9856858, 1002, 999]

unl_muv_CelebA = [32.3621, 23.749 , 21.41661, 22.37170, 21.5619, 23.5819]
unl_mib_CelebA = [1232.582, 1131.4467 , 1225.5774, 1250.929, 1227.0406, 1205.699]



for i in range(len(labels)):
    unl_muv_MNIST[i] = unl_muv_MNIST[i]/1000
    unl_mib_MNIST[i] = unl_mib_MNIST[i] / 1000
    unl_muv_CIFAR[i] = unl_muv_CIFAR[i]/1000
    unl_mib_CIFAR[i] = unl_mib_CIFAR[i] / 1000
    unl_muv_CelebA[i] = unl_muv_CelebA[i]/1000
    unl_mib_CelebA[i] = unl_mib_CelebA[i] / 1000


x = np.arange(len(labels))  # the label locations
width = 0.9 # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

plt.style.use('seaborn')
plt.figure()
#plt.subplots(figsize=(8, 5.3))
plt.bar(x - width /6 - width / 6 , unl_muv_MNIST, width=width/6, label='UEV MNIST', color='#C6B3D3', edgecolor='black', hatch='/')

plt.bar(x - width / 6 , unl_muv_CIFAR, width=width/6,  label='UEV CIFAR10', color='#F7D58B', edgecolor='black' , hatch='x')
plt.bar(x , unl_muv_CelebA, width=width/6, label='UEV CelebA', color='#80BA8A', edgecolor='black', hatch='o')


plt.bar(x + width / 6  , unl_mib_MNIST,   width=width/6, label='MIB MNIST', color='#9CD1C8', edgecolor='black',  hatch='-')

plt.bar(x + width / 6 + width/6 , unl_mib_CIFAR, width=width/6, label='MIB CIFAR10', color='#6BB7CA', edgecolor='black', hatch='*')


plt.bar(x + width / 6 + width / 6 + width/6  , unl_mib_CelebA,   width=width/6, label='MIB CelebA', color='#E58579', edgecolor='black', hatch='\\')
# plt.bar(x - width / 8 - width / 16, unl_vib, width=0.168, label='PriMU$_{w}$', color='cornflowerblue', hatch='*')
# plt.bar(x + width / 8, unl_self_r, width=0.168, label='PriMU$_{w/o}$', color='g', hatch='x')
# plt.bar(x + width / 2 - width / 8 + width / 16, unl_hess_r, width=0.168, label='HBFU', color='orange', hatch='\\')


# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 1.25, 0.2)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)
# plt.grid(axis='y')
# plt.legend(loc='upper left', fontsize=20)
plt.legend( title = 'Methods and Datasets',frameon=True, facecolor='white', loc='best',
           ncol=2, mode="expand", framealpha=0.5, borderaxespad=0., fontsize=20, title_fontsize=20)


plt.xlabel('$\it{ESS}$' ,fontsize=20)
# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('mnist_rt_sample_size_bar.pdf', format='pdf', dpi=200)
plt.show()
