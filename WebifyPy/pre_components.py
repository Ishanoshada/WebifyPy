#pre_components.py

class BootstrapComponents:
    def __init__(self):
        pass

    def render_button(self, label):
        return f'<button class="btn btn-primary">{label}</button>'

    def render_modal(self, title, content):
        return f'''
            <div class="modal fade" tabindex="-1" role="dialog">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">{title}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            {content}
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
        '''



class Alert:
    def __init__(self, message, alert_type='info'):
        self.message = message
        self.alert_type = alert_type

    def render(self):
        return f'<div class="alert alert-{self.alert_type}" role="alert">{self.message}</div>'

class Modal:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def render(self):
        return f'''
            <div class="modal fade" tabindex="-1" role="dialog">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">{self.title}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            {self.content}
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
        '''

class Card:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def render(self):
        return f'''
            <div class="card">
                <div class="card-header">{self.title}</div>
                <div class="card-body">
                    {self.content}
                </div>
            </div>
        '''


class Navbar:
    def __init__(self, brand, links):
        self.brand = brand
        self.links = links

    def render(self):
        nav_links = ''.join([f'<a class="nav-link" href="{link["url"]}">{link["text"]}</a>' for link in self.links])
        return f'''
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="#">{self.brand}</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ml-auto">
                        {nav_links}
                    </ul>
                </div>
            </nav>
        '''

class Pagination:
    def __init__(self, total_pages, current_page):
        self.total_pages = total_pages
        self.current_page = current_page

    def render(self):
        pagination_items = ''.join([f'<li class="page-item"><a class="page-link" href="?page={i}">{i}</a></li>' for i in range(1, self.total_pages + 1)])
        return f'''
            <nav aria-label="Page navigation example">
                <ul class="pagination">
                    {pagination_items}
                </ul>
            </nav>
        '''

class Progress:
    def __init__(self, value, max):
        self.value = value
        self.max = max

    def render(self):
        return f'<progress value="{self.value}" max="{self.max}"></progress>'



class Badge:
    def __init__(self, text, badge_type='primary'):
        self.text = text
        self.badge_type = badge_type

    def render(self):
        return f'<span class="badge badge-{self.badge_type}">{self.text}</span>'

class Jumbotron:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def render(self):
        return f'''
            <div class="jumbotron">
                <h1 class="display-4">{self.title}</h1>
                <p class="lead">{self.content}</p>
            </div>
        '''

class AlertDismissable:
    def __init__(self, message, alert_type='info'):
        self.message = message
        self.alert_type = alert_type

    def render(self):
        return f'''
            <div class="alert alert-{self.alert_type} alert-dismissible fade show" role="alert">
                {self.message}
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        '''

class ListGroup:
    def __init__(self, items):
        self.items = items

    def render(self):
        item_list = ''.join([f'<li class="list-group-item">{item}</li>' for item in self.items])
        return f'<ul class="list-group">{item_list}</ul>'

class Carousel:
    def __init__(self, images):
        self.images = images

    def render(self):
        carousel_items = ''.join([f'<div class="carousel-item"><img src="{image}" class="d-block w-100" alt="..."></div>' for image in self.images])
        return f'''
            <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    {carousel_items}
                </div>
            </div>
        '''

class Breadcrumb:
    def __init__(self, links):
        self.links = links

    def render(self):
        breadcrumb_items = ''.join([f'<li class="breadcrumb-item"><a href="{link["url"]}">{link["text"]}</a></li>' for link in self.links])
        return f'<ol class="breadcrumb">{breadcrumb_items}</ol>'


class Toast:
    def __init__(self, message, toast_type='success'):
        self.message = message
        self.toast_type = toast_type

    def render(self):
        return f'''
            <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-delay="2000">
                <div class="toast-header">
                    <strong class="mr-auto">Notification</strong>
                    <small class="text-muted">just now</small>
                    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="toast-body">
                    <div class="alert alert-{self.toast_type}" role="alert">
                        {self.message}
                    </div>
                </div>
            </div>
        '''

class Popover:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def render(self):
        return f'''
            <a tabindex="0" class="btn btn-secondary" role="button" data-toggle="popover" data-trigger="focus" title="{self.title}" data-content="{self.content}">
                Popover
            </a>
        '''

