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
    content=Header(level=2, text="Welcome to WebifyPy!") +
             Paragraph(content="WebifyPy is a Python module for generating HTML forms and components.")
)

# Render the content
content_html = content.render()
```

### Streamlined Form Creation

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

### Pre-Styled Components for Quick Design

```python
from WebifyPy.pre_components import AlertComponent, CardComponent

# Create an alert
alert = AlertComponent(message="This is a sample alert.", alert_type="success")

# Create a card with content
card = CardComponent(content="This is a sample card.")

# Render the alert and card
alert_html = alert.render()
card_html = card.render()
```

### Style Elements with Ease

```python
from WebifyPy.styled_components import StyledDiv, StyledButton

# Create a styled div
styled_div = StyledDiv(content="This is a styled div.")

# Create a styled button
styled_button = StyledButton(label="Click me")

# Render the styled div and button
styled_div_html = styled_div.render()
styled_button_html = styled_button.render()
```

### Interactive JavaScript Components

```python
from WebifyPy.js_components import CounterComponent, ToggleSwitchComponent

# Create a counter component
counter = CounterComponent()

# Create a toggle switch component
toggle_switch = ToggleSwitchComponent(default_state=True)

# Render the counter and toggle switch
counter_html = counter.render()
toggle_switch_html = toggle_switch.render()
```



## Classes Reference


### components

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

### forms

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



### pre_components

| Class Name         | Description                                            |
|--------------------|--------------------------------------------------------|
| PreComponent       | Base class for pre-rendered components.                |
| AlertComponent     | Renders an alert message with specified content.      |
| BadgeComponent     | Renders a badge with specified content.               |
| CardComponent      | Renders a card with specified content.                |
| ProgressComponent  | Renders a progress bar with specified value.          |
| ListGroupComponent | Renders a list group with specified items.           |
| SpinnerComponent   | Renders a loading spinner.                           |
| ToastComponent     | Renders a toast notification with specified content. |
| ModalComponent     | Renders a modal dialog with specified content.       |
| CollapseComponent  | Renders a collapsible content section.               |
| DropdownComponent  | Renders a dropdown menu with specified options.      |
| TabComponent       | Renders a tabbed interface.                          |
| TooltipComponent   | Renders a tooltip with specified text and content.   |

### styled_components

| Class Name          | Description                                             |
|---------------------|---------------------------------------------------------|
| StyledComponent     | Base class for styled components.                        |
| StyledDiv           | Renders a styled div element with specified content.   |
| StyledButton        | Renders a styled button element with specified label.  |
| StyledInputField    | Renders a styled input field element with specified attributes. |
| StyledLink          | Renders a styled anchor element with specified href and text. |
| StyledParagraph     | Renders a styled paragraph element with specified content.   |
| StyledHeader        | Renders a styled header element with specified level and text. |
| StyledSpan          | Renders a styled span element with specified content.         |
| StyledList          | Renders a styled list element with specified items.           |
| StyledImage         | Renders a styled image element with specified src and alt.     |
| StyledForm          | Renders a styled form element with specified action and method. |
| StyledTextArea      | Renders a styled text area element with specified attributes.   |
| StyledTable         | Renders a styled table element with specified headers and rows. |
| StyledSelect        | Renders a styled select element with specified options.        |

### js_components

| Class Name             | Description                                             |
|------------------------|---------------------------------------------------------|
| JSComponent            | Base class for JavaScript-based components.            |
| CounterComponent       | Renders a counter component with increment and decrement buttons. |
| ToggleSwitchComponent  | Renders a toggle switch component with an on/off state.  |
| CopyToClipboardComponent| Renders a button to copy content to clipboard.            |
| ScrollToTopComponent   | Renders a button to scroll to the top of the page.       |
| DarkModeToggleComponent| Renders a toggle switch for dark mode.                   |
| HTTPRequestComponent   | Renders a button to send an HTTP request.                |
| ImageSliderComponent   | Renders an image slider with navigation buttons.         |
| AccordionComponent     | Renders an accordion with collapsible sections.          |
| CountdownTimerComponent | Renders a countdown timer to a specified date.          |
| RandomQuoteComponent    | Renders a random quote from a provided list.             |
| InteractiveMapComponent | Renders an interactive map with specified coordinates.  |
| LightboxComponent       | Renders a lightbox gallery for images.                   |
| ImageZoomComponent      | Renders an image with zoom functionality.               |
| CarouselComponent       | Renders a carousel with navigation buttons.             |
| ProgressBarComponent    | Renders a progress bar with animation.               
**Repository Views** ![Views](https://profile-counter.glitch.me/WebifyPy/count.svg)


## Author

[Ishan Oshada](https://github.com/ishanoshada)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
