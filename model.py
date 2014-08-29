__author__ = 'qing'

class Model:
    def read(self, stored_path):
        try:
            with open(stored_path, 'r', encoding='utf-8') as f:
                return f.readlines()
        except:
            return None



    def write(self, lines, path):
        with open(path, 'w+', encoding='utf-8') as f:
            f.writelines(lines)


