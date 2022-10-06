def conta_frases(f):
'''A função retorna a quantidade de frases depois do referêncial: (.),(!),(?),(...)'''
     
    t= f.split('?')
    f= '.'.join(t)
    
    t= f.split('!')
    f= '.'.join(t)
    
    t= f.split('...')
    f= '.'.join(t)
    
    return len(f.split('.'))-1
