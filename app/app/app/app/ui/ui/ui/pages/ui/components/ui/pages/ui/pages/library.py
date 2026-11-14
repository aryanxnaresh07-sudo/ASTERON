from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class LibraryPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("ISO Library")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        msg = QLabel("ISO management coming in Phase 6.")
        msg.setStyleSheet("color: #858B96; font-size: 14px;")
        layout.addWidget(msg)
        layout.setAlignment(Qt.AlignTop)
