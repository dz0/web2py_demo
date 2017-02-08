# -*- coding: utf-8 -*-

# from gluon.storage import Storage

"""
  Duomenų saugojimo lentele ypatumai..

  sarasas iš skaičių:
  kiek
  -------
 [ 10 ,
  -20 ,
   55 , ]
  
  sarasas iš sąrašų:
  kiek  uz_ka
    0      1
  ------------
 [
  [10,     "premija"], 
  [-20,    "pietūs"],
  [55,     "pasisekė loterijoj"],
 ]
  for kiek, uz_ka in sarasas:
      if kiek  > 0:
          print "gavau", kiek, 'uz', uz_ka  #  gražus pythoniškas
  
 
 
  sąrašas iš ŽODYNŲ:
  ---------------------
 [
     { 'kiek': 10,  'uz_ka': "premija"  },
     { 'kiek':-20,  'uz_ka': "pietūs"   },
 ]
  
  for row in sarasas:
      row = Storage( row )  # web2py įprastas duomenų laikymas  
      
      if row.kiek  > 0:
          print "gavau", row.kiek, 'uz', row.uz_ka  
          
          # python su žodynas
          # print "gavau", row['kiek'], 'uz', row['uz_ka']  
                    
"""

# -*- coding: utf-8 -*-

def index():
    """
    sąrašas
    """
    session.clear()
    if not session.sarasas:
        session.sarasas =  [
             { 'kiek': 10,  'uz_ka': "premija"  },
             { 'kiek':-20,  'uz_ka': "pietūs"   },
         ]

    # Create
    form_create = FORM( 
            INPUT(_name='skaicius'),
            # INPUT(_name='nr'),
            _action = URL('prideti') 
       )   
       
    return CAT( form_create, BEAUTIFY(session.sarasas ))
