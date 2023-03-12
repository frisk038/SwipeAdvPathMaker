#!/usr/bin/env python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QTextEdit, QLabel, QLineEdit, QHBoxLayout, QComboBox)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene,
                             QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtWebEngineWidgets import *

from GraphWiew import *
from Path import *


def createMainLayout():
    hLayout = QHBoxLayout()
    vLayout1 = QVBoxLayout()
    vLayout2 = QVBoxLayout()
    hLayout.addLayout(vLayout1)
    hLayout.addLayout(vLayout2)
    return hLayout, vLayout1, vLayout2


def createNewPathLayout(vLayout1):
    po = QHBoxLayout()
    po.addWidget(QLabel("index"))
    index = QLineEdit('')
    po.addWidget(index)
    vLayout1.addLayout(po)

    description = QTextEdit('')
    vLayout1.addWidget(description)

    po = QHBoxLayout()
    po.addWidget(QLabel("imgpath"))
    imgpath = QLineEdit('')
    po.addWidget(imgpath)
    vLayout1.addLayout(po)

    hLayout1 = QHBoxLayout()
    left = QLineEdit('')
    up = QLineEdit('')
    right = QLineEdit('')
    down = QLineEdit('')
    special = QComboBox()
    special.addItem("Normal")
    special.addItem("Luck")
    special.addItem("Combat")
    vname = QLineEdit('_')
    avatar = QLineEdit('_')
    life = QLineEdit('0')
    atk = QLineEdit('0')
    hLayout1.addWidget(QLabel('Left'))
    hLayout1.addWidget(left)
    hLayout1.addWidget(QLabel('Up'))
    hLayout1.addWidget(up)
    hLayout1.addWidget(QLabel('Right'))
    hLayout1.addWidget(right)
    hLayout1.addWidget(QLabel('Down'))
    hLayout1.addWidget(down)
    hLayout1.addWidget(special)
    vLayout1.addLayout(hLayout1)

    po = QHBoxLayout()
    po.addWidget(QLabel("ltxt"))
    ltxt = QLineEdit('')
    po.addWidget(ltxt)
    vLayout1.addLayout(po)

    po = QHBoxLayout()
    po.addWidget(QLabel("utxt"))
    utxt = QLineEdit('')
    po.addWidget(utxt)
    vLayout1.addLayout(po)

    po = QHBoxLayout()
    po.addWidget(QLabel("rtxt"))
    rtxt = QLineEdit('')
    po.addWidget(rtxt)
    vLayout1.addLayout(po)

    po = QHBoxLayout()
    po.addWidget(QLabel("dtxt"))
    dtxt = QLineEdit('')
    po.addWidget(dtxt)
    vLayout1.addLayout(po)

    po = QHBoxLayout()
    po.addWidget(QLabel("Name"))
    po.addWidget(vname)
    vLayout1.addLayout(po)

    po = QHBoxLayout()
    po.addWidget(QLabel("Avatar"))
    po.addWidget(avatar)
    vLayout1.addLayout(po)

    po = QHBoxLayout()
    po.addWidget(QLabel("Life"))
    po.addWidget(life)
    vLayout1.addLayout(po)

    po = QHBoxLayout()
    po.addWidget(QLabel("ATK"))
    po.addWidget(atk)
    vLayout1.addLayout(po)

    crtbtn = QPushButton('Add')
    crtbtn.clicked.connect(on_create_click)
    vLayout1.addWidget(crtbtn)

    return PathLayout(imgpath, description, index,
                      left, up, right, down, crtbtn,
                      special, life, atk, vname, avatar,
                      ltxt, utxt, rtxt, dtxt)


def createGraphViewLayout(vLayout2):
    selectInfo = QLabel('...')
    selectInfo.setWordWrap(True)
    a = GraphWiew(newPathLayout)
    vLayout2.addWidget(a)
    vLayout2.addWidget(selectInfo)
    hLayout2 = QHBoxLayout()
    vLayout2.addLayout(hLayout2)
    svbtn = QPushButton('Save')
    svbtn.clicked.connect(on_save_click)
    hLayout2.addWidget(svbtn)
    ldbtn = QPushButton('Load')
    ldbtn.clicked.connect(on_load_click)
    hLayout2.addWidget(ldbtn)
    return a


def on_create_click():
    if len(newPathLayout.index.text()) > 0 and len(newPathLayout.description.toPlainText()) > 0 \
            and len(newPathLayout.imgpath.text()) > 0 and len(newPathLayout.left.text()) > 0 \
            and len(newPathLayout.up.text()) > 0 and len(newPathLayout.right.text()) > 0 \
            and len(newPathLayout.down.text()) > 0:
        graph.addNode(newPathLayout.toPath())
        newPathLayout.clearForm()
    else:
        print('Error : some fields are missing')


def on_save_click():
    with open("save.lyt", 'w') as out:
        for node in graph.nodes:
            out.write(str(node) + ';' + graph.nodes[node].ndtxt.toPlainText() + ';' + str(
                graph.nodes[node].pos().x()) + ';' + str(graph.nodes[node].pos().y()) + '\n')


def on_load_click():
    graph.loadNetworkLayout()


app = QApplication([])
window = QWidget()

hLayout, vLayout1, vLayout2 = createMainLayout()
newPathLayout = createNewPathLayout(
    vLayout1)
graph = createGraphViewLayout(vLayout2)

window.setLayout(hLayout)
window.setWindowTitle("Choice Network")
window.show()
app.exec_()
