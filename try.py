import sys
import os
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
import subprocess

class MyForm(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)

        self.pushButton_2=QtGui.QPushButton("Start")
        self.pushButton_Selection=QtGui.QPushButton("Stop")

        self.pushButton_2.clicked.connect(self.print_LineEdit)
        self.pushButton_Selection.clicked.connect(self.print_Selection)

        vbox=QtGui.QVBoxLayout()
        vbox.addWidget(self.pushButton_2)
        vbox.addWidget(self.pushButton_Selection)
        self.setLayout(vbox)

    def print_LineEdit(self):
        QtGui.QMessageBox.about(self, 'Status',"Started Recording")
	print "Recording Started"
        p = subprocess.Popen('ffmpeg -f alsa -i hw:1,0 -itsoffset 00:00:00 -f video4linux2 -i /dev/video0 out1.avi', shell = True)
            

    def print_Selection(self):
        os.system('killall ffmpeg')
        QtGui.QMessageBox.about(self, 'Status', "Stopped Recording")
        print "Recording Stopped"
        parent_window = self
        title = "Video_name"
        message = "Enter a name for your video"
        video_name, ok = QtGui.QInputDialog.getText(parent_window, title, message)
        print video_name
        os.system("mv out1.avi %s.avi"%video_name)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = MyForm()
    MainWindow.show()
    sys.exit(app.exec_())

