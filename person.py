from section import Section
class Person:
    __section = set()
    def __init__(self, fio, phone):
        self.__fio = fio
        self.__phone = phone

    def __str__(self):
        if len(self.__section) == 0:
            return (f"fio: {self.__fio} | phone: {self.__phone}")
        else:
            result = ""
            for i in self.__section:
                result += str(i) + "\n"
            return (f"fio: {self.__fio} | phone: {self.__phone} | {result}")

    @property
    def fio(self):
        return self.__fio
    @fio.setter
    def fio(self, fio):
        self.__fio = fio
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    def add_section(self, section):
        if isinstance(section, Section):
            self.__section.add(section)

    def del_section(self, name):
        for i in self.__section:
            if i.name_section == name:
                self.__section.discard(i)
                break