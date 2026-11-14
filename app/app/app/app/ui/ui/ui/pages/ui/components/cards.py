from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel

class StatCard(QFrame):
    def __init__(self, title: str, value: str, subtitle: str = ""):
        super().__init__()
        self.setObjectName("card")
        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        t = QLabel(title)
        t.setObjectName("cardTitle")
        layout.addWidget(t)

        v = QLabel(value)
        v.setObjectName("cardValue")
        layout.addWidget(v)

        if subtitle:
            s = QLabel(subtitle)
            s.setStyleSheet("color: #858B96; font-size: 12px;")
            layout.addWidget(s)
