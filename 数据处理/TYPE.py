class FileType:
    def __init__(self, filetype):
        self.type = filetype
        self.count = 0
        self.money = 0


class ReplaceData:
    def __init__(self, replacedata):
        self.replace_name = replacedata[1]
        self.replace_name_before = replacedata[0]
