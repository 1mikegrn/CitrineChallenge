import mpl_toolkits.mplot3d.axis3d as axis3d

from matplotlib import pyplot as plt

def dim3(report_values):
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter(report_values[:,2], report_values[:,1],report_values[:,0])
    plt.show()

def dim2(report_values):

    pass
