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
    avatar = None
    ltxt = None
    utxt = None
    rtxt = None
    dtxt = None

    def __init__(self, imgpath, description, index,
                 left, up, right, down, crtbtn, special,
                 life, atk, vname, avatar, ltxt, utxt,
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
        self.avatar = avatar
        self.ltxt = ltxt
        self.utxt = utxt
        self.rtxt = rtxt
        self.dtxt = dtxt

    def toPath(self):
        return Path(self.imgpath.text(),
                    self.description.toPlainText(),
                    self.index.text(),
                    self.left.text(),
                    self.up.text(),
                    self.right.text(),
                    self.down.text(),
                    self.special.currentText(),
                    self.life.text(),
                    self.atk.text(),
                    self.vname.text(),
                    self.avatar.text(),
                    self.ltxt.text(),
                    self.utxt.text(),
                    self.rtxt.text(),
                    self.dtxt.text())


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
    avatar = ""
    ltxt = ""
    utxt = ""
    rtxt = ""
    dtxt = ""

    def __init__(self, imgpath, description, index,
                 left, up, right, down, special, life,
                 atk, vname, avatar, ltxt, utxt, rtxt, dtxt):
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
        self.avatar = avatar
        self.ltxt = ltxt
        self.utxt = utxt
        self.rtxt = rtxt
        self.dtxt = dtxt
