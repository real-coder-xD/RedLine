import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QIcon
from PyQt6.QtCore import Qt


class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.draw_flag = True  # trạng thái hiển thị các vạch
        self.setWindowTitle("Overlay Ruler")

        # Hiển thị trên taskbar, topmost, frameless
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Window
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Đặt icon
        self.setWindowIcon(QIcon("icon.ico"))  # đổi thành đường dẫn icon của bạn

        # Fullscreen
        self.showFullScreen()

        # Lấy thông số màn hình
        screen = QApplication.primaryScreen()
        self.width = screen.size().width()
        self.height = screen.size().height()
        self.center_x = self.width // 2
        self.center_y = self.height // 2

        # Cấu hình thước
        self.short_len = 50
        self.long_len = 300
        self.spacing = 120

    def paintEvent(self, event):
        if not self.draw_flag:
            return  # không vẽ gì nếu tắt

        painter = QPainter(self)
        pen = QPen(QColor("white"))
        pen.setWidth(1)
        painter.setPen(pen)

        # Đường ngang chính
        painter.drawLine(0, self.center_y, self.width, self.center_y)

        # Các đường dọc
        for x in range(0, self.width, self.spacing):
            v_len = self.long_len if x == self.center_x else self.short_len
            painter.drawLine(x, self.center_y - v_len, x, self.center_y + v_len)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            QApplication.quit()
        elif event.key() == Qt.Key.Key_F1:
            self.draw_flag = not self.draw_flag
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    sys.exit(app.exec())
