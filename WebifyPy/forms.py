class Form:
    def __init__(self, action, method):
        self.action = action
        self.method = method
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def render(self):
        form_html = f'<form action="{self.action}" method="{self.method}">'
        for field in self.fields:
            form_html += field.render()
        form_html += '</form>'
        return form_html

    def set_action(self, action):
        self.action = action

    def set_method(self, method):
        self.method = method


class InputField:
    def __init__(self, name, type, label=None):
        self.name = name
        self.type = type
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="{self.type}" name="{self.name}">'

class TextArea:
    def __init__(self, name, rows, cols, label=None):
        self.name = name
        self.rows = rows
        self.cols = cols
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<textarea name="{self.name}" rows="{self.rows}" cols="{self.cols}"></textarea>'

class Checkbox:
    def __init__(self, name, value, label=None):
        self.name = name
        self.value = value
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="checkbox" name="{self.name}" value="{self.value}">'

class Radio:
    def __init__(self, name, value, label=None):
        self.name = name
        self.value = value
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="radio" name="{self.name}" value="{self.value}">'

class SelectField:
    def __init__(self, name, options, label=None):
        self.name = name
        self.options = options
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        option_tags = ''.join([f'<option value="{option}">{option}</option>' for option in self.options])
        return f'{label_tag}<select name="{self.name}">{option_tags}</select>'
        


class FileUpload:
    def __init__(self, name, accept=None, label=None):
        self.name = name
        self.accept = accept
        self.label = label

    def render(self):
        accept_attr = f' accept="{self.accept}"' if self.accept else ''
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="file" name="{self.name}"{accept_attr}>'

class HiddenField:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def render(self):
        return f'<input type="hidden" name="{self.name}" value="{self.value}">'

class SubmitButton:
    def __init__(self, label):
        self.label = label

    def render(self):
        return f'<input type="submit" value="{self.label}">'

 
class RangeInput:
    def __init__(self, name, min_value, max_value, step, label=None):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="range" name="{self.name}" min="{self.min_value}" max="{self.max_value}" step="{self.step}">'

class ColorInput:
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="color" name="{self.name}">'

class DateInput:
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="date" name="{self.name}">'

class EmailInput:
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ""
        return f'{label_tag}<input type="email" name="{self.name}">'

class PasswordInput:
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="password" name="{self.name}">'
                       


class TelephoneInput:
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="tel" name="{self.name}">'

class URLInput:
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="url" name="{self.name}">'

class SearchInput:
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        return f'{label_tag}<input type="search" name="{self.name}">'

class CheckboxGroup:
    def __init__(self, name, options, label=None):
        self.name = name
        self.options = options
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        checkbox_tags = ''.join([f'<input type="checkbox" name="{self.name}" value="{option}">{option}<br>' for option in self.options])
        return f'{label_tag}{checkbox_tags}'

class RadioGroup:
    def __init__(self, name, options, label=None):
        self.name = name
        self.options = options
        self.label = label

    def render(self):
        label_tag = f'<label>{self.label}</label>' if self.label else ''
        radio_tags = ''.join([f'<input type="radio" name="{self.name}" value="{option}">{option}<br>' for option in self.options])
        return f'{label_tag}{radio_tags}'
                                        
                                                                