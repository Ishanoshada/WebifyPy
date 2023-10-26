# styling.py

class CSS:
    def __init__(self, styles):
        self.styles = styles

    def apply(self, component):
        component.styles = self.styles

class Theme:
    def __init__(self, theme):
        self.theme = theme

    def apply(self, component):
        component.theme = self.theme

class CSSInJS:
    def __init__(self, library):
        self.library = library

    def apply(self, component):
        component.library = self.library

class StyledComponent:
    def __init__(self, styles):
        self.styles = styles

    def apply(self, component):
        component.styles = self.styles

class SASS:
    def __init__(self, sass_code):
        self.sass_code = sass_code

    def apply(self, component):
        component.sass_code = self.sass_code

class Less:
    def __init__(self, less_code):
        self.less_code = less_code

    def apply(self, component):
        component.less_code = self.less_code

class TailwindCSS:
    def __init__(self, classes):
        self.classes = classes

    def apply(self, component):
        component.classes = self.classes

class Bootstrap:
    def __init__(self, version):
        self.version = version

    def apply(self, component):
        component.bootstrap_version = self.version
