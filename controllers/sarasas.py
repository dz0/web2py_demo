# -*- coding: utf-8 -*-

def index():
    """
    sąrašas
    """
    if not session.sarasas:
        session.sarasas = []

    # Create
    form = FORM( 
            INPUT(_name='skaicius'),
            # INPUT(_name='nr'),
       )   

    
    sar2 = []
    for nr, sk in enumerate( session.sarasas ):
        # Read, Update
        form_read_update = FORM( 
            INPUT( _name="skaicius", _value=sk ) , 
            INPUT( _name="nr", _value=nr, _type="hidden" ) , 
            _action = URL('redaguoti')  
        )
        
        # Delete
        form_delete = FORM( 
                INPUT( _name="nr", _value=nr, _type="hidden" ), 
                INPUT( _type="submit", _value="del") ,
               _action = URL('trinti')  
        )
        
        sar2 . append ( CAT(form_read_update, form_delete) )
    
    return CAT(form,  UL(sar2), request.vars ) 

def trinti():
    # Delete 
    if  request.vars.nr  :
        nr = int(request.vars.nr) 
        del session.sarasas[nr]
        print "deleting", nr
        
    redirect ( URL ('index') )

def redaguoti():
    # Update
    if  request.vars.nr  and request.vars.skaicius :
        nr = int(request.vars.nr) 
        skaicius = int(request.vars.skaicius) 
        session.sarasas[nr] = skaicius
        print "updating", nr, "to", skaicius 
        
    redirect ( URL ('index') )


def prideti():
    if request.vars.skaicius:
        skaicius = int(request.vars.skaicius)
        session.sarasas.append( skaicius )    
        print "creating element", skaicius 
        
    redirect ( URL ('index') )
