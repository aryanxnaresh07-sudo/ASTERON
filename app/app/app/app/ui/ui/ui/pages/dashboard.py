"""Home Dashboard."""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PySide6.QtCore import Qt
from ui.components.cards import StatCard

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 32, 40, 32)
        layout.setSpacing(24)

        title = QLabel("Home")
        title.setObjectName("pageTitle")
        layout.addWidget(title)

        subtitle = QLabel("Manage your multiboot USB drives and ISO library.")
        subtitle.setObjectName("pageSubtitle")
        layout.addWidget(subtitle)

        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        cards_row.addWidget(StatCard("USB DRIVE", "Not connected", "Connect a USB drive to begin"))
        cards_row.addWidget(StatCard("CAPACITY", "—", "No device selected"))
        cards_row.addWidget(StatCard("ISO LIBRARY", "0 ISOs", "Add ISO files to get started"))
        cards_row.addWidget(StatCard("BOOT STATUS", "Not prepared", "USB is not multiboot ready"))
        layout.addLayout(cards_row)

        actions_row = QHBoxLayout()
        actions_row.setSpacing(12)

        create_btn = QPushButton("Create Multiboot USB")
        create_btn.setObjectName("primaryButton")
        create_btn.setEnabled(False)
        actions_row.addWidget(create_btn)

        add_iso_btn = QPushButton("Add ISO")
        add_iso_btn.setObjectName("secondaryButton")
        add_iso_btn.setEnabled(False)
        actions_row.addWidget(add_iso_btn)

        actions_row.addStretch()
        layout.addLayout(actions_row)

        empty_frame = QFrame()
        empty_frame.setObjectName("card")
        empty_layout = QVBoxLayout(empty_frame)
        empty_layout.setAlignment(Qt.AlignCenter)

        icon = QLabel("⬡")
        icon.setStyleSheet("font-size: 48px; color: #3478F6;")
        icon.setAlignment(Qt.AlignCenter)
        empty_layout.addWidget(icon)

        empty_title = QLabel("No USB Drive Connected")
        empty_title.setStyleSheet("font-size: 18px; font-weight: 600; color: #D9DDE3;")
        empty_title.setAlignment(Qt.AlignCenter)
        empty_layout.addWidget(empty_title)

        layout.addWidget(empty_frame, 1)
