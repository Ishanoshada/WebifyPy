# WebifyPy

WebifyPy is a versatile Python module designed to simplify HTML form and component creation. It offers a comprehensive set of classes that enable effortless development of common web elements.

## Installation

Get started with WebifyPy by installing it via pip:

```bash
pip install WebifyPy
```

## Usage


### Components for Easy UI Building

```python
from WebifyPy.components import Div, Header, Paragraph

# Create a div with a header and a paragraph
content = Div(
    content=[Header(level=2, text="Welcome to WebifyPy"), Paragraph(content="WebifyPy is a Python module for generating HTML forms and components.")]
)

# Render the content
content_html = content.render()
```

### Streamlined Form Creation

```python
from WebifyPy.forms import Form, InputField
from WebifyPy.components import Button


# Create a form
form = Form(action="/submit", method="POST")

# Add fields to the form
username_field = InputField(name="username", type="text")
password_field = InputField(name="password", type="password")
submit_button = Button(label="Submit")

form.add_field(username_field)
form.add_field(password_field)
form.add_field(submit_button)

# Render the form
form_html = form.render()
```

### Pre-Styled Components for Quick Design

```python
from WebifyPy.pre_components import Alert, Card

# Create an alert
alert = Alert(message="This is a sample alert.", alert_type="success")

# Create a card with content
card = Card(title="Sample Card", content="This is a sample card.")

# Render the alert and card
alert_html = alert.render()
card_html = card.render()
```

### Style Elements with Ease

```python
from WebifyPy.styled_components import StyledButton

# Create a styled button
styled_button = StyledButton(label="Click me")

# Render the styled button
styled_button_html = styled_button.render()

```

### Interactive JavaScript Components

```python
from WebifyPy.js_components import CounterComponent

# Create a counter component
counter = CounterComponent()

# Render the counter component
counter_html = counter.render()

```

### Styling

```python
from WebifyPy.styling import CSS

# Define the styles you want to apply
styles = '''
    .button {
        background-color: #007bff;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
'''

# Create a CSS instance with the styles
css_styles = CSS(styles)

# Apply the styles to a component (for example, a ButtonComponent)
button_component = ButtonComponent()
css_styles.apply(button_component)
```

## Classes Reference


### components


| Class Name       | Description                                        |
|------------------|----------------------------------------------------|
| FormComponent    | Renders a form element with custom action and method. |
| InputField       | Renders an input field with custom name and type.    |
| Button           | Renders a button with custom label.                  |
| TextArea         | Renders a text area with custom name, rows, and columns. |
| Image            | Renders an image with custom source and alt text.    |
| Link             | Renders a hyperlink with custom href and text.       |
| Header           | Renders a header with custom level and text.         |
| List             | Renders an unordered list with custom items.        |
| Dropdown         | Renders a dropdown menu with custom options.        |
| Checkbox         | Renders a checkbox with custom name and value.      |
| Radio            | Renders a radio button with custom name and value.   |
| Table            | Renders a table with custom headers and rows.       |
| Div              | Renders a div element with custom content.          |
| Span             | Renders a span element with custom content.         |
| Paragraph        | Renders a paragraph with custom content.           |
| Heading          | Renders a heading with custom level and content.    |
| Strong           | Renders a strong (bold) text element with custom content. |
| Emphasis         | Renders an emphasis (italic) text element with custom content. |
| Anchor           | Renders an anchor (link) with custom href and text.  |
| ImageLink        | Renders an image within a link with custom href, source, and alt text. |
| UnorderedList    | Renders an unordered list with custom items.        |
| OrderedList      | Renders an ordered list with custom items.          |
| Blockquote       | Renders a blockquote element with custom content.    |
| Code             | Renders a code element with custom content.         |
| Preformatted     | Renders preformatted text with custom content.      |
| HorizontalRule   | Renders a horizontal rule (line).                  |
| Navigation       | Renders a navigation bar with custom links.         |
| Section          | Renders a section element with custom content.      |
| Article          | Renders an article element with custom content.      |
| Footer           | Renders a footer element with custom content.       |


### forms

