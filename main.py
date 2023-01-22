import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)  # changed this line
        self.showMaximized()

        #navbar buttons
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        #forward buttons
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        #forward buttons
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        #home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        #search bar field
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)



    def update_url(self , q):
        self.url_bar.setText(q.toString())

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))





    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

app = QApplication(sys.argv)
QApplication.setApplicationName('cool browsers')
window = MainWindow()
window.show() # added this line
sys.exit(app.exec_()) # changed this line
