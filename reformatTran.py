'''
chemkin tran.dat reformat code
'''

tran = r'before-reformat-tran.dat'
content = []
s = ' '
with open(tran, 'r') as rf:
    content = rf.readlines()
    print(content[:15])
    
with open('new_tran.dat','w') as wf:
    for line in content:
        if line == '\n':
            continue
        if line[0] == '!':
            continue
        else:            
            strlist = line.strip().split()
            if len(strlist) < 7:
                continue
            else:
                for n in range(len(strlist[2:])):
                    strlist[2+n] = str('{:.3f}'.format(float(strlist[2+n])))
                interval1 = 19 - len(strlist[0])
                interval2 = 10 - len(strlist[2])
                interval3 = 10 - len(strlist[3])
                interval4 = 10 - len(strlist[4])
                interval5 = 10 - len(strlist[5])
                interval6 = 10 - len(strlist[6])
                wf.write(strlist[0] + interval1*s + \
                         strlist[1] + interval2*s + \
                         strlist[2] + interval3*s + \
                         strlist[3] + interval4*s + \
                         strlist[4] + interval5*s + \
                         strlist[5] + interval6*s + \
                         strlist[6] + '\n')
    
    wf.write('END')            