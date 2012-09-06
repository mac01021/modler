from sqlalchemy import Table, Column, MetaData, ForeignKey,\
                       Integer, String, Numeric, DateTime
from sqlalchemy import create_engine

#commodity classes
mineral = 1
vegetable = 2

#commodities
celery = 1
radish = 2
iron = 3
uranium = 4

#banks
si = 1
aboc = 2

#marketeers
eitc = 1
scpc = 2
tbb = 3

#facilities
husky_pizza = 1
smd = 2
om33 = 3
warehouse = 4


class Fixtures(object):
    metadata = None
    engine = None
    model = None

    @classmethod
    def clear(cls):
        cls.metadata = None
        cls.engine = None
        cls.model = None

def _setup_db():
    Fixtures.metadata = MetaData()
    Fixtures.engine = create_engine('sqlite:///:memory:')

def _setup_tables():
    metadata = Fixtures.metadata
    commodities = Table('commodities', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String, nullable=False, unique=True),
                    Column('class_id', Integer)
                  )
    commodity_classes = Table('commodity_classes', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('name', String, nullable=False, unique=True)
                        )
    banks = Table('banks', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String, nullable=False, unique=True)
            )
    marketeers = Table('marketeers', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String, nullable=False, unique=True),
                    Column('deposit_acct_bank_id', Integer),
                    Column('deposit_acct_number', String)
                 )
    facilities = Table('facilities', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String, nullable=False, unique=True),
                    Column('owner_id', Integer, nullable=False),
                    Column('system_name', String, nullable=False),
                    Column('planet_name', String, nullable=False),
                    Column('latitude', Numeric(asdecimal=False), nullable=False),
                    Column('longitude', Numeric(asdecimal=False), nullable=False)
                )
    transactions = Table('transactions', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('when', DateTime, nullable=False),
                    Column('commodity_id', Integer, nullable=False),
                    Column('facility_id', Integer, nullable=False),
                    Column('qty', Integer, nullable=False),
                    Column('value', Numeric(scale=2, precision=19), nullable=False)
                   )
    metadata.create_all(Fixtures.engine)

def _setup_records():
    tables = Fixtures.metadata.tables
    insertions = [ tables['commodity_classes'].insert().values(id=mineral,
                                                               name='Mineral')
                 , tables['commodity_classes'].insert().values(id=vegetable,
                                                               name='Vegetable')
                 , tables['commodities'].insert().values(id=celery,
                                                         name='celery')
                 , tables['commodities'].insert().values(id=radish,
                                                         name='radish')
                 , tables['commodities'].insert().values(id=iron, name='iron')
                 , tables['commodities'].insert().values(id=uranium,
                                                         name='uranium')
                 , tables['banks'].insert().values(id=si,
                                                   name='The Savings Institute')
                 , tables['banks'].insert().values(id=aboc,
                                                   name='Agricultural Bank of China')
                 , tables['marketeers'].insert().values(id=eitc,
                                                        name='East India Trading Co',
                                                        deposit_acct_bank_id=aboc,
                                                        deposit_acct_number='120005697')
                 , tables['marketeers'].insert().values(id=scpc,
                                                        name='Southern Connecticut Pizza Co',
                                                        deposit_acct_bank_id=si,
                                                        deposit_acct_number='00009956')
                 , tables['marketeers'].insert().values(id=tbb,
                                                        name='The Big Buyer',
                                                        deposit_acct_bank_id=si,
                                                        deposit_acct_number='1')
                 , tables['facilities'].insert().values(id=husky_pizza,
                                                        name='Husky Pizza Shoppe',
                                                        owner_id=scpc,
                                                        system_name='Sol',
                                                        planet_name='Earth',
                                                        latitude=43.00156,
                                                        longitude=72.83341)
                 , tables['facilities'].insert().values(id=smd,
                                                        name='Square Market Depot',
                                                        owner_id=eitc,
                                                        system_name='Sol',
                                                        planet_name='Earth',
                                                        latitude=43.01005,
                                                        longitude=72.80023)
                 , tables['facilities'].insert().values(id=om33,
                                                        name='Olympus Mons Post 33',
                                                        owner_id=eitc,
                                                        system_name='Sol',
                                                        planet_name='Mars',
                                                        latitude=0.01165,
                                                        longitude=52.21503)
                 , tables['facilities'].insert().values(id=warehouse,
                                                        name='The Warehouse',
                                                        owner_id=tbb,
                                                        system_name='Sol',
                                                        planet_name='Luna',
                                                        latitude=88.81255,
                                                        longitude=2)
                 , #must insert some transactions
                 ]
    for stmt in insertions:
        Fixtures.engine.execute(stmt)
    #Fixtures.engine.commit()


def _setup_model():
    pass

def setup():
    _setup_db()
    _setup_tables()
    _setup_records()
    _setup_model()

def teardown():
    Fixtures.clear()




##Test cases start here:


def test_model_description():
    pass

def test_get_something():
    banks = Fixtures.engine.execute(Fixtures.metadata.tables['banks'].select())
    banks = list(banks)
    assert (si, 'The Savings Institute') in banks
    assert (aboc, 'Agricultural Bank of China') in banks