| Class Name      | Description                                             |
|-----------------|---------------------------------------------------------|
| FormComponent    | A component that renders a form with specified action and method. |
| InputField       | A component that renders an input field with specified attributes. |
| ToggleSwitchField | A component that renders a toggle switch as an input field. |
| CheckboxField    | A component that renders a checkbox input field with specified attributes. |
| RadioField       | A component that renders a radio button input field with specified attributes. |
| SelectField      | A component that renders a select input field with specified options. |
| TextAreaField    | A component that renders a text area input field with specified attributes. |
| FileUploadField  | A component that renders a file upload input field with specified attributes. |
| HiddenField      | A component that renders a hidden input field with specified attributes. |
| SubmitButtonField| A component that renders a submit button input field with specified label. |
| RangeInputField  | A component that renders a range input field with specified attributes. |
| ColorInputField  | A component that renders a color input field with specified attributes. |
| DateInputField   | A component that renders a date input field with specified attributes. |
| EmailInputField  | A component that renders an email input field with specified attributes. |
| PasswordInputField | A component that renders a password input field with specified attributes. |
| TelephoneInputField | A component that renders a telephone input field with specified attributes. |
| URLInputField    | A component that renders a URL input field with specified attributes. |
| SearchInputField | A component that renders a search input field with specified attributes. |
| CheckboxGroupField | A component that renders a group of checkboxes with specified attributes. |
| RadioGroupField  | A component that renders a group of radio buttons with specified attributes. |

### pre_components


| Class Name           | Description                                                        |
|----------------------|--------------------------------------------------------------------|
| BootstrapComponents  | Provides methods to render Bootstrap components like buttons and modals. |
| Alert                | Renders an alert message with customizable type and message.        |
| Modal                | Renders a modal with custom title and content.                      |
| Card                 | Renders a card element with custom title and content.               |
| Navbar               | Renders a navigation bar with custom brand and links.               |
| Pagination           | Renders a pagination component with total pages and current page.   |
| Progress             | Renders a progress bar with customizable value and maximum.         |
| Badge                | Renders a badge with custom text and badge type.                    |
| Jumbotron            | Renders a jumbotron with custom title and content.                  |
| AlertDismissable     | Renders a dismissable alert message with customizable type and message. |
| ListGroup            | Renders a list group with custom items.                              |
| Carousel             | Renders a carousel with a list of images.                            |
| Breadcrumb           | Renders a breadcrumb navigation with custom links.                   |
| Toast                | Renders a toast notification with customizable type and message.    |
| Popover              | Renders a popover with custom title and content.                     |
| Tooltip              | Renders a tooltip with custom title.                                 |
| Collapse             | Renders a collapsible element with custom button text and content.   |
| Accordion            | Renders an accordion with collapsible items.                          |
| Tab                  | Renders a tab element with multiple content panes.                    |
| Dropdown             | Renders a dropdown menu with custom options.                          |
| InputGroup           | Renders an input element with custom type and placeholder.            |
| NavbarBrand          | Renders a navbar brand with custom brand text.                        |
| CardDeck             | Renders a card deck with a list of cards.                             |
| CardGroup            | Renders a card group with a list of cards.                            |
| Tabs                 | Renders tabs with multiple content panes.                             |
| Form                 | Renders a form element with custom action and method.                 |


### styled_components


| Class Name         | Description                                                        |
|--------------------|--------------------------------------------------------------------|
| StyledButton       | Renders a styled button element with custom CSS.                    |
| StyledInput        | Renders a styled input element with custom CSS.                     |
| StyledCard         | Renders a styled card element with custom title and content.        |
| StyledNavbar       | Renders a styled navigation bar with custom brand and links.         |
| StyledAlert        | Renders a styled alert message with customizable type and message.   |
| StyledModal        | Renders a styled modal with custom title and content.                |
| StyledForm         | Renders a styled form element with custom action and method.         |
| StyledAccordion    | Renders a styled accordion with collapsible sections.               |
| StyledTabs         | Renders styled tabs with multiple content panes.                    |
| StyledDropdown     | Renders a styled dropdown menu with custom options.                 |
| StyledCheckbox     | Renders a styled checkbox input with custom label.                  |
| StyledRadio        | Renders a styled radio button input with custom label.              |
| StyledTextarea     | Renders a styled textarea element with custom placeholder.           |
| StyledImage        | Renders an image with custom source and alternate text.             |
| StyledProgressBar  | Renders a styled progress bar with customizable progress value.      |
| StyledTooltip      | Renders a styled tooltip with custom text and content.              |
| StyledBadge        | Renders a styled badge with custom text.                             |


### js_components


