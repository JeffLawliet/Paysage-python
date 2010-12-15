def dessineLune(diametre,x,y):
    
    aller(x,y,0)
    
    begin_fill()
    color('#fffaa2')
    circle(diametre/2)
    end_fill()
    
    aller((27*diametre/50)+x,(27*diametre/50)+y,90)
    
    begin_fill()
    color('#06011d')
    circle(diametre/3)
    end_fill()
    
    aller(x,y,0)
