import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsRectItem, QApplication, QWidget, QGraphicsEllipseItem
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt

# QGraphicsView 有点像QLabel
class MainWindow(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        # Defining a scene rect of 400x200, with it's origin at 0,0.
        # If we don't set this on creation, we can set it later with .setSceneRect
        self.scene = QGraphicsScene(0, 0, 400, 200)

        # Draw a rectangle item, setting the dimensions.
        self.rect = QGraphicsRectItem(0, 0, 200, 50)
        self.rect.setPos(50, 20)
        
        # Define the brush (fill).
        brush = QBrush(Qt.red)
        self.rect.setBrush(brush)
        # Define the pen (line)
        pen = QPen(Qt.cyan)
        pen.setWidth(10)
        self.rect.setPen(pen)
        
        
        
        self.ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
        self.ellipse.setPos(75, 30)
        pen.setColor(Qt.green)
        pen.setWidth(5)
        self.ellipse.setPen(pen)
        brush.setColor(Qt.blue)
        self.ellipse.setBrush(brush)
        
        
        self.ellipse.setZValue(2)
        self.rect.setZValue(1)
        
        self.ellipse.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        
        

        
        
        # Add the items to the scene. Items are stacked in the order they are added.
        self.scene.addItem(self.ellipse)
        self.scene.addItem(self.rect)
        self.setScene(self.scene)





if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()