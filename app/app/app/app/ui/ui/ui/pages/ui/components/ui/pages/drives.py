from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class DrivesPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("USB Drives")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        msg = QLabel("USB detection coming in Phase 3.")
        msg.setStyleSheet("color: #858B96; font-size: 14px;")
        layout.addWidget(msg)
        layout.setAlignment(Qt.AlignTop)
