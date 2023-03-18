class PathLayout():
    imgpath = None
    description = None
    index = None
    left = None
    up = None
    right = None
    down = None
    crtbtn = None
    special = None
    life = None
    atk = None
    vname = None
    ltxt = None
    utxt = None
    rtxt = None
    dtxt = None

    def __init__(self, imgpath, description, index,
                 left, up, right, down, crtbtn, special,
                 life, atk, vname, ltxt, utxt,
                 rtxt, dtxt):
        self.imgpath = imgpath
        self.description = description
        self.index = index
        self.left = left
        self.up = up
        self.right = right
        self.down = down
        self.crtbtn = crtbtn
        self.special = special
        self.life = life
        self.atk = atk
        self.vname = vname
        self.ltxt = ltxt
        self.utxt = utxt
        self.rtxt = rtxt
        self.dtxt = dtxt

    def clearForm(self):
        self.index.clear()
        self.description.clear()
        self.imgpath.clear()
        self.left.clear()
        self.up.clear()
        self.right.clear()
        self.down.clear()
        self.ltxt.clear()
        self.utxt.clear()
        self.rtxt.clear()
        self.dtxt.clear()
        self.life.setText("0")
        self.atk.setText("0")
        self.vname.setText("_")
        self.special.setCurrentIndex(0)

    def toPath(self):
        return Path(self.imgpath.text(),
                    "[center]%s[/center]" % self.description.toPlainText(),
                    self.index.text(),
                    self.left.text(),
                    self.up.text(),
                    self.right.text(),
                    self.down.text(),
                    self.special.currentText(),
                    self.life.text(),
                    self.atk.text(),
                    self.vname.text(),
                    "[center]%s[/center]" % self.ltxt.text(),
                    "[center]%s[/center]" % self.utxt.text(),
                    "[center]%s[/center]" % self.rtxt.text(),
                    "[center]%s[/center]" % self.dtxt.text())


class Path():
    imgpath = ""
    description = ""
    index = ""
    left = ""
    up = ""
    right = ""
    down = ""
    special = ""
    life = ""
    atk = ""
    vname = ""
    ltxt = ""
    utxt = ""
    rtxt = ""
    dtxt = ""

    def __init__(self, imgpath, description, index,
                 left, up, right, down, special, life,
                 atk, vname, ltxt, utxt, rtxt, dtxt):
        self.imgpath = imgpath
        self.description = description
        self.index = index
        self.left = left
        self.up = up
        self.right = right
        self.down = down
        self.special = special
        self.life = life
        self.atk = atk
        self.vname = vname
        self.ltxt = ltxt
        self.utxt = utxt
        self.rtxt = rtxt
        self.dtxt = dtxt
