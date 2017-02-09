def index():
    """
    sąrašas
    """
    sarasas = db().select( db.finansai.ALL );
    
    # Create
    form_create = FORM( 
            INPUT(_name='kiek'),
            INPUT(_name='uz_ka'),
            INPUT(_value='ok', _type="submit"),
            _action = URL('prideti') 
       )   
       
    return CAT( form_create, sarasas )


def prideti():
    
    kiek = int(request.vars.kiek)
    
    db.finansai.insert( kiek = kiek, 
                        uz_ka = request.vars.uz_ka 
                        )
                          
