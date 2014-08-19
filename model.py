__author__ = 'qing'

class Model:
    def read(self, stored_path):
        with open(stored_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines


    def write(self):
        pass

