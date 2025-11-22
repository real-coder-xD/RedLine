import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont, QIcon
from PyQt6.QtCore import Qt


class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.draw_flag = True
        self.setWindowTitle("Overlay Ruler")

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Window
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowIcon(QIcon("icon.ico"))
        self.showFullScreen()

        screen = QApplication.primaryScreen()
        self.width = screen.size().width()
        self.height = screen.size().height()
        self.center_x = self.width // 2
        self.center_y = self.height // 2

        self.short_len = 50
        self.long_len = 300
        self.spacing = 120

    def paintEvent(self, event):
        if not self.draw_flag:
            return

        painter = QPainter(self)
        pen = QPen(QColor("red"))
        pen.setWidth(1)
        painter.setPen(pen)

        font = QFont("Arial", 10)
        painter.setFont(font)

        # Đường ngang chính
        painter.drawLine(0, self.center_y, self.width, self.center_y)

        # Các đường dọc và số px nằm ngang
        for x in range(0, self.width, self.spacing):
            if x == 0:
                continue  # bỏ vạch và số 0px
            v_len = self.long_len if x == self.center_x else self.short_len
            painter.drawLine(x, self.center_y - v_len, x, self.center_y + v_len)

            # Vẽ số px dưới trục ngang
            text = str(x)
            text_width = painter.fontMetrics().horizontalAdvance(text)
            painter.drawText(x - text_width // 2, self.center_y + v_len + 15, text)

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
