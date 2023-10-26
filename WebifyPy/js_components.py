# js_components.py

class CounterComponent:
    def __init__(self):
        self.value = 0

    def render(self):
        return f'''
            <div>
                <button onclick="increment()">Increment</button>
                <span id="counterValue">{self.value}</span>
                <button onclick="decrement()">Decrement</button>
            </div>
            <script>
                function increment() {{
                    var counterValue = document.getElementById('counterValue');
                    counterValue.innerText = parseInt(counterValue.innerText) + 1;
                }}

                function decrement() {{
                    var counterValue = document.getElementById('counterValue');
                    counterValue.innerText = parseInt(counterValue.innerText) - 1;
                }}
            </script>
        '''


class ToggleSwitchComponent:
    def __init__(self, default_state=False):
        self.state = default_state

    def render(self):
        return f'''
            <label class="toggle-switch">
                <input type="checkbox" {'checked' if self.state else ''} onchange="toggleSwitch(this)">
                <span class="slider"></span>
            </label>
            <script>
                function toggleSwitch(input) {{
                    var slider = input.nextElementSibling;
                    if (input.checked) {{
                        slider.style.backgroundColor = '#007bff';
                    }} else {{
                        slider.style.backgroundColor = '#ccc';
                    }}
                }}
            </script>
        '''
 



class TooltipComponent:
    def __init__(self, text, content):
        self.text = text
        self.content = content

    def render(self):
        return f'''
            <div class="tooltip">
                {self.text}
                <span class="tooltiptext">{self.content}</span>
            </div>
            <style>
                .tooltip {{
                    position: relative;
                    display: inline-block;
                    cursor: pointer;
                }}

                .tooltiptext {{
                    visibility: hidden;
                    width: 120px;
                    background-color: #007bff;
                    color: #fff;
                    text-align: center;
                    border-radius: 5px;
                    padding: 5px;
                    position: absolute;
                    z-index: 1;
                    bottom: 125%;
                    left: 50%;
                    margin-left: -60px;
                    opacity: 0;
                    transition: opacity 0.2s;
                }}

                .tooltip:hover .tooltiptext {{
                    visibility: visible;
                    opacity: 1;
                }}
            </style>
        '''

class DropdownComponent:
    def __init__(self, options):
        self.options = options

    def render(self):
        option_tags = ''.join([f'<option value="{option}">{option}</option>' for option in self.options])
        return f'''
            <select>
                {option_tags}
            </select>
        '''

class AlertComponent:
    def __init__(self, message, alert_type='success'):
        self.message = message
        self.alert_type = alert_type

    def render(self):
        return f'''
            <div class="alert alert-{self.alert_type}" role="alert">
                {self.message}
            </div>
            <style>
                .alert {{
                    padding: 15px;
                    margin-bottom: 20px;
                    border: 1px solid transparent;
                    border-radius: .25rem;
                }}
                .alert-success {{
                    color: #28a745;
                    background-color: #d4edda;
                    border-color: #c3e6cb;
                }}
                .alert-danger {{
                    color: #721c24;
                    background-color: #f8d7da;
                    border-color: #f5c6cb;
                }}
            </style>
        '''




class CopyToClipboardComponent:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'''
            <button onclick="copyToClipboard('{self.content}')">Copy to Clipboard</button>
            <script>
                function copyToClipboard(content) {{
                    var tempInput = document.createElement('input');
                    tempInput.value = content;
                    document.body.appendChild(tempInput);
                    tempInput.select();
                    document.execCommand('copy');
                    document.body.removeChild(tempInput);
                }}
            </script>
        '''

class ScrollToTopComponent:
    def render(self):
        return f'''
            <button onclick="scrollToTop()">Scroll to Top</button>
            <script>
                function scrollToTop() {{
                    window.scrollTo(0, 0);
                }}
            </script>
        '''

class DarkModeToggleComponent:
    def render(self):
        return f'''
            <label class="toggle-switch">
                <input type="checkbox" onchange="toggleDarkMode()">
                <span class="slider"></span>
            </label>
            <script>
                function toggleDarkMode() {{
                    document.body.classList.toggle('dark-mode');
                }}
            </script>
            <style>
                .dark-mode {{
                    background-color: #333;
                    color: #fff;
                }}
            </style>
        '''
        

