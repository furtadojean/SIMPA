class data:
    def __init__(self):
        self.prefix = ""
        self.data = {}
        self.dependents = set()

    def clean(self):
        self.data = {}

    def __repr__(self):
        return "\n".join(map(str, sorted(filter(lambda x: x[1] != None, self.data.items()))))

    def _add_prefix(self, name):
        name = self._remove_prefix(name)
        if self.prefix == "":
            return name
        return self.prefix + "_" + name

    def _remove_prefix(self, name):
        if "_" in name:
            return name.split("_")[1]
        return name

    def add_value(self, name, value):
        name = self._add_prefix(name)
        self.data[name] = value

    def _update_value(self, name, value):
        name = self._add_prefix(name)
        if type(value) == type(lambda x: x):
            self.data[name] = value(self.data)
        else:
            self.data[name] = value

    def update_value(self, name, value):
        self._update_value(name, value)
        self.update_dependents()

    def get_value(self, name):
        name = self._add_prefix(name)
        return self.data[name]

    def add_dependent(self, dependent):
        self.dependents.add(dependent)

    def update_dependents(self):
        for dependent in self.dependents:
            dependent.update(self.data)
