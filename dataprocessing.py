import numpy as np
class procs:
    def __init__(self, filenm):
		self.idx = np.fromfile(filenm, dtype=np.int64)
		self.size = self.idx.size

class data_procs:
	def __init__(self, filenm):
		self.data = np.fromfile(filenm, dtype=np.float)
        #self.size = self.data.size

test = procs('m000.full.mpicosmo.100#21-id.dat')
hacc = data_procs('m000.full.mpicosmo.100#21-4.dat')
hacc1 = data_procs('m000.full.mpicosmo.102#21-4.dat')
hacc2 = data_procs('m000.full.mpicosmo.105#21-4.dat')
hacc3 = data_procs('m000.full.mpicosmo.107#21-4.dat')
hacc4 = data_procs('m000.full.mpicosmo.110#21-4.dat')
hacc5 = data_procs('m000.full.mpicosmo.113#21-4.dat')
test1 = procs('m000.full.mpicosmo.102#21-id.dat')
test2 = procs('m000.full.mpicosmo.105#21-id.dat')
test3 = procs('m000.full.mpicosmo.107#21-id.dat')
test4 = procs('m000.full.mpicosmo.110#21-id.dat')
test5 = procs('m000.full.mpicosmo.113#21-id.dat')



print(test.size)
print(hacc.data.size)
print(test1.size)
print(hacc1.data.size)
print(test2.size)
print(hacc2.data.size)
print(test3.size)
print(hacc3.data.size)
print(test4.size)
print(hacc4.data.size)
print(test5.size)
print(hacc5.data.size)
idarr = [test, test1, test2, test3, test4, test5]
haccarr = [hacc, hacc1, hacc2, hacc3, hacc4, hacc5]

#print(idarr)
print(idarr[3].idx)
print(haccarr[3].data)
itsct = np.intersect1d(idarr[0].idx, idarr[1].idx)
for i in range(4):
	itsct = np.intersect1d(itsct, idarr[i+2].idx)

print(itsct)
cldata0 = []
cldata1 = []
cldata2 = []
cldata3 = []
cldata4 = []
cldata5 = []

clid = np.zeros((6, itsct.size), np.int64)
cldata = np.zeros((6, itsct.size), np.float)

for i in range(6):
    sorter = np.argsort(idarr[i].idx)
    clid[i,:] = sorter[np.searchsorted(idarr[i].idx, itsct, sorter=sorter)]
    cldata[i,:] = [haccarr[i].data[x] for x in clid[i,:]]

#cldata = np.zeros((6, itsct.size), np.float)
#for i

#sorter = np.argsort(idarr[0])


#for i in range(itsct.size):
#	comid = itsct[i];
#	cldata0.extend(haccarr[(idarr[0].idx).index(comid)])
#	cldata1.extend(haccarr[(idarr[1].idx).index(comid)])
#	cldata2.extend(haccarr[(idarr[2].idx).index(comid)])
#	cldata3.extend(haccarr[(idarr[3].idx).index(comid)])
#	cldata4.extend(haccarr[(idarr[4].idx).index(comid)])
#	cldata5.extend(haccarr[(idarr[5].idx).index(comid)])
print(itsct.size)
#print(cldata0.size)
#print(cldata1.size)
#print(cldata2.size)
#print(cldata3.size)
#print(cldata4.size)
#print(cldata5.szie)

sum1 = 0
for i in range(6):
    sum1+=idarr[i].size;

sum1 = sum1/6.0
stayratio = itsct.size/sum1
print(stayratio)


for i in range(6):
    flname = "alignedoutput"+str(i)+".dat"
    cldata[i,:].tofile(flname)
