"""ASTERON sidebar navigation."""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtCore import Signal, Qt

NAV_ITEMS = [
    ("home", "Home"),
    ("drives", "USB Drives"),
    ("library", "ISO Library"),
    ("boot_menu", "Boot Menu"),
    ("compatibility", "Compatibility"),
    ("downloads", "Downloads"),
    ("settings", "Settings"),
    ("about", "About"),
]

class AsteronSidebar(QWidget):
    page_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.setObjectName("sidebar")
        self.setFixedWidth(220)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        logo = QLabel("ASTERON")
        logo.setObjectName("logoLabel")
        layout.addWidget(logo)

        slogan = QLabel("BEYOND BOOTING.")
        slogan.setObjectName("sloganLabel")
        layout.addWidget(slogan)

        self.buttons = {}
        for key, label in NAV_ITEMS:
            btn = QPushButton(label)
            btn.setObjectName("navButton")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked=False, k=key: self._on_click(k))
            layout.addWidget(btn)
            self.buttons[key] = btn

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

    def _on_click(self, key: str):
        self.set_active(key)
        self.page_changed.emit(key)

    def set_active(self, key: str):
        for k, btn in self.buttons.items():
            btn.setProperty("active", "true" if k == key else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)
