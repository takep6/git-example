import sys
import threading

import keyboard  # グローバルホットキー用
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QVBoxLayout, QWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel("Enter your name")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        self.setLayout(layout)


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

        # グローバルショートカット設定
        threading.Thread(target=self.setup_hotkey, daemon=True).start()

    def setup_hotkey(self):
        keyboard.add_hotkey('ctrl+shift+h', self.show_window)

    def show_window(self):
        if not self.window.isVisible():
            self.window.show()
        else:
            # 画面を最前面に
            flags = self.window.windowFlags()
            self.window.setWindowFlags(flags | Qt.WindowStaysOnTopHint)
            self.window.show()
            self.window.raise_()
            self.window.activateWindow()
            self.window.setWindowFlags(flags)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = MainApp()
    app.run()
