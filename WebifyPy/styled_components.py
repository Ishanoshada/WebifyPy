# styled_components.py

class StyledButton:
    def __init__(self, label):
        self.label = label

    def render(self):
        return f'''
            <button style="
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            ">{self.label}</button>
        '''

class StyledInput:
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def render(self):
        return f'''
            <input type="text" style="
                width: 100%;
                padding: 10px;
                font-size: 16px;
                border: 2px solid #007bff;
                border-radius: 5px;
                box-sizing: border-box;
            " placeholder="{self.placeholder}">
        '''

class StyledCard:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def render(self):
        return f'''
            <div style="
                border: 2px solid #007bff;
                border-radius: 10px;
                padding: 20px;
                margin: 10px;
                background-color: #f8f9fa;
            ">
                <h2 style="color: #007bff;">{self.title}</h2>
                <p>{self.content}</p>
            </div>
        '''

class StyledNavbar:
    def __init__(self, brand, links):
        self.brand = brand
        self.links = links

    def render(self):
        nav_links = ''.join([f'<a href="{link["url"]}" style="color: #007bff; margin: 0 10px;">{link["text"]}</a>' for link in self.links])
        return f'''
            <nav style="
                background-color: #f8f9fa;
                padding: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <div>
                    <a href="#" style="color: #007bff; font-size: 24px; font-weight: bold; text-decoration: none;">{self.brand}</a>
                </div>
                <div>
                    {nav_links}
                </div>
            </nav>
        '''


class StyledAlert:
    def __init__(self, message, alert_type='success'):
        self.message = message
        self.alert_type = alert_type

    def render(self):
        return f'''
            <div style="
                padding: 10px;
                margin: 10px 0;
                border: 2px solid #28a745;
                border-radius: 5px;
                background-color: #d4edda;
                color: #28a745;
            ">
                {self.message}
            </div>
        '''

class StyledModal:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def render(self):
        return f'''
            <div style="
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: #fff;
                padding: 20px;
                border: 2px solid #007bff;
                border-radius: 10px;
            ">
                <h2 style="color: #007bff;">{self.title}</h2>
                <p>{self.content}</p>
                <button style="
                    padding: 10px 20px;
                    font-size: 16px;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                ">Close</button>
            </div>
        '''

class StyledForm:
    def __init__(self, action, method):
        self.action = action
        self.method = method

    def render(self):
        return f'''
            <form action="{self.action}" method="{self.method}" style="
                margin: 20px 0;
                padding: 20px;
                border: 2px solid #007bff;
                border-radius: 10px;
                background-color: #f8f9fa;
            ">
                <!-- Add form fields here -->
            </form>
        '''


class StyledAccordion:
    def __init__(self, items):
        self.items = items

    def render(self):
        accordion_items = ''.join([f'''
            <div style="
                border: 2px solid #007bff;
                border-radius: 10px;
                margin: 10px 0;
                background-color: #f8f9fa;
            ">
                <div style="padding: 10px; cursor: pointer;" data-toggle="collapse" data-target="#collapse{i}">
                    <h2 style="color: #007bff;">Item {i}</h2>
                </div>
                <div id="collapse{i}" class="collapse" style="padding: 10px;">
                    {item}
                </div>
            </div>
        ''' for i, item in enumerate(self.items)])

        return f'''
            {accordion_items}
        '''

class StyledTabs:
    def __init__(self, tabs):
        self.tabs = tabs

    def render(self):
        tab_panes = ''.join([f'''
            <div id="tab{i}" style="display: none;">
                {content}
            </div>
        ''' for i, content in enumerate(self.tabs)])

        nav_tabs = ''.join([f'''
            <div style="
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                font-size: 16px;
                border: 2px solid #007bff;
                border-radius: 5px;
                cursor: pointer;
                background-color: #fff;
            " onclick="showTab({i})">Tab {i}
            </div>
        ''' for i in range(len(self.tabs))])

        return f'''
            <div>
                <div style="display: flex; flex-wrap: wrap;">
                    {nav_tabs}
                </div>
                <div>
                    {tab_panes}
                </div>
            </div>
            <script>
                function showTab(tabIndex) {{
                    var tabs = document.getElementById('tabs').children;
                    for (var i = 0; i < tabs.length; i++) {{
                        tabs[i].style.display = i === tabIndex ? 'block' : 'none';
                    }}
                }}
            </script>
        '''

class StyledDropdown:
    def __init__(self, options):
        self.options = options

    def render(self):
        option_tags = ''.join([f'<option value="{option}">{option}</option>' for option in self.options])
        return f'''
            <select style="
                padding: 10px;
                font-size: 16px;
                border: 2px solid #007bff;
                border-radius: 5px;
                box-sizing: border-box;
            ">{option_tags}</select>
        '''

class StyledCheckbox:
    def __init__(self, label):
        self.label = label

    def render(self):
        return f'''
            <label style="display: block; margin-bottom: 10px;">
                <input type="checkbox" style="margin-right: 5px;">{self.label}
            </label>
        '''

class StyledRadio:
    def __init__(self, label):
        self.label = label

    def render(self):
        return f'''
            <label style="display: block; margin-bottom: 10px;">
                <input type="radio" style="margin-right: 5px;">{self.label}
            </label>
        '''

class StyledTextarea:
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def render(self):
        return f'''
            <textarea style="
                width: 100%;
                padding: 10px;
                font-size: 16px;
                border: 2px solid #007bff;
                border-radius: 5px;
                box-sizing: border-box;
            " placeholder="{self.placeholder}"></textarea>
        '''

class StyledImage:
    def __init__(self, src, alt):
        self.src = src
        self.alt = alt

    def render(self):
        return f'<img src="{self.src}" alt="{self.alt}" style="max-width: 100%; height: auto;">'


class StyledProgressBar:
    def __init__(self, progress):
        self.progress = progress

    def render(self):
        return f'''
            <div style="
                background-color: #f8f9fa;
                border: 2px solid #007bff;
                border-radius: 5px;
                padding: 5px;
            ">
                <div style="
                    width: {self.progress}%;
                    background-color: #007bff;
                    border-radius: 3px;
                    padding: 5px;
                    color: #fff;
                    text-align: center;
                ">{self.progress}%</div>
            </div>
        '''


class StyledTooltip:
    def __init__(self, text, content):
        self.text = text
        self.content = content

    def render(self):
        return f'''
            <div style="position: relative; display: inline-block;">
                <div style="
                    display: none;
                    position: absolute;
                    background-color: #f9f9f9;
                    color: #333;
                    border: 1px solid #ccc;
                    padding: 10px;
                    border-radius: 5px;
                    z-index: 1;
                    font-size: 14px;
                    width: 200px;
                    text-align: center;
                ">{self.content}</div>
                <span style="border-bottom: 1px dotted #333; cursor: pointer;">{self.text}</span>
            </div>
        '''

class StyledBadge:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f'''
            <span style="
                display: inline-block;
                padding: 5px 10px;
                font-size: 14px;
                font-weight: bold;
                background-color: #007bff;
                color: #fff;
                border-radius: 5px;
            ">{self.text}</span>
        '''



                                                                        