class Cardinality(object):
    one = 1
    many = 2

class Field(object):

    def __init__(self, name, scalar_type, table, column):
        self.name=name
        self.scalar_type = scalar_type
        self.table = table
        self.column = column

class Relationship(object):
    
    def __init__(self, name, to_card, to_type):
        self.name = name
        self.to_type = to_type
        self.to_card = to_card

class Type(dict):

    def __init__(self, *fields):
        for field in fields:
            self.add(field)

    def add(self, field):
        self[field.name] = field

class Model(dict):

    def __init__(self, *types):
        for t in types:
            assert type(t) == Type
            self[t.name] = t

    def relate(self, card1, type1, name1, card2, type2, name2):
        pass


