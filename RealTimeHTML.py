import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Real Time HTML Editor')
        self.showMaximized()

        #Creating Defautl HTML
        self.html = """ <h2>Welcome to Matt's HTML Editor </h2>

<p> Enter Your HTML in the Left Window and it will Display in the Right Window</p> """

        #Creating Widgets
        self.inputHtml = QTextEdit()
        self.inputHtml.setPlainText(self.html)
        self.inputHtml.textChanged.connect(self.updateView)
        self.outputHtml = QWebView()
        self.outputHtml.setHtml(self.html)

        #Adding Widgets to a Layout
        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.inputHtml)
        self.mainLayout.addWidget(self.outputHtml)
        self.mainWidget.setLayout(self.mainLayout)


        
        self.setCentralWidget(self.mainWidget)

        self.menuBar = QMenuBar()
        
        #Creating actions -- File
        self.newFile = QAction("New File", self)
        self.newFile.setShortcut("CTRL+N")
        
        self.open = QAction("Open..", self)
        self.open.setShortcut("CTRL+O")


        

        #Recent Files Menu
        self.openRecent = QMenu("Recent Files")
        self.file1 = QAction("file 1", self)
        self.file2 = QAction("file 2", self)
        self.file3 = QAction("file 3", self)

        self.openRecent.addAction(self.file1)
        self.openRecent.addAction(self.file2)
        self.openRecent.addAction(self.file3)

        self.save = QAction("Save", self)
        self.save.setShortcut("CTRL+S")

        
        self.saveAs = QAction("Save As..", self)
        self.saveAs.setShortcut("CTRL+SHIFT+S")


        #Creating Actions -- Edit

        self.undo = QAction("Undo", self)
        self.undo.setShortcut("CTRL+Z")

        

        #Creating Menus
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.newFile)
        self.fileMenu.addAction(self.open)
        self.fileMenu.addMenu(self.openRecent)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.save)
        self.fileMenu.addAction(self.saveAs)

        self.editMenu = self.menuBar.addMenu("Edit")
        self.editMenu.addAction(self.undo)

        self.setMenuBar(self.menuBar)

    def updateView(self):
        self.html = self.inputHtml.toPlainText()
        self.outputHtml.setHtml(self.html)
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
