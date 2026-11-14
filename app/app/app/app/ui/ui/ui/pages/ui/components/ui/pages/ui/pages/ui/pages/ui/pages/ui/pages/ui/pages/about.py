from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("About ASTERON")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        msg = QLabel("ASTERON v0.1.0\nPhase 1 - UI Foundation\n\nBEYOND BOOTING.")
        msg.setStyleSheet("color: #858B96; font-size: 14px;")
        layout.addWidget(msg)
        layout.setAlignment(Qt.AlignTop)
