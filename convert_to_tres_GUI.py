from convert_to_tres import convert

import sys
import time
import os

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget, \
        QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFileDialog, QLabel, \
        QProgressBar, QErrorMessage, QComboBox


video_extension = ['.mp4', '.mov', '.webm', '.mkv', '.ogv']

class GUI(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(480, 360)
        self.center()
        self.setWindowTitle('AnimatedTexture creator')    

        # Whole window
        layout = QVBoxLayout()

        # First line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Input (GIF/video):')
        h_layout.addWidget(nameLabel)
        self.input_line = QLineEdit(self)
        # TODO: connect onchange signal
        h_layout.addWidget(self.input_line)
        input_btn = QPushButton('Browse')
        input_btn.clicked.connect(self.chooseInput)
        h_layout.addWidget(input_btn)
        layout.addLayout(h_layout)

        # Second line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Output (frames):')
        h_layout.addWidget(nameLabel)
        self.output_frames_line = QLineEdit(self)
        # TODO: connect onchange signal
        h_layout.addWidget(self.output_frames_line)
        output_frames_btn = QPushButton('Browse')
        output_frames_btn.clicked.connect(self.chooseOuputFrames)
        h_layout.addWidget(output_frames_btn)
        layout.addLayout(h_layout)

        # Third Line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Output (.tres AnimatedTexture):')
        h_layout.addWidget(nameLabel)
        self.output_texture_line = QLineEdit(self)
        # TODO: connect onchange signal
        h_layout.addWidget(self.output_texture_line)
        output_texture_btn = QPushButton('Browse')
        output_texture_btn.clicked.connect(self.chooseOuputTexture)
        h_layout.addWidget(output_texture_btn)
        layout.addLayout(h_layout)

        # Fourth Line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Output FPS:')
        h_layout.addWidget(nameLabel)
        self.fps_line = QLineEdit(self)
        h_layout.addWidget(self.fps_line)
        layout.addLayout(h_layout)

        # Fifth Line
        h_layout = QHBoxLayout()
        nameLabel = QLabel(self)
        nameLabel.setText('Frames image format:')
        h_layout.addWidget(nameLabel)
        self.image_format = QComboBox(self)
        self.image_format.addItem(".jpeg")
        self.image_format.addItem(".jpg")
        self.image_format.addItem(".png")
        self.image_format.addItem(".bmp")
        h_layout.addWidget(self.image_format)
        layout.addLayout(h_layout)

        # Sixth Line
        convert_btn = QPushButton('CONVERT')
        convert_btn.clicked.connect(self.startConversion)
        layout.addWidget(convert_btn)

        # Seventh Line
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)
        self.progress_bar.hide()

        # Eighth Line
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
        dlg.setFileMode(QFileDialog.ExistingFile)
        dlg.setNameFilters(["Video (*.mkv *mp4 *.mov *.ogv *.webm)", "GIF (*gif)"])
        dlg.selectNameFilter("Video (*.mkv *mp4 *.mov *.ogv *.webm)")

        if dlg.exec_():
            # Only one file can be selected
            input_file = dlg.selectedFiles()
            # Double make sure the selected path is a directory
            if not os.path.isfile(input_file[0]): return
            self.input_line.setText(input_file[0])

    def chooseOuputFrames(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)

        if dlg.exec_():
            path = dlg.selectedFiles()
            # Double make sure the selected path is a directory
            if not os.path.isdir(path[0]): return
            self.output_frames_line.setText(path[0])

    def chooseOuputTexture(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setDefaultSuffix(".tres")
        dlg.setNameFilter("(*.tres)")

        if dlg.exec_():
            filename = dlg.selectedFiles()
            self.output_texture_line.setText(filename[0])
            
    def startConversion(self):
        input_file = self.input_line.text()
        output_frames = self.output_frames_line.text()
        output_texture = self.output_texture_line.text()
        fps = self.fps_line.text()

        # Checks if all the required path are valid
        if not input_file or not os.path.isfile(input_file) or not os.path.splitext(input_file)[1] in video_extension:
            self.showError("Input path is not valid!")
            return
        elif not output_frames or not os.path.isdir(output_frames):
            self.showError("Frames output path is not valid!")
            return
        elif not output_texture or os.path.splitext(output_texture)[1] != ".tres":
            self.showError("Terxture output path is not valid!")
            return
        elif fps <= 0:
            self.showError("FPS should be > 0")
            return

        im_format = self.image_format.currentText()
    
        convert(input_file, output_frames, output_texture, fps, im_format)

        '''
        self.progress_bar.show()
        count = 0
        while count < 10:
            count += 1
            time.sleep(1)
            self.progress_bar.setValue(count)
        '''

    def showError(self, msg):
        err = QMessageBox()
        err.setIcon(QMessageBox.Critical)
        err.setText("Error")
        err.setInformativeText(msg)
        err.setWindowTitle("Error")
        err.exec_()
        
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