| Class Name                | Description                              |
|---------------------------|------------------------------------------|
| CounterComponent          | Renders a counter with increment and decrement buttons. |
| ToggleSwitchComponent     | Renders a toggle switch with an optional default state. |
| TooltipComponent          | Renders a tooltip with specified text and content. |
| DropdownComponent         | Renders a dropdown with specified options. |
| AlertComponent            | Renders an alert with a specified message and type. |
| CopyToClipboardComponent  | Renders a button to copy specified content to the clipboard. |
| ScrollToTopComponent      | Renders a button to scroll to the top of the page. |
| DarkModeToggleComponent    | Renders a dark mode toggle switch. |
| HTTPRequestComponent      | Base class for making HTTP requests with specified URL and method. |
| GETRequestComponent       | Renders a button to make a GET request to a specified URL. Inherits from HTTPRequestComponent. |
| POSTRequestComponent      | Renders a button to make a POST request to a specified URL. Inherits from HTTPRequestComponent. |
| PUTRequestComponent       | Renders a button to make a PUT request to a specified URL. Inherits from HTTPRequestComponent. |
| DELETERequestComponent    | Renders a button to make a DELETE request to a specified URL. Inherits from HTTPRequestComponent. |
| ImageSliderComponent      | Renders an image slider with specified images. |
| AccordionComponent        | Renders an accordion with specified sections. |
| CountdownTimerComponent   | Renders a countdown timer to a specified target date. |
| RandomQuoteComponent      | Renders a random quote from a specified list of quotes. |
| InteractiveMapComponent   | Renders an interactive map with specified latitude, longitude, zoom level, and API key. |
| ModalComponent            | Renders a modal window with specified content. |
| LightboxComponent         | Renders a lightbox gallery with specified images. |
| ImageZoomComponent        | Renders an image with zoom functionality. |
| CarouselComponent         | Renders a carousel with specified images. |
| ProgressBarComponent      | Renders a progress bar with specified maximum value. |



### styling 

| Class Name      | Description                                                  |
|-----------------|--------------------------------------------------------------|
| `CSS`           | Represents a set of CSS styles to be applied to a component. |
| `Theme`         | Represents a theme to be applied to a component.             |
| `CSSInJS`       | Represents a CSS-in-JS library to be used with a component.  |
| `StyledComponent` | Represents a component with specific styles applied.       |
| `SASS`          | Represents SASS code to be applied to a component.           |
| `Less`          | Represents Less code to be applied to a component.           |
| `TailwindCSS`   | Represents Tailwind CSS classes to be applied.              |
| `Bootstrap`     | Represents a specific version of Bootstrap to be used.     |



## Usage Examples Components 

### FormComponent

```python
from WebifyPy.components import FormComponent

# Create a form component
form_component = FormComponent(action="/submit", method="POST")
form_html = form_component.render()
```

### InputField

```python
from WebifyPy.components import InputField

# Create an input field
input_field = InputField(name="username", type="text")
input_html = input_field.render()
```

### Button

```python
from WebifyPy.components import Button

# Create a button
button = Button(label="Submit")
button_html = button.render()
```

### TextArea

```python
from WebifyPy.components import TextArea

# Create a text area
text_area = TextArea(name="my_text", rows=4, cols=50)
text_area_html = text_area.render()
```

### Image

```python
from WebifyPy.components import Image

# Create an image
image = Image(src="image.jpg", alt="Sample Image")
image_html = image.render()
```

These examples demonstrate how to create instances of different components and generate their corresponding HTML code using the `render` method. You can customize the attributes (like `name`, `type`, `label`, etc.) based on your specific requirements.


### Using Forms

#### Form
The `Form` class allows you to create a form with specified action and method.

```python
from WebifyPy.forms import Form

# Create a form
form = Form(action="/submit", method="POST")

# Add fields to the form
username_field = InputField(name="username", type="text", label="Username")
password_field = InputField(name="password", type="password", label="Password")

form.add_field(username_field)
form.add_field(password_field)

# Render the form
form_html = form.render()
```

#### InputField
The `InputField` class generates an input field with specified name and type.

```python
from WebifyPy.forms import InputField

# Create an input field
username_field = InputField(name="username", type="text")

# Render the input field
input_html = username_field.render()
```

#### TextArea
The `TextArea` class generates a text area element with specified attributes.

```python
from WebifyPy.forms import TextArea

# Create a text area
message_area = TextArea(name="message", rows=5, cols=30, label="Message")

# Render the text area
textarea_html = message_area.render()
```

#### Checkbox
The `Checkbox` class generates an input checkbox element with specified attributes.

```python
from WebifyPy.forms import Checkbox

# Create a checkbox
subscribe_checkbox = Checkbox(name="subscribe", value="yes", label="Subscribe to newsletter")

# Render the checkbox
checkbox_html = subscribe_checkbox.render()
```

#### Radio
The `Radio` class generates an input radio button element with specified attributes.

```python
from WebifyPy.forms import Radio

# Create a radio button
gender_radio = Radio(name="gender", value="male", label="Male")

# Render the radio button
radio_html = gender_radio.render()
```

These examples showcase how to use various form elements provided by the `forms` module in WebifyPy. You can customize these elements further by adjusting their attributes as needed.

**Repository Views** ![Views](https://profile-counter.glitch.me/WebifyPy/count.svg)


## Author

[Ishan Oshada](https://github.com/ishanoshada)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
