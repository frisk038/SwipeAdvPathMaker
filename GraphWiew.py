import time
import re
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
    newPathLayout = None

    def __init__(self, newPathLayout):
        super(GraphWiew, self).__init__()
        scene = QGraphicsScene(self)
        self.setScene(scene)
        self.newPathLayout = newPathLayout
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setSceneRect(0, 0, 2000, 2000)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        try:
            self.loadNetwork()
            self.loadNetworkLayout()
        except Exception as e:
            print('fail to load graph view' + str(e))

    def loadEdges(self):
        for node in self.jsondt:
            try:
                if node['p'][0] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][0]], self.scene()))
            except Exception as e:
                pass

            try:
                if node['p'][1] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][1]], self.scene()))
            except Exception as e:
                pass
            try:
                if node['p'][2] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][2]], self.scene()))
            except Exception as e:
                pass
            try:
                if node['p'][3] in self.nodes:
                    self.edges.append(
                        Edge(self.nodes[node['i']], self.nodes[node['p'][3]], self.scene()))
            except Exception as e:
                pass

    def loadNodes(self):
        prog = re.compile(r"(?<=center\])(.*?)(?=\[\/center)")
        for node in self.jsondt:
            if node['i'] not in self.nodes:
                self.nodes[node['i']] = Node(
                    str(node['i']), self.scene(), Path(node['a'], prog.search(node['d']).group(0), node['i'],
                                                       node['p'][0], node['p'][1], node['p'][2], node['p'][3],
                                                       node['s'], node['l'], node['k'],
                                                       node['n'], prog.search(node['lt']).group(
                                                           0), prog.search(node['ut']).group(0),
                                                       prog.search(node['rt']).group(0), prog.search(node['dt']).group(0), node['loc']),
                    self.newPathLayout)

    def clear(self):
        self.edges.clear()
        for node in self.nodes:
            self.nodes[node].edges.clear()
        self.scene().clear()
        self.nodes.clear()

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
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):
        self.newPathLayout.clearForm()
        super().mousePressEvent(event)

    def updateJSONData(self, newNode):
        for i in range(len(self.jsondt)):
            if self.jsondt[i]["i"] == newNode["i"]:
                self.jsondt[i] = newNode
                return
        self.jsondt.append(newNode)

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
            "n": newPath.vname,
            "lt": newPath.ltxt,
            "ut": newPath.utxt,
            "rt": newPath.rtxt,
            "dt": newPath.dtxt,
            "loc": newPath.location
        }

        self.updateJSONData(node)
        with open('path.json', 'w') as outfile:
            json.dump(self.jsondt, outfile, indent=4, ensure_ascii=False)
        self.loadNetwork()
        self.loadNetworkLayout()
