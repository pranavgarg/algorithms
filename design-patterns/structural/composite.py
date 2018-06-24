from abc import ABCMeta

class MenuComponent:
    __metaclass__ = ABCMeta
    def __init__(self, text):
        self.text = text

class MenuItem(MenuComponent):
    def __init__(self, text):
        super(MenuItem, self).__init__(text)

class Menu(MenuComponent):
    def __init__(self, text):
        self.components = []
        super(Menu, self).__init__(text)

file = Menu("File")
file.components.append(MenuItem("Open"))
file.components.append(MenuItem("Save"))
file.components.append(MenuItem("Exit"))
recentFiles = Menu("Recent")
file.components.append(recentFiles)


