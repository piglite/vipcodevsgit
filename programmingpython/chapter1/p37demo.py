bob = {'name':'Bob Smith','age':24,'pay':6000,'job':'dev'}
sue = {'name':'Sue Jones','age':32,'pay':15000,'job':'hdw'}
tom = {'name':'Tom Pages','age':36,'pay':26000,'job':'mgr'}

import pickle
for (k,v) in [('bob',bob),('sue',sue),('tom',tom)]:
    filewriter = open(k + '.pkl','wb')
    pickle.dump(v,filewriter)
    filewriter.close()

import glob
for filename in glob.glob('*.pkl'):
    reader = open(filename,'rb')
    value = pickle.load(reader)
    print(filename,'==>',value)
    reader.close()
    
