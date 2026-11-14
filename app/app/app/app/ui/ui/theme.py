"""ASTERON theme engine."""
from PySide6.QtWidgets import QApplication

DARK_STYLE = """
QMainWindow, QWidget {
    background-color: #101114;
    color: #FFFFFF;
    font-family: "Inter", "Segoe UI", sans-serif;
    font-size: 14px;
}
QWidget#sidebar {
    background-color: #08090C;
    border-right: 1px solid #1E2028;
}
QPushButton#navButton {
    background-color: transparent;
    color: #858B96;
    border: none;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: left;
    font-size: 14px;
    font-weight: 500;
    margin: 2px 12px;
}
QPushButton#navButton:hover {
    background-color: #1A1C23;
    color: #D9DDE3;
}
QPushButton#navButton[active="true"] {
    background-color: #1E2430;
    color: #3478F6;
    font-weight: 600;
}
QLabel#logoLabel {
    color: #FFFFFF;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 24px 16px 16px 16px;
}
QLabel#sloganLabel {
    color: #858B96;
    font-size: 11px;
    letter-spacing: 1px;
    padding: 0 16px 24px 16px;
}
QLabel#pageTitle {
    color: #FFFFFF;
    font-size: 28px;
    font-weight: 700;
    padding: 8px 0;
}
QLabel#pageSubtitle {
    color: #858B96;
    font-size: 14px;
    padding-bottom: 24px;
}
QFrame#card {
    background-color: #1A1C23;
    border: 1px solid #2A2D38;
    border-radius: 12px;
    padding: 20px;
}
QLabel#cardTitle {
    color: #D9DDE3;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
QLabel#cardValue {
    color: #FFFFFF;
    font-size: 24px;
    font-weight: 700;
}
QPushButton#primaryButton {
    background-color: #3478F6;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-size: 14px;
    font-weight: 600;
}
QPushButton#primaryButton:disabled {
    background-color: #2A2D38;
    color: #5A5F6B;
}
QPushButton#secondaryButton {
    background-color: transparent;
    color: #D9DDE3;
    border: 1px solid #2A2D38;
    border-radius: 8px;
    padding: 12px 24px;
    font-size: 14px;
    font-weight: 500;
}
QComboBox {
    background-color: #1A1C23;
    border: 1px solid #2A2D38;
    border-radius: 8px;
    padding: 10px 14px;
    color: #D9DDE3;
    min-width: 160px;
}
"""

LIGHT_STYLE = """
QMainWindow, QWidget {
    background-color: #F4F5F7;
    color: #101114;
    font-family: "Inter", "Segoe UI", sans-serif;
    font-size: 14px;
}
QWidget#sidebar {
    background-color: #FFFFFF;
    border-right: 1px solid #E0E3E8;
}
QPushButton#navButton {
    background-color: transparent;
    color: #858B96;
    border: none;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: left;
    font-size: 14px;
    font-weight: 500;
    margin: 2px 12px;
}
QPushButton#navButton[active="true"] {
    background-color: #EBF1FE;
    color: #3478F6;
    font-weight: 600;
}
QLabel#logoLabel {
    color: #101114;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 24px 16px 16px 16px;
}
QLabel#pageTitle {
    color: #101114;
    font-size: 28px;
    font-weight: 700;
}
QFrame#card {
    background-color: #FFFFFF;
    border: 1px solid #E0E3E8;
    border-radius: 12px;
}
"""

def apply_theme(theme: str):
    app = QApplication.instance()
    if theme == "light":
        app.setStyleSheet(LIGHT_STYLE)
    else:
        app.setStyleSheet(DARK_STYLE)
