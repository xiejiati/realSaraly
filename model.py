__author__ = 'qing'

class CommonFileModel:
    def read(self, stored_path):
        try:
            with open(stored_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                i = 0
                size = len(lines)
                while i < size:
                    if lines[i].strip() == '':
                        del lines[i]

                return f.readlines()
        except:
            return None



    def write(self, lines, path):
        with open(path, 'w+', encoding='utf-8') as f:
            f.writelines(lines)







