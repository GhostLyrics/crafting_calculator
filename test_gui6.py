import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from html import escape


def render_textboxes(items):
    """Renders a list of textboxes where the label is the item name and the textbox will be for a quantity.

    Args:
        items: A list of items, where each item is a tuple of (name, quantity).

    Returns:
        A string containing the HTML code for the textboxes.
    """

    textboxes = []
    for name, quantity in items:
        label_html = f"<label>{escape(name)}</label>"
        input_html = f'<input type="number" value="{escape(str(quantity))}">'
        paragraph_html = f"<p>{label_html}{input_html}</p>"
        textboxes.append(paragraph_html)

    return "".join(textboxes)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HTML Render Example")
        self.setGeometry(100, 100, 800, 600)

        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)

        items = [("Item 1", 10), ("Item 2", 5), ("Item 3", 2)]
        html_content = render_textboxes(items)

        self.webview.setHtml(html_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
