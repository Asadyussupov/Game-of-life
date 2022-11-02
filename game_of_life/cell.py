class Cell:
    def __init__(self, i, j, color):
        self.alive = False
        self.color = self._from_rgb(color) if type(color) == tuple else color
        self.i = i
        self.j = j

    @classmethod
    def _from_rgb(cls, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'