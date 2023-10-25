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
