'''
chemkin therm.dat reformat code
'''
             
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    print('Cannot convert to float!')
    return False                
                

                
def format_e(n):
    if isfloat(n):
        n = float(n)
    a = '%E' % n
    decimal = len(a.split('E')[0].split('.')[1].rstrip('0'))
    return a.split('E')[0].rstrip('0') + '0'*(8-decimal)+ 'E' + a.split('E')[1]

#k = format_e(Decimal('3.86388918E+00'))
#a= '%E' % float('3.86388918E+00')
#print(a)
#print(k)
def find(s, ch):
    return [i for i, itr in enumerate(s) if itr == ch]
#print('find =',find('1.20499164E-8-2.18365931E-12', 'E')) 
    
def divideContinue(n):
    if isfloat(n):
        return n
    if len(n.split('E')) == 2:
        return n
    if len(n.split('E')) == 3:
        pos = find(n, 'E')[0]
        if n[pos+3]=='-':
            pos=pos+3
        if n[pos+4]=='-':
            pos=pos+4
        return [n[:pos], n[pos:]]
    else:
        print('long continue string!')
#    else:
#        pos = find(n, 'E')
#        for i in range(len(pos)):
#            
#            if pos[i]+3 <= len(n):
##                print(n[pos[i]+3])
#                if n[pos[i]+3] == '-': pos[i]=pos[i]+4
#                continue
#            if pos[i]+4 <= len(n):
##                print(n[pos[i]+4])
#                if n[pos[i]+4] == '-': pos[i]=pos[i]+4
#                continue
#        return splitByPos(n, pos)

#print(divideContinue('1.20499164E-8-2.18365931E-12'))
   

        
   
#
#a = np.array(find('1.20499164E-8-2.18365931E-12', 'E'))+4
#print('a= ', a)


#def splitByPos(s, indices):
#    indices = np.insert(indices, 0, 0)
#    print('indices = ', indices)
#    return [s[i:j] for i,j in zip(indices, indices[1:]+[-1])]

#print(splitByPos('1.20499164E-8-2.18365931E-12', a))



therm = r'befor-reformat-therm.dat'
content = []
s = ' '
with open(therm, 'r') as rf:
    content = rf.readlines()
    print(content[:15])
    
with open('new_therm.dat','w') as wf:
    for line in content:
        if line == '\n':
            continue
        if line[0] == '!':
            continue
        if 'THERMO' in line:
            wf.write('THERMO \n')
            continue
        if 'END' in line:
            wf.write('END \n')
            continue
        else:            
            strlist = line.strip().split()
            print('---------')
            print(strlist)          
            if len(strlist) == 3:            
                wf.write(3*s+strlist[0]+2*s+strlist[1]+2*s+strlist[2]+'\n')
            elif strlist[-1] == '1':
                interval1 = 25-len(strlist[1]+strlist[0])
                interval2 = 3
                
                last5 = strlist[-5]+3*s+ \
                        strlist[-4]+4*s+ \
                        strlist[-3]+4*s+ \
                        strlist[-2]+6*s+ \
                        strlist[-1]+ '\n'
                        
                element = len(strlist[:-5])
                print(element)
                if element == 3:
                    interval3 = 44-interval1-interval2-len(strlist[2]+strlist[1]+strlist[0]) 
                    wf.write(strlist[0]+ \
                             interval1*s + strlist[1] + \
                             interval2*s + strlist[2] +interval3*s)
                if element == 4:
                    interval4 = 40-interval1-interval2-len(strlist[2]+strlist[1]+strlist[0]) 
                    wf.write(strlist[0]+ \
                             interval1*s + strlist[1] + \
                             interval2*s + strlist[2] +3*s + strlist[3] + interval4*s)
                if element == 5:
                    interval5 = 35-interval1-interval2-len(strlist[2]+strlist[1]+strlist[0]) 
                    wf.write(strlist[0]+ \
                             interval1*s + strlist[1] + \
                             interval2*s + strlist[2] +3*s + strlist[3] + 3*s +strlist[4] + interval5*s)
                wf.write(last5)
#            elif strlist[-1] == '2' or strlist[-1] == '3':
            else:
                for x in strlist[:-1]:
                    print('x = ',x, type(x))
                    xlist = divideContinue(x)
                    print('xlist =', xlist)
#                    print(isinstance(xlist, list))
                    if isinstance(xlist, list):
                        for xx in xlist:
#                            print('xx =',xx)
#                            format_e(xx)
                            val = float(format_e(xx))
#                            print('val = ', val)
                            if val > 0.0:
                                wf.write(s + format_e(xx))
                            else:
                                wf.write(format_e(xx))
                    else:
#                         format_e(xlist)
                         val = float(format_e(xlist))
#                         print('val = ', val)
                         if val >= 0.0:
                             wf.write(s + format_e(xlist))
                         else:
                             wf.write(format_e(xlist))
                if strlist[-1] == '2' or strlist[-1] == '3':
                    wf.write(4*s + strlist[-1] + '\n')
                else:
                    wf.write(15*s + 4*s + strlist[-1] + '\n')
                    






