"""ASTERON entry point."""
import sys
from PySide6.QtWidgets import QApplication
from app.application import AsteronApplication
from services.logger import setup_logging

def main() -> int:
    setup_logging()
    app = QApplication(sys.argv)
    app.setApplicationName("ASTERON")
    app.setApplicationDisplayName("ASTERON")
    app.setOrganizationName("ASTERON")

    window = AsteronApplication()
    window.show()

    return app.exec()