class Tooltip:
    def __init__(self, title):
        self.title = title

    def render(self):
        return f'''
            <a href="#" data-toggle="tooltip" title="{self.title}">Hover over me</a>
        '''

class Collapse:
    def __init__(self, button_text, content):
        self.button_text = button_text
        self.content = content

    def render(self):
        return f'''
            <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                {self.button_text}
            </button>
            <div class="collapse" id="collapseExample">
                <div class="card card-body">
                    {self.content}
                </div>
            </div>
        '''

class Accordion:
    def __init__(self, items):
        self.items = items

    def render(self):
        accordion_items = ''.join([f'''
            <div class="card">
                <div class="card-header" id="heading{i}">
                    <h5 class="mb-0">
                        <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{i}" aria-expanded="true" aria-controls="collapse{i}">
                            Item {i}
                        </button>
                    </h5>
                </div>

                <div id="collapse{i}" class="collapse" aria-labelledby="heading{i}" data-parent="#accordionExample">
                    <div class="card-body">
                        {item}
                    </div>
                </div>
            </div>
        ''' for i, item in enumerate(self.items)])

        return f'''
            <div class="accordion" id="accordionExample">
                {accordion_items}
            </div>
        '''

class Tab:
    def __init__(self, tabs):
        self.tabs = tabs

    def render(self):
        tab_panes = ''.join([f'''
            <div class="tab-pane fade {'show active' if i == 0 else ''}" id="tab{i}" role="tabpanel" aria-labelledby="tab{i}-tab">
                {content}
            </div>
        ''' for i, content in enumerate(self.tabs)])

        nav_tabs = ''.join([f'''
            <a class="nav-item nav-link {'active' if i == 0 else ''}" id="tab{i}-tab" data-toggle="tab" href="#tab{i}" role="tab" aria-controls="tab{i}" aria-selected="{'true' if i == 0 else 'false'}">Tab {i}</a>
        ''' for i in range(len(self.tabs))])

        return f'''
            <ul class="nav nav-tabs" id="myTab" role="tablist">
                {nav_tabs}
            </ul>
            <div class="tab-content" id="myTabContent">
                {tab_panes}
            </div>
                  '''


class Dropdown:
    def __init__(self, options):
        self.options = options

    def render(self):
        option_tags = ''.join([f'<option value="{option}">{option}</option>' for option in self.options])
        return f'<select>{option_tags}</select>'

class InputGroup:
    def __init__(self, input_type, placeholder):
        self.input_type = input_type
        self.placeholder = placeholder

    def render(self):
        return f'<input type="{self.input_type}" placeholder="{self.placeholder}">'

class NavbarBrand:
    def __init__(self, brand_text):
        self.brand_text = brand_text

    def render(self):
        return f'<a class="navbar-brand" href="#">{self.brand_text}</a>'

class CardDeck:
    def __init__(self, cards):
        self.cards = cards

    def render(self):
        card_deck = ''.join([f'<div class="card">{card}</div>' for card in self.cards])
        return f'<div class="card-deck">{card_deck}</div>'

class CardGroup:
    def __init__(self, cards):
        self.cards = cards

    def render(self):
        card_group = ''.join([f'<div class="card">{card}</div>' for card in self.cards])
        return f'<div class="card-group">{card_group}</div>'

 

class Tabs:
    def __init__(self, tabs):
        self.tabs = tabs

    def render(self):
        tab_panes = ''.join([f'''
            <div class="tab-pane fade {'show active' if i == 0 else ''}" id="tab{i}" role="tabpanel" aria-labelledby="tab{i}-tab">
                {content}
            </div>
        ''' for i, content in enumerate(self.tabs)])

        nav_tabs = ''.join([f'''
            <li class="nav-item">
                <a class="nav-link {'active' if i == 0 else ''}" id="tab{i}-tab" data-toggle="pill" href="#tab{i}" role="tab" aria-controls="tab{i}" aria-selected="{'true' if i == 0 else 'false'}">Tab {i}</a>
            </li>
        ''' for i in range(len(self.tabs))])

        return f'''
            <ul class="nav nav-pills" id="myTab" role="tablist">
                {nav_tabs}
            </ul>
            <div class="tab-content" id="myTabContent">
                {tab_panes}
            </div>
        '''

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
        
                        