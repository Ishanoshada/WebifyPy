# WebifyPy

WebifyPy is a Python module for generating HTML forms and components. It provides a set of classes to easily create various HTML elements commonly used in web development.

## Installation

You can install WebifyPy using pip:

```bash
pip install WebifyPy
```

## Usage

### Using Forms

```python
from WebifyPy.forms import Form, InputField, SubmitButton

# Create a form
form = Form(action="/submit", method="POST")

# Add fields to the form
username_field = InputField(name="username", type="text", label="Username")
password_field = InputField(name="password", type="password", label="Password")
submit_button = SubmitButton(label="Submit")

form.add_field(username_field)
form.add_field(password_field)
form.add_field(submit_button)

# Render the form
form_html = form.render()
```

### Using Components

```python
from WebifyPy.components import Div, Header, Paragraph

# Create a div with a header and a paragraph
content = Div(
    content=Header(level=2, text="Welcome to WebifyPy!") +
             Paragraph(content="WebifyPy is a Python module for generating HTML forms and components.")
)

# Render the content
content_html = content.render()
```


### Creating a Dropdown Menu

```python
from WebifyPy.components import Dropdown

# Define options for the dropdown
options = ["Option 1", "Option 2", "Option 3"]

# Create a dropdown
dropdown = Dropdown(options=options)

# Render the dropdown
dropdown_html = dropdown.render()
```

### Building a Contact Form

```python
from WebifyPy.forms import Form, InputField, TextArea, SubmitButton

# Create a contact form
contact_form = Form(action="/contact_submit", method="POST")

# Add fields to the form
name_field = InputField(name="name", type="text", label="Name")
email_field = InputField(name="email", type="email", label="Email")
message_field = TextArea(name="message", rows=5, cols=30, label="Message")
submit_button = SubmitButton(label="Send Message")

contact_form.add_field(name_field)
contact_form.add_field(email_field)
contact_form.add_field(message_field)
contact_form.add_field(submit_button)

# Render the form
contact_form_html = contact_form.render()
```

### Creating a List of Products

```python
from WebifyPy.components import List

# Define a list of products
products = ["Product 1", "Product 2", "Product 3"]

# Create a list component
product_list = List(items=products)

# Render the list
product_list_html = product_list.render()
```

### Making a Table of User Data

```python
from WebifyPy.components import Table

# Define headers and rows for the table
headers = ["Name", "Email", "Role"]
rows = [
    ["John Doe", "john@example.com", "Admin"],
    ["Jane Smith", "jane@example.com", "User"],
    ["Jim Brown", "jim@example.com", "User"]
]

# Create a table component
user_table = Table(headers=headers, rows=rows)

# Render the table
user_table_html = user_table.render()
```


## Classes Reference


### components.py

| Class Name       | render Description                                              |
|------------------|---------------------------------------------------------------|
| FormComponent    | Renders a form element with specified action and method.        |
| InputField       | Renders an input field with specified name and type.         |
| Button           | Renders a button element with specified label.               |
| TextArea         | Renders a text area element with specified attributes.        |
| Image            | Renders an image element with specified src and alt.         |
| Link             | Renders an anchor element with specified href and text.      |
| Header           | Renders a header element with specified level and text.      |
| List             | Renders a list element with specified items.                |
| Dropdown         | Renders a select element with specified options.             |
| Checkbox         | Renders an input checkbox element with specified attributes. |
| Radio            | Renders an input radio button element with specified attributes. |
| Table            | Renders a table element with specified headers and rows.     |
| Div              | Renders a div element with specified content.               |
| Span             | Renders a span element with specified content.              |
| Paragraph        | Renders a paragraph element with specified content.         |
| Heading          | Renders a heading element with specified level and content.   |
| Strong           | Renders a strong element with specified content.            |
| Emphasis         | Renders an emphasis element with specified content.         |
| Anchor           | Renders an anchor element with specified href and text.      |
| ImageLink        | Renders an anchor element with specified href and an image.  |
| UnorderedList   | Renders an unordered list element with specified items.      |
| OrderedList     | Renders an ordered list element with specified items.       |
| Blockquote       | Renders a blockquote element with specified content.        |
| Code             | Renders a code element with specified content.              |
| Preformatted     | Renders a preformatted element with specified content.     |
| HorizontalRule  | Renders a horizontal rule element.                            |
| Navigation      | Renders a navigation element with specified links.          |
| Section         | Renders a section element with specified content.           |
| Article         | Renders an article element with specified content.           |
| Footer          | Renders a footer element with specified content.             |

### forms.py

| Class Name      | render Description                                                           |
|-----------------|-----------------------------------------------------------------------|
| Form            | Renders a form element with specified action, method, and fields.    |
| InputField      | Renders an input field element with specified attributes.             |
| TextArea        | Renders a text area element with specified attributes.                |
| Checkbox        | Renders an input checkbox element with specified attributes.         |
| Radio           | Renders an input radio button element with specified attributes.     |
| SelectField     | Renders a select element with specified attributes.                  |
| FileUpload      | Renders a file input element with specified attributes.              |
| HiddenField     | Renders a hidden input element with specified attributes.            |
| SubmitButton    | Renders a submit input element with specified label.                 |
| RangeInput      | Renders a range input element with specified attributes.              |
| ColorInput      | Renders a color input element with specified attributes.              |
| DateInput       | Renders a date input element with specified attributes.               |
| EmailInput      | Renders an email input element with specified attributes.             |
| PasswordInput   | Renders a password input element with specified attributes.          |
| TelephoneInput  | Renders a telephone input element with specified attributes.         |
| URLInput        | Renders a URL input element with specified attributes.              |
| SearchInput     | Renders a search input element with specified attributes.           |
| CheckboxGroup   | Renders a group of checkboxes with specified attributes.             |
| RadioGroup      | Renders a group of radio buttons with specified attributes.          |


**Repository Views** ![Views](https://profile-counter.glitch.me/WebifyPy/count.svg)



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