class HTTPRequestComponent:
    def __init__(self, url, method):
        self.url = url
        self.method = method

    def render(self):
        return f'''
            <button onclick="sendRequest('{self.method}')">{self.method} Request</button>
            <script>
                function sendRequest(method) {{
                    var xhr = new XMLHttpRequest();
                    xhr.open(method, '{self.url}', true);
                    xhr.onreadystatechange = function() {{
                        if (xhr.readyState == XMLHttpRequest.DONE) {{
                            if (xhr.status == 200) {{
                                console.log('Request successful:', xhr.responseText);
                            }} else {{
                                console.error('Error:', xhr.status, xhr.statusText);
                            }}
                        }}
                    }};
                    xhr.send();
                }}
            </script>
        '''

class GETRequestComponent(HTTPRequestComponent):
    def __init__(self, url):
        super().__init__(url, 'GET')

class POSTRequestComponent(HTTPRequestComponent):
    def __init__(self, url):
        super().__init__(url, 'POST')

class PUTRequestComponent(HTTPRequestComponent):
    def __init__(self, url):
        super().__init__(url, 'PUT')

class DELETERequestComponent(HTTPRequestComponent):
    def __init__(self, url):
        super().__init__(url, 'DELETE')

class ImageSliderComponent:
    def __init__(self, images):
        self.images = images

    def render(self):
        image_tags = ''.join([f'<img src="{image}" alt="Slide">' for image in self.images])
        return f'''
            <div class="slider">
                {image_tags}
                <button class="prev" onclick="prevSlide()">&#10094;</button>
                <button class="next" onclick="nextSlide()">&#10095;</button>
            </div>
            <script>
                var slideIndex = 1;

                function showSlide(n) {{
                    var slides = document.getElementsByClassName("slide");
                    if (n > slides.length) {{ slideIndex = 1 }}
                    if (n < 1) {{ slideIndex = slides.length }}
                    for (var i = 0; i < slides.length; i++) {{
                        slides[i].style.display = "none";
                    }}
                    slides[slideIndex - 1].style.display = "block";
                }}

                function nextSlide() {{
                    showSlide(slideIndex += 1);
                }}

                function prevSlide() {{
                    showSlide(slideIndex -= 1);
                }}

                showSlide(slideIndex);
            </script>
            <style>
                .slider {{
                    position: relative;
                }}
                .slide {{
                    display: none;
                }}
                .prev, .next {{
                    position: absolute;
                    top: 50%;
                    width: auto;
                    padding: 16px;
                    margin-top: -22px;
                    color: white;
                    font-weight: bold;
                    font-size: 18px;
                    transition: 0.6s ease;
                    border-radius: 0 3px 3px 0;
                    user-select: none;
                    cursor: pointer;
                }}
                .next {{
                    right: 0;
                    border-radius: 3px 0 0 3px;
                }}
            </style>
        '''
                                     


class AccordionComponent:
    def __init__(self, sections):
        self.sections = sections

    def render(self):
        section_html = ''.join([f'<div class="section"><button class="accordion" onclick="toggleSection({i})">{section["title"]}</button><div class="content">{section["content"]}</div></div>' for i, section in enumerate(self.sections)])
        return f'''
            <div class="accordion-container">
                {section_html}
            </div>
            <script>
                function toggleSection(index) {{
                    var sections = document.getElementsByClassName('content');
                    sections[index].classList.toggle('active');
                }}
            </script>
            <style>
                .accordion-container {{
                    max-width: 600px;
                    margin: 0 auto;
                }}
                .section {{
                    margin-bottom: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }}
                .accordion {{
                    width: 100%;
                    text-align: left;
                    padding: 10px;
                    background-color: #f5f5f5;
                    border: none;
                    outline: none;
                    cursor: pointer;
                }}
                .content {{
                    display: none;
                    padding: 10px;
                }}
                .content.active {{
                    display: block;
                }}
            </style>
        '''
                                                                             

class CountdownTimerComponent:
    def __init__(self, target_date):
        self.target_date = target_date

    def render(self):
        return f'''
            <div id="countdown"></div>
            <script>
                var targetDate = new Date('{self.target_date}').getTime();

                var x = setInterval(function() {{
                    var now = new Date().getTime();
                    var distance = targetDate - now;
                    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                    document.getElementById('countdown').innerHTML = days + 'd ' + hours + 'h '
                    + minutes + 'm ' + seconds + 's ';

                    if (distance < 0) {{
                        clearInterval(x);
                        document.getElementById('countdown').innerHTML = 'EXPIRED';
                    }}
                }}, 1000);
            </script>
        '''

