class Section:
    def __init__(self, name, max):
        self.__name_section = name
        self.__max = max
    def __str__(self):
        return f"name: {self.__name_section} - {self.__max}"
    @property
    def name_section(self):
        return self.__name_section
    @name_section.setter
    def name_section(self, name):
        self.__name_section = name
    @property
    def max(self):
        return self.__max
    @max.setter
    def max(self, value):
        self.__max = value