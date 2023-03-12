from PyQt5.QtWebEngineWidgets import *
import math
from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QSizeF)
from PyQt5.QtGui import (QColor, QRadialGradient, QPen, QPainterPath,
                         QPolygonF, QFont)
from PyQt5.QtWidgets import (QGraphicsItem, QStyle,  QGraphicsTextItem)


class NodeText(QGraphicsTextItem):
    def __init__(self, text, parent, font=QFont("Arial", 15)):
        super(NodeText, self).__init__(text, parent)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setFont(font)
        self.setSelected(True)


class Node(QGraphicsItem):
    selectInfo = None
    edges = []

    def __init__(self, label, scene, description, selectInfo):
        super(Node, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(-1)
        self.ndtxt = NodeText(label, self)
        self.description = description
        self.selectInfo = selectInfo
        scene.addItem(self)

    def addEdge(self, edge):
        self.edges.append(edge)

    def edge(self):
        return self.edges

    def paint(self, painter, option, widget):
        gradient = QRadialGradient(-3, -3, 10)
        if option.state & QStyle.State_Sunken:
            gradient.setCenter(3, 3)
            gradient.setFocalPoint(3, 3)
            gradient.setColorAt(1, QColor(Qt.red).lighter(120))
            gradient.setColorAt(0, QColor(Qt.darkRed).lighter(120))
        else:
            gradient.setColorAt(0, Qt.red)
            gradient.setColorAt(1, Qt.darkRed)

        painter.setBrush(gradient)
        painter.setPen(QPen(Qt.black, 0))
        painter.drawEllipse(-10, -10, 20, 20)

    def boundingRect(self):
        adjust = 2
        return QRectF(-10 - adjust, -10 - adjust, 23 + adjust, 23 + adjust)

    def shape(self):
        path = QPainterPath()
        path.addEllipse(-10, -10, 20, 20)
        return path

    def mousePressEvent(self, event):
        self.selectInfo.setText(self.description)
        self.update()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.update()
        super().mouseReleaseEvent(event)

    def itemChange(self, change, value):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
            for edge in self.edges:
                edge.adjust()
        return super().itemChange(change, value)


class Edge(QGraphicsItem):
    sourcePoint = QPointF()
    destPoint = QPointF()
    arrowSize = 5
    src = None
    dst = None

    def __init__(self, src, dst, scene):
        super(Edge, self).__init__()
        self.src = src
        self.dst = dst
        src.addEdge(self)
        dst.addEdge(self)
        self.adjust()
        scene.addItem(self)

    def adjust(self):
        line = QLineF(self.mapFromItem(self.src, 0, 0),
                      self.mapFromItem(self.dst, 0, 0))
        length = line.length()

        self.prepareGeometryChange()

        if (length > 20):
            edgeOffset = QPointF((line.dx() * 10) / length,
                                 (line.dy() * 10) / length)
            self.sourcePoint = line.p1() + edgeOffset
            self.destPoint = line.p2() - edgeOffset
        else:
            self.sourcePoint = self.destPoint = line.p1()

    def paint(self, painter, option, widget):
        line = QLineF(self.sourcePoint, self.destPoint)
        if line.length() == 0:
            return

        painter.setPen(QPen(Qt.white, 1, Qt.SolidLine,
                       Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(line)
        angle = math.atan2(-line.dy(), line.dx())

        destArrowP1 = QPointF(self.destPoint + QPointF(math.sin(angle - math.pi / 3)
                              * self.arrowSize, math.cos(angle - math.pi / 3) * self.arrowSize))
        destArrowP2 = QPointF(self.destPoint + QPointF(math.sin(angle - math.pi + math.pi / 3)
                              * self.arrowSize, math.cos(angle - math.pi + math.pi / 3) * self.arrowSize))

        painter.setBrush(Qt.white)

        pf = QPolygonF()
        pf.append(line.p2())
        pf.append(destArrowP1)
        pf.append(destArrowP2)
        painter.drawPolygon(pf)

    def boundingRect(self):
        if self.src == None or self.dst == None:
            return QRectF()

        penWidth = 1
        extra = (penWidth + self.arrowSize) / 2.0

        return QRectF(self.sourcePoint, QSizeF(self.destPoint.x() - self.sourcePoint.x(),
                                               self.destPoint.y() - self.sourcePoint.y())).normalized().adjusted(-extra, -extra, extra, extra)
