s = '/users/altairbuilds_ati6/2021.2/dev/2021.2.0.23-santoskSDS-2465_hwJson-dev2/rahulpan/rahulpandevsantoskSDS-2465_hwJson-dev2'
s = s.rsplit('/',2)
installdir = s[0].replace('altairbuilds_ati6','qa_installs6')
#print(installdir)

s2 = '/trisilon-cifs.prog.altair.com/qa_installs6/2021.2/dev/2021.2.0.23-santoskSDS-2465_hwJson-dev2'
s2 = s2.replace('/','\\\\')
#print(s2)

l = ['\t//altair/dev/ati/fb/branchtillbvt/tests/hw/bvt/','\t//altair/dev/mview/fb/21/bfsa2/tests/hw/bvt/mview/... //SDS2482Motion/hwdesktop/bvt/mview/...', '\t+//altair/dev/mauto/fb/21/bfsa2/tests/hw/bvt/mauto/... //SDS2482Motion/hwdesktop/bvt/mauto/...']
temp = ''
s3 = '\t+//altair/dev/mview/fb/21/bfsa2/tests/hw/bvt/mview/'
for line in l:
    print('Original Line : ',line.strip())
    if not line.strip().startswith("+"):
        line = line.replace('//altair', '+//altair')
        print('line  with + sign in the starting :', line)
    else:    
        print('line starts with plus')
#print('bvt : ',temp)    
