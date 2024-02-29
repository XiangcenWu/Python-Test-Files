from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PySide6.QtCore import Qt

class CustomGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super(CustomGraphicsView, self).__init__(scene)

    def mousePressEvent(self, event):
        # Get the mouse position in scene coordinates
        scene_pos = self.mapToScene(event.pos())
        x, y = scene_pos.x(), scene_pos.y()

        # Print or perform actions based on the mouse location
        print(f"Mouse Pressed at Scene Coordinates: ({x}, {y})")

if __name__ == "__main__":
    app = QApplication([])

    scene = QGraphicsScene()
    item = QGraphicsRectItem(0, 0, 100, 100)
    scene.addItem(item)

    view = CustomGraphicsView(scene)
    view.show()

    app.exec()