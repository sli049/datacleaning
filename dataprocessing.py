import numpy as np
class procs:

	def __init__(self, filenm):
		self.idx = np.fromfile(filenm, dtype=long)
		self.size = self.idx.size

class data_procs:
	def __init__(self, filenm):
		self.data = np.fromfile(filenm, dtype=float)

test = procs('m000.full.mpicosmo.100#21-id.dat')
hacc = data_procs('m000.full.mpicosmo.100#21-id.dat')
hacc1 = data_procs('m000.full.mpicosmo.102#21-id.dat')
hacc2 = data_procs('m000.full.mpicosmo.105#21-id.dat')
hacc3 = data_procs('m000.full.mpicosmo.107#21-id.dat')
hacc4 = data_procs('m000.full.mpicosmo.110#21-id.dat')
hacc5 = data_procs('m000.full.mpicosmo.113#21-id.dat')
test1 = procs('m000.full.mpicosmo.102#21-id.dat')
test2 = procs('m000.full.mpicosmo.105#21-id.dat')
test3 = procs('m000.full.mpicosmo.107#21-id.dat')
test4 = procs('m000.full.mpicosmo.110#21-id.dat')
test5 = procs('m000.full.mpicosmo.113#21-id.dat')

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
for i in range(itsct.size):
	comid = itsct[i];
	cldata0.extend(haccarr[(idarr[0].idx).index(comid)])
	cldata1.extend(haccarr[(idarr[1].idx).index(comid)])
	cldata2.extend(haccarr[(idarr[2].idx).index(comid)])
	cldata3.extend(haccarr[(idarr[3].idx).index(comid)])
	cldata4.extend(haccarr[(idarr[4].idx).index(comid)])
	cldata5.extend(haccarr[(idarr[5].idx).index(comid)])
print(itsct.size)
print(cldata0.size)
print(cldata1.size)
print(cldata2.size)
print(cldata3.size)
print(cldata4.size)
print(cldata5.szie)
