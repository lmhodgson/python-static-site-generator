import pathlib


class Site():
    def __init__(self, source, dest):
        self.source = pathlib.Path(source)
        self.dest = pathlib.Path(dest)

    def create_dir(self, path):
        directory = self.dest + "/" + pathlib.relative_to(self.source)
