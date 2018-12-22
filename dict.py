import BingDict
import YoudaoDict
import sys
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def onClicked(self, btn):
        word = self.line.text()
        desc = BingDict.search(word)
        self.bing_text.setPlainText(desc)
        desc = YoudaoDict.search(word)
        self.youdao_text.setPlainText(desc)

    def initUI(self):
        # self.statusBar().showMessage('Ready')

        searchButton = QPushButton("Search")
        self.bing = QLabel()
        self.bing.setText("Bing:")
        self.youdao = QLabel()
        self.youdao.setText("Youdao:")
        self.line = QLineEdit()
        self.bing_text = QPlainTextEdit()
        self.bing_text.setReadOnly(True)

        self.youdao_text = QPlainTextEdit()
        self.youdao_text.setReadOnly(True)

        hbox = QHBoxLayout()
        hbox.addWidget(self.line)
        # hbox.addStretch(1)
        hbox.addWidget(searchButton)
        vbox = QVBoxLayout()

        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(self.bing)
        vbox.addWidget(self.bing_text)
        vbox.addStretch(1)
        vbox.addWidget(self.youdao)
        vbox.addWidget(self.youdao_text)
        searchButton.clicked.connect(self.onClicked)
        self.setLayout(vbox)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Dict')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
