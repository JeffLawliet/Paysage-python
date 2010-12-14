def dessineLune(diametre,x,y):
    
    aller(x,y,0)
    
    fill(True)
    color('#fffaa2')
    circle(diametre/2)
    fill(False)
    
    aller((27*diametre/50)+x,(27*diametre/50)+y,90)
    
    fill(True)
    color('#06011d')
    circle(diametre/3)
    fill(False)
    
    aller(x,y,0)
