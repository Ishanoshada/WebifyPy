# components.py

class FormComponent:
    def __init__(self, action, method):
        self.action = action
        self.method = method

    def render(self):
        return f'<form action="{self.action}" method="{self.method}"></form>'

class InputField:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def render(self):
        return f'<input type="{self.type}" name="{self.name}">'

class Button:
    def __init__(self, label):
        self.label = label

    def render(self):
        return f'<button>{self.label}</button>'

class TextArea:
    def __init__(self, name, rows, cols):
        self.name = name
        self.rows = rows
        self.cols = cols

    def render(self):
        return f'<textarea name="{self.name}" rows="{self.rows}" cols="{self.cols}"></textarea>'

class Image:
    def __init__(self, src, alt):
        self.src = src
        self.alt = alt

    def render(self):
        return f'<img src="{self.src}" alt="{self.alt}">'

class Link:
    def __init__(self, href, text):
        self.href = href
        self.text = text

    def render(self):
        return f'<a href="{self.href}">{self.text}</a>'

class Header:
    def __init__(self, level, text):
        self.level = level
        self.text = text

    def render(self):
        return f'<h{self.level}>{self.text}</h{self.level}>'

class List:
    def __init__(self, items):
        self.items = items

    def render(self):
        item_list = ''.join([f'<li>{item}</li>' for item in self.items])
        return f'<ul>{item_list}</ul>'

class Dropdown:
    def __init__(self, options):
        self.options = options

    def render(self):
        option_tags = ''.join([f'<option value="{option}">{option}</option>' for option in self.options])
        return f'<select>{option_tags}</select>'

class Checkbox:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def render(self):
        return f'<input type="checkbox" name="{self.name}" value="{self.value}">'

class Radio:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def render(self):
        return f'<input type="radio" name="{self.name}" value="{self.value}">'
        
class Table:
    def __init__(self, headers, rows):
        self.headers = headers
        self.rows = rows

    def render(self):
        header_tags = ''.join([f'<th>{header}</th>' for header in self.headers])
        row_tags = ''.join(['<tr>' + ''.join([f'<td>{data}</td>' for data in row]) + '</tr>' for row in self.rows])

        return f'<table><thead><tr>{header_tags}</tr></thead><tbody>{row_tags}</tbody></table>'

class Div:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<div>{self.content}</div>'
        
class Span:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<span>{self.content}</span>'

class Paragraph:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<p>{self.content}</p>'

class Heading:
    def __init__(self, level, content):
        self.level = level
        self.content = content

    def render(self):
        return f'<h{self.level}>{self.content}</h{self.level}>'

class Strong:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<strong>{self.content}</strong>'

        
class Emphasis:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<em>{self.content}</em>'

class Anchor:
    def __init__(self, href, text):
        self.href = href
        self.text = text

    def render(self):
        return f'<a href="{self.href}">{self.text}</a>'

class ImageLink:
    def __init__(self, href, src, alt):
        self.href = href
        self.src = src
        self.alt = alt

    def render(self):
        return f'<a href="{self.href}"><img src="{self.src}" alt="{self.alt}"></a>'
                                
class UnorderedList:
    def __init__(self, items):
        self.items = items

    def render(self):
        item_tags = ''.join([f'<li>{item}</li>' for item in self.items])
        return f'<ul>{item_tags}</ul>'

class OrderedList:
    def __init__(self, items):
        self.items = items

    def render(self):
        item_tags = ''.join([f'<li>{item}</li>' for item in self.items])
        return f'<ol>{item_tags}</ol>'

class Blockquote:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<blockquote>{self.content}</blockquote>'
                                        

class Code:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<code>{self.content}</code>'

class Preformatted:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<pre>{self.content}</pre>'

class HorizontalRule:
    def render(self):
        return '<hr>'

class Navigation:
    def __init__(self, links):
        self.links = links

    def render(self):
        nav_links = ''.join([f'<a href="{link["url"]}">{link["text"]}</a>' for link in self.links])
        return f'<nav>{nav_links}</nav>'

class Section:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<section>{self.content}</section>'

class Article:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<article>{self.content}</article>'

class Footer:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<footer>{self.content}</footer>'
   