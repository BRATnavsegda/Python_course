class User:

    def __init__(self, level, id_, name):
        self.level = level
        self.id_ = id_
        self.name = name

    def __eq__(self, other):
        return self.id_ == other.id_

    def __str__(self):
        return f'User {self.name}\nID {self.id_}\nLevel {self.level}'

    def __repr__(self):
        return f'User({self.level}, "{self.id_}", "{self.name}")'