class RandomQuoteComponent:
    def __init__(self, quotes):
        self.quotes = quotes

    def render(self):
        return f'''
            <div id="quote"></div>
            <script>
                var quotes = {self.quotes};
                var randomIndex = Math.floor(Math.random() * quotes.length);
                document.getElementById('quote').innerHTML = quotes[randomIndex];
            </script>
        '''

class InteractiveMapComponent:
    def __init__(self, latitude, longitude, zoom, api_key):
        self.latitude = latitude
        self.longitude = longitude
        self.zoom = zoom
        self.api_key = api_key

    def render(self):
        return f'''
            <div id="map" style="width: 100%; height: 400px;"></div>
            <script>
                function initMap() {{
                    var myLatLng = {{lat: {self.latitude}, lng: {self.longitude}}};
                    var map = new google.maps.Map(document.getElementById('map'), {{
                        center: myLatLng,
                        zoom: {self.zoom}
                    }});
                    var marker = new google.maps.Marker({{
                        position: myLatLng,
                        map: map,
                        title: 'Hello World!'
                    }});
                }}
            </script>
            <script async defer src="https://maps.googleapis.com/maps/api/js?key={self.api_key}&callback=initMap"></script>
        '''
 
 
 
 

class ModalComponent:
    def __init__(self, modal_id, content):
        self.modal_id = modal_id
        self.content = content

    def render(self):
        return f'''
            <div id="{self.modal_id}" class="modal">
                <div class="modal-content">
                    <span class="close" onclick="closeModal('{self.modal_id}')">&times;</span>
                    {self.content}
                </div>
            </div>
            <script>
                function openModal(id) {{
                    var modal = document.getElementById(id);
                    modal.style.display = "block";
                }}

                function closeModal(id) {{
                    var modal = document.getElementById(id);
                    modal.style.display = "none";
                }}

                window.onclick = function(event) {{
                    var modals = document.getElementsByClassName('modal');
                    for (var i = 0; i < modals.length; i++) {{
                        if (event.target == modals[i]) {{
                            modals[i].style.display = "none";
                        }}
                    }}
                }}
            </script>
            <style>
                .modal {{
                    display: none;
                    position: fixed;
                    z-index: 1;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    overflow: auto;
                    background-color: rgb(0,0,0);
                    background-color: rgba(0,0,0,0.4);
                    padding-top: 60px;
                }}

                .modal-content {{
                    background-color: #fefefe;
                    margin: 5% auto;
                    padding: 20px;
                    border: 1px solid #888;
                    width: 80%;
                }}

                .close {{
                    color: #aaa;
                    float: right;
                    font-size: 28px;
                    font-weight: bold;
                }}

                .close:hover,
                .close:focus {{
                    color: black;
                    text-decoration: none;
                    cursor: pointer;
                }}
            </style>
        '''

class LightboxComponent:
    def __init__(self, images):
        self.images = images

    def render(self):
        image_tags = ''.join([f'<img src="{image}" onclick="openLightbox(\'lightbox-{i}\')" class="lightbox-image">' for i, image in enumerate(self.images)])
        lightbox_tags = ''.join([f'<div id="lightbox-{i}" class="lightbox-modal"><span class="close-lightbox" onclick="closeLightbox(\'lightbox-{i}\')">&times;</span><img src="{image}" class="lightbox-content"></div>' for i, image in enumerate(self.images)])
        return f'''
            <div class="lightbox-gallery">
                {image_tags}
            </div>
            {lightbox_tags}
            <script>
                function openLightbox(id) {{
                    var lightbox = document.getElementById(id);
                    lightbox.style.display = "block";
                }}

                function closeLightbox(id) {{
                    var lightbox = document.getElementById(id);
                    lightbox.style.display = "none";
                }}
            </script>
            <style>
                .lightbox-gallery {{
                    display: flex;
                    flex-wrap: wrap;
                }}

                .lightbox-image {{
                    max-width: 100px;
                    margin: 10px;
                    cursor: pointer;
                }}

                .lightbox-modal {{
                    display: none;
                    position: fixed;
                    z-index: 1;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    overflow: auto;
                    background-color: rgb(0,0,0);
                    background-color: rgba(0,0,0,0.9);
                    text-align: center;
                    padding-top: 60px;
                }}

                .lightbox-content {{
                    margin: auto;
                    display: block;
                    max-height: 80%;
                    max-width: 80%;
                }}

                .close-lightbox {{
                    position: absolute;
                    top: 15px;
                    right: 35px;
                    font-size: 50px;
                    font-weight: bold;
                    color: #f1f1f1;
                    cursor: pointer;
                }}

                .close-lightbox:hover,
                .close-lightbox:focus {{
                    color: #bbb;
                    text-decoration: none;
                    cursor: pointer;
                }}
            </style>
        '''


