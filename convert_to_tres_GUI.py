from convert_to_tres import convert

import sys
import time

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget, \
    QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFileDialog, QLabel, QProgressBar


class GUI(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(480, 360)
        self.center()
        self.setWindowTitle('AnimatedTexture converter')    

        # Whole window
        layout = QVBoxLayout()

        # First line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Input (GIF/video):')
        h_layout.addWidget(nameLabel)
        h_layout.addWidget(QLineEdit(self))
        input_btn = QPushButton('Browse..')
        input_btn.clicked.connect(self.chooseInput)
        h_layout.addWidget(input_btn)
        layout.addLayout(h_layout)

        # Second line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Output (frames):')
        h_layout.addWidget(nameLabel)
        h_layout.addWidget(QLineEdit(self))
        output_frames_btn = QPushButton('Browse..')
        output_frames_btn.clicked.connect(self.chooseOuputFrames)
        h_layout.addWidget(output_frames_btn)
        layout.addLayout(h_layout)

        # Third Line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Output (.tres AnimatedTexture):')
        h_layout.addWidget(nameLabel)
        h_layout.addWidget(QLineEdit(self))
        output_texture_btn = QPushButton('Browse..')
        output_texture_btn.clicked.connect(self.chooseOuputTexture)
        h_layout.addWidget(output_texture_btn)
        layout.addLayout(h_layout)

        # Fourth Line
        convert_btn = QPushButton('CONVERT')
        convert_btn.clicked.connect(self.startConversion)
        layout.addWidget(convert_btn)

        # Fifth Line
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)
        self.progress_bar.hide()

        # Sixth Line
        self.log_label = QLabel(self)
        self.log_label.setText('Chose input gif or video, select your destination folder and hit CONVERT')
        layout.addWidget(self.log_label)
        
        self.setLayout(layout)

        self.show()

    def center(self):     
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def chooseInput(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        #dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()

    def chooseOuputFrames(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        #dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()

    def chooseOuputTexture(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        #dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            
    def startConversion(self):
        self.progress_bar.show()
        count = 0
        while count < 10:
            count += 1
            time.sleep(1)
            self.progress_bar.setValue(count)
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Exit',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
