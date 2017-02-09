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
   
                          
# SQLFORM   http://www.web2pyref.com/reference/sqlform-web2pys-high-level-api-form

def sqlform_create():
    form = SQLFORM( db.finansai )
    form.process()  # pritaiko  request.vars   lentelei --> form.vars, 
                    # bei  įterpia įrašą

    return CAT( form,  form.vars )
    
    

def sqlform_update():
    # http://localhost:8002/demo/db/sqlform_update/2
    id = int( request.args[0])
    record =  db.finansai ( id )
    return SQLFORM( db.finansai , record )