class ImageZoomComponent:
    def __init__(self, src, zoom_factor):
        self.src = src
        self.zoom_factor = zoom_factor

    def render(self):
        return f'''
            <div class="image-zoom-container">
                <img src="{self.src}" class="image-zoom">
            </div>
            <script>
                var zoomContainer = document.querySelector('.image-zoom-container');
                var zoomImage = document.querySelector('.image-zoom');

                zoomContainer.addEventListener('mousemove', function(e) {{
                    var offsetX = e.offsetX;
                    var offsetY = e.offsetY;

                    var xPercent = offsetX / zoomContainer.offsetWidth;
                    var yPercent = offsetY / zoomContainer.offsetHeight;

                    var xZoom = xPercent * {self.zoom_factor};
                    var yZoom = yPercent * {self.zoom_factor};

                    zoomImage.style.transform = 'scale({self.zoom_factor}) translate(-' + xZoom + 'px, -' + yZoom + 'px)';
                }});

                zoomContainer.addEventListener('mouseleave', function() {{
                    zoomImage.style.transform = 'scale(1) translate(0, 0)';
                }});
            </script>
            <style>
                .image-zoom-container {{
                    position: relative;
                    overflow: hidden;
                    width: 400px;
                    height: 300px;
                    border: 1px solid #ccc;
                }}

                .image-zoom {{
                    max-width: 100%;
                    max-height: 100%;
                    transition: transform 0.2s;
                }}
            </style>
        '''



class CarouselComponent:
    def __init__(self, images):
        self.images = images

    def render(self):
        image_tags = ''.join([f'<img src="{image}" class="carousel-image">' for image in self.images])
        return f'''
            <div class="carousel-container">
                <div class="carousel-content">
                    {image_tags}
                </div>
                <button class="carousel-button" onclick="prevSlide()">❮</button>
                <button class="carousel-button" onclick="nextSlide()">❯</button>
            </div>
            <script>
                var slideIndex = 0;

                function showSlide(n) {{
                    var slides = document.getElementsByClassName('carousel-image');
                    if (n >= slides.length) {{ slideIndex = 0; }}
                    if (n < 0) {{ slideIndex = slides.length - 1; }}
                    for (var i = 0; i < slides.length; i++) {{
                        slides[i].style.display = 'none';
                    }}
                    slides[slideIndex].style.display = 'block';
                }}

                function nextSlide() {{
                    showSlide(slideIndex += 1);
                }}

                function prevSlide() {{
                    showSlide(slideIndex -= 1);
                }}

                showSlide(slideIndex);
            </script>
            <style>
                .carousel-container {{
                    position: relative;
                    max-width: 800px;
                    margin: auto;
                }}

                .carousel-content {{
                    display: flex;
                    overflow: hidden;
                }}

                .carousel-image {{
                    display: none;
                    width: 100%;
                }}

                .carousel-button {{
                    position: absolute;
                    top: 50%;
                    font-size: 30px;
                    cursor: pointer;
                    color: #333;
                    background: none;
                    border: none;
                    transition: 0.3s;
                }}

                .carousel-button:hover {{
                    color: #000;
                }}

                .carousel-button:focus {{
                    outline: none;
                }}

                .carousel-button:first-child {{
                    left: 0;
                }}

                .carousel-button:last-child {{
                    right: 0;
                }}
            </style>
        '''




class ProgressBarComponent:
    def __init__(self, max_value):
        self.max_value = max_value

    def render(self):
        return f'''
            <div class="progress-container">
                <div class="progress-bar"></div>
            </div>
            <style>
                .progress-container {{
                    width: 100%;
                    background-color: #f3f3f3;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }}

                .progress-bar {{
                    width: 0;
                    height: 30px;
                    text-align: center;
                    line-height: 30px;
                    color: white;
                    background-color: #4caf50;
                    border-radius: 5px;
                }}
            </style>
            <script>
                var progressValue = 0;
                var maxProgress = {self.max_value};
                var progressBar = document.querySelector('.progress-bar');

                function updateProgressBar() {{
                    if (progressValue < maxProgress) {{
                        progressValue++;
                        progressBar.style.width = (progressValue / maxProgress * 100) + '%';
                        progressBar.innerHTML = progressValue + '%';
                        setTimeout(updateProgressBar, 50);
                    }}
                }}

                updateProgressBar();
            </script>
        '''
        
                                                    
                                                                                                                                                            