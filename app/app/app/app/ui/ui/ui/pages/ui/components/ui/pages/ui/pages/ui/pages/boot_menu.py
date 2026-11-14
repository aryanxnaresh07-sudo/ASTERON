from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class BootMenuPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("Boot Menu")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        msg = QLabel("Boot menu customization coming in Phase 5.")
        msg.setStyleSheet("color: #858B96; font-size: 14px;")
        layout.addWidget(msg)
        layout.setAlignment(Qt.AlignTop)
