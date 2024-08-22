from ..components.component import component, component_input
from ..components.data import data

def get_intermediate_register():
    class intermediate_register(component):
        data = data()
        input = component_input()

        def __init__(self):
            pass

        def setup(self, dependencies):
            for dependency in dependencies:
                self.add_dependency(dependency)

        def update(self, data):
            self.input.update(data)

        def ready(self):
            self.data.clean()
            for key, value in self.input.input.items():
                self.data._update_value(key, value)
            self.input.clean()

        def on_clock(self):
            self.data.update_dependents()

        def add_dependency(self, dependency):
            dependency.data.add_dependent(self)

    return intermediate_register
