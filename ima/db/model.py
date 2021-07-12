from sqlalchemy import (MetaData, String, Table, Column, Integer, Date, Numeric)

meta = MetaData()

stooq_tickers = Table('stooq_tickers', meta,
                      Column('id', Integer, primary_key=True),
                      Column('ticker', String),
                      Column('www', String),
                      Column('name', String)
                      )

biznes_radar_hist = Table('biznes_radar_historical', meta,
                          Column('id', Integer, primary_key=True),
                          Column('ticker', String),
                          Column('Data', Date),
                          Column('Opening', Numeric),
                          Column('Max', Numeric),
                          Column('Min', Numeric),
                          Column('Closing', Numeric),
                          Column('Volumen', Integer),
                          Column('turnover', Integer)
                          )
