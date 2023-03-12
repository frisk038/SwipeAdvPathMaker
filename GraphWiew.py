from PyQt5.QtWidgets import (QGraphicsView, QGraphicsScene)
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

import json
from Node import *
from Path import *


class GraphWiew(QGraphicsView):
    nodes = {}
    edges = []
    jsondt = []

    def __init__(self, selectInfo):
        super(GraphWiew, self).__init__()

        scene = QGraphicsScene(self)
        self.setScene(scene)
        self.selectInfo = selectInfo
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setSceneRect(0, 0, 2000, 2000)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        try:
            self.loadNetwork()
            self.loadNetworkLayout()
        except:
            pass

    def loadEdges(self):
        for node in self.jsondt:
            try:
                if node['p'][0] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][0]], self.scene()))
            except:
                pass

            try:
                if node['p'][1] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][1]], self.scene()))
            except:
                pass
            try:
                if node['p'][2] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][2]], self.scene()))
            except:
                pass
            try:
                if node['p'][3] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][3]], self.scene()))
            except:
                pass

    def loadNodes(self):
        for node in self.jsondt:
            if node['i'] not in self.nodes:
                self.nodes[node['i']] = Node(
                    str(node['i']), self.scene(), node['d'], self.selectInfo)

    def clear(self):
        for edge in self.edges:
            self.scene().removeItem(edge)
            self.edges.clear()
        for node in self.nodes:
            self.nodes[node].edges.clear()

    def loadNetwork(self):
        with open('path.json', 'r') as f:
            self.jsondt = json.load(f)
            self.clear()
            self.loadNodes()
            self.loadEdges()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_C:
            for edge in self.edges:
                self.scene().removeItem(edge)
            self.edges.clear()
        if key == Qt.Key_N:
            self.loadNetwork()
        super(GraphWiew, self).keyPressEvent(event)

    def loadNetworkLayout(self):
        try:
            with open("save.lyt", 'r') as fp:
                line = fp.readline().rstrip()
                while line:
                    saved = line.split(';')
                    self.nodes[int(saved[0])].setPos(
                        float(saved[2]), float(saved[3]))
                    line = fp.readline().rstrip()
        except:
            pass

    def addNode(self, newPath):
        node = {
            "i": int(newPath.index),
            "d": newPath.description,
            "a": newPath.imgpath,
            "p": [
                int(newPath.left),
                int(newPath.up),
                int(newPath.right),
                int(newPath.down)
            ],
            "s": newPath.special,
            "l": int(newPath.life),
            "k": int(newPath.atk),
            "v": newPath.avatar,
            "n": newPath.vname,
            "lt": newPath.ltxt,
            "ut": newPath.utxt,
            "rt": newPath.rtxt,
            "dt": newPath.dtxt
        }
        self.jsondt.append(node)
        with open('path.json', 'w') as outfile:
            json.dump(self.jsondt, outfile, indent=4, ensure_ascii=False)
        self.loadNetwork()
        self.loadNetworkLayout()
