from .data import data

class component_input:
    def __init__(self):
        self.input = dict()

    def __getitem__(self, key):
        try:
            return self.input[key]
        except:
            return None

    def __setitem__(self, key, value):
        self.input[key] = value

    def update(self, data):
        self.input.update(data)

    def clean(self):
        self.input = dict()

class component:
    def __init__(self):
        self.data = data()
        self.input = component_input()
        self.fatal_exceptions = []

    def update(self, data):
        self.input.update(data)
        try:
            self._compute()
        except Exception as e:
            if any([arg in e.args for arg in self.fatal_exceptions]):
                raise e

    def _compute(self):
        pass

    def add_dependency(self, dependency):
        dependency.data.add_dependent(self)
