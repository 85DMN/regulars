import csv
import re

with open('phonebook_raw.csv', encoding='utf=8') as f:
    rows = csv.reader(f,delimiter=',')
    contacts_list = list(rows)

nev_var = []
for j in contacts_list:
    sbor = []
    for z,f in enumerate(j):
        if f == '':
            if z>3:
                sbor.append(f)
            else:
                if z+1>len(sbor):
                    sbor.append(f)
                else: continue
        else:
            if z<3:
                sbor.extend(f.split(' '))
            else:
                sbor.append(f)
    nev_var.append(sbor)
final_var = []
vhg = []
phn = []
for s,j in enumerate(nev_var):
    if s not in vhg:
        for z,h in enumerate(nev_var[s+1:]):
            if j[:2]==h[:2]:
                if s+z+1 in vhg:
                    continue
                else:
                    for zz in range(len(j)):
                        if h[zz]==j[zz]:continue
                        else: 
                            if h[zz]=='' and j[zz]!='':
                                continue
                            else:j[zz]=h[zz]
                vhg.append(s+z+1)
    else: 
        vhg.append(s)
        continue
    
    if len(j)<7:
        j.append('')
    final_var.append(j)
  
regex = r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})\s*(\w*)'
zmn = r"+7(\2)\3-\4-\5 \6"
zz=[]
for d,g in enumerate(final_var):
    mes = re.sub(regex, zmn, str(g[-2]))
    final_var[d][-2]=mes

with open('phonebook.csv','w+', encoding='utf=8') as f:
    rows_d = csv.writer(f)
    rows_d.writerows(final_var)
print('__finish__')