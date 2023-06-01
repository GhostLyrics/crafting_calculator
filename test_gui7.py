import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSlot

# HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        .accordion {
            background-color: #eee;
            color: #444;
            cursor: pointer;
            padding: 18px;
            width: 100%;
            border: none;
            text-align: left;
            outline: none;
            font-size: 15px;
            transition: 0.4s;
        }

        .active, .accordion:hover {
            background-color: #ccc;
        }

        .accordion::after {
            content: '\002B';
            color: #777;
            font-weight: bold;
            float: right;
            margin-left: 5px;
        }

        .active::after {
            content: "\2212";
        }

        .panel {
            padding: 0 18px;
            background-color: white;
            display: none;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <h1>Simple Input-Output Example</h1>

    <button class="accordion">Alchemy</button>
    <div class="panel">
        <p>Content inside the accordion panel.</p>
    </div>
    <button class="accordion">Blacksmithing</button>
    <div class="panel">
        <p>Content inside the accordion panel.</p>
    </div>
    <button class="accordion">Cooking</button>
    <div class="panel">
        <p>Content inside the accordion panel.</p>
    </div>

    <input id="inputField" type="text" size="4" placeholder="Enter text">
    <button id="submitButton">Submit</button>
    <p id="outputText"></p>

    <script src="https://cdn.jsdelivr.net/npm/@qt/qtwebchannel/dist/qtwebchannel.js"></script>
    <script>
        var inputField = document.getElementById('inputField');
        var submitButton = document.getElementById('submitButton');
        var outputText = document.getElementById('outputText');
        var accordion = document.querySelector('.accordion');
        var panel = document.querySelector('.panel');

        accordion.addEventListener('click', function() {
            this.classList.toggle('active');
            panel.style.display = panel.style.display === 'block' ? 'none' : 'block';
        });

        new QWebChannel(qt.webChannelTransport, function (channel) {
            var backend = channel.objects.backend;

            submitButton.addEventListener('click', function () {
                var inputText = inputField.value;
                backend.processInput(inputText);
            });

            backend.textChanged.connect(function (text) {
                outputText.textContent = text;
            });
        });
    </script>
</body>
</html>
"""


class Backend(QObject):
    textChanged = pyqtSlot(str)

    @pyqtSlot(str)
    def processInput(self, inputText):
        # Perform some processing on the input text
        # In this example, we simply echo back the input text
        outputText = "You entered: " + inputText
        # self.textChanged.emit(outputText)
        print(outputText)


app = QApplication(sys.argv)

webview = QWebEngineView()
webchannel = QWebChannel()
backend = Backend()
webchannel.registerObject("backend", backend)
webview.page().setWebChannel(webchannel)

webview.setHtml(html_template, QUrl.fromLocalFile("."))
webview.show()

sys.exit(app.exec_())
