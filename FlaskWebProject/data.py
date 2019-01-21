import pandas as  pd
import pyodbc
import urllib
import sqlalchemy as sa

quoted = urllib.parse.quote_plus("Driver={SQL Server Native Client 11.0};"
                      "Server=ssqlpaazu01;"
                      "Database=Pret_Predictive;"
                      "Trusted_Connection=yes;"
                      )
engine = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))


shops = []
shops_table = pd.read_sql('select * from data.MM_model_shop_mapping where predictions_live = 1 order by shop_name', engine)
shop_zip = zip(shops_table['shop_id'], shops_table['shop_name'])

for elem in shop_zip:
    shops.append(elem)

def get_shops(self):
    #shops = [(30, 'Marble Archxxx'), (10474, 'Stansted Airportxxxx'), (10475, 'Stansted Airportyyy')]
    return shops
