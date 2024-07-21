import alignment
import csv
import numpy


path0 = "/Users/rexzhou/Downloads/data/simphy-"
path = []
for i in (10, 25, 50):
    for j in (100000, 500000, 1000000, 5000000, 10000000):
        path.append(path0 + str(i) + "tax-1000gen-" + str(j) + "su/")
        

def write_phy_csv(path, file_num):
    
    if file_num < 10:
        path1 = path + "0" + str(file_num) + "/"
    else:
        path1 = path + str(file_num) + "/"
        
    pd1 = [0] * 1001
    for i in range(1,10):
        dir1 = path1 + "g_trees" + "000" + str(i) + "_TRUE.phy"
        a = alignment.read_phylip(dir1)
        pd1[i] = a.summarize_p_distances()
    for i in range(10,100):
        dir1 = path1 + "g_trees" + "00" + str(i) + "_TRUE.phy"
        a = alignment.read_phylip(dir1)
        pd1[i] = a.summarize_p_distances()
    for i in range(100,1000):
        dir1 = path1 + "g_trees" + "0" + str(i) + "_TRUE.phy"
        a = alignment.read_phylip(dir1)
        pd1[i] = a.summarize_p_distances()

    pd1[1000] = alignment.read_phylip(path1 + "g_trees" + str(1000) + "_TRUE.phy").summarize_p_distances()
    pd1 = pd1[1:]
    return pd1

pd = []


for i in range(15):
    for j in range(1,16):
        pd.append(write_phy_csv(path[i], j))
    mean = [[0] *4]* 15
    for k in range(15):
        mean[k] = numpy.mean(pd[k], axis=0).tolist()
    with open('mean-pd-' + str(i) + ".csv", 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data = [['hmin_mean', 'hmax_mean', 'havg_mean','hstd_mean']] + mean
        a.writerows(data)
