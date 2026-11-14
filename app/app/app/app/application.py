"""ASTERON main window."""
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from ui.sidebar import AsteronSidebar
from ui.theme import apply_theme
from ui.pages.dashboard import DashboardPage
from ui.pages.drives import DrivesPage
from ui.pages.library import LibraryPage
from ui.pages.boot_menu import BootMenuPage
from ui.pages.compatibility import CompatibilityPage
from ui.pages.downloads import DownloadsPage
from ui.pages.settings import SettingsPage
from ui.pages.about import AboutPage

class AsteronApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASTERON")
        self.setMinimumSize(1100, 700)
        self.resize(1280, 800)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = AsteronSidebar()
        self.sidebar.page_changed.connect(self.switch_page)
        layout.addWidget(self.sidebar)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack, 1)

        self.pages = {
            "home": DashboardPage(),
            "drives": DrivesPage(),
            "library": LibraryPage(),
            "boot_menu": BootMenuPage(),
            "compatibility": CompatibilityPage(),
            "downloads": DownloadsPage(),
            "settings": SettingsPage(),
            "about": AboutPage(),
        }

        for page in self.pages.values():
            self.stack.addWidget(page)

        self.stack.setCurrentWidget(self.pages["home"])
        self.sidebar.set_active("home")

        self.current_theme = "dark"
        apply_theme(self.current_theme)

    def switch_page(self, key: str):
        if key in self.pages:
            self.stack.setCurrentWidget(self.pages[key])
