from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("Settings")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        msg = QLabel("Theme switching and settings coming soon.")
        msg.setStyleSheet("color: #858B96; font-size: 14px;")
        layout.addWidget(msg)
        layout.setAlignment(Qt.AlignTop)
