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


def search():
    # db.reikalai.tiekejas.requires = IS_IN_DB( db, db.reikalai.tiekejas, distinct=True )
    sform = SQLFORM.factory ( 
       db.reikalai.tiekejas_id,   # vietoj tiekejas
       db.finansai.reikalas_id,  # vietoj uz_ka
       Field( 'iki_kiek', 'integer') # Todo: padaryt ir    nuo_kiek
    ) 
    sform.process(keepvalues=True)  # suvirškinam formai įvestus   vars'us
    # request.vars  -->     sform.vars
    
    query = db.finansai.id > 0  # pradinis filtras -- visi įrašai
    # INNER JOIN
    # query &= db.reikalai.id == db.finansai.reikalas_id # --> perkaliam į select(.., join/left=[..])
    
    # nes
    # WHERE  filtrai labiau skirti atfiltruot įrašams/eilutėms, 
    # o lentelių sujungimui naudojami:
    # INNER/LEFT JOIN ON    reikalai.id = finansai.reikalas_id
        
    if sform.vars.tiekejas:
        query &= db.reikalai.tiekejas == sform.vars.tiekejas
        
    
    
    if sform.vars.reikalas_id:
        query &= db.finansai.reikalas_id == sform.vars.reikalas_id
    
    if sform.vars.iki_kiek not in [None, '']:
        query &= db.finansai.kiek <= sform.vars.iki_kiek  # papildoma sąlyga
        
    duom = db( query ).select( 
                db.asmenys.vardas, db.finansai.ALL, db.reikalai.ALL, db.tiekejai.vardas,
                left=[
                   db.reikalai.on(db.reikalai.id == db.finansai.reikalas_id), 
                   db.tiekejai.on(db.tiekejai.id == db.reikalai.tiekejas_id), 
                   
                   db.asmenys.on(db.asmenys.id == db.finansai.asmuo_id), 
                ] 
            )
    
    return CAT(sform, duom, sform.vars, query, PRE(db._lastsql))



def sqlform():
    items = []
    # aprašyt ir processint formą
    for x in db().select(db.finansai.ALL):
        form = SQLFORM( 
                    db.finansai,
                    record=x,
                    showid=False,
                    deletable=True,
                    #formstyle="bootstrap3_inline" ,
                ).process()
        items.append( form )
     #  ją pridėti 
    style = STYLE("""
    ul tr {float:left; } 
    ul  {  list-style: none;  }
    li { margin-bottom: -15px; }
     """)
    return CAT ( UL( items ), style )
 


