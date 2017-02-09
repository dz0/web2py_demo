# -*- coding: utf-8 -*-


# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)


db = DAL(myconf.get('db.uri'),
         pool_size=myconf.get('db.pool_size'),
         migrate_enabled=myconf.get('db.migrate'),
         check_reserved=['all'])

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
# response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
# response.form_label_separator = myconf.get('forms.separator') or ''

# lenteles valdyt galėsim per /appadmin/index

db.define_table(   'finansai' , 
                    Field('kiek', 'integer'), 
                    Field('uz_ka', requires=IS_IN_SET(['bauda', 'premija', 'kažkas'])  )
                )
# uzka = db.finansai.uz_ka
# uzka.requires=IS_IN_DB(db, uzka)
