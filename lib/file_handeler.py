import os

class File():
    def __init__(self):
        pass

    def find_file(self, file_name, search_path):
        final_path = ''
        for root, dirs, files in os.walk(search_path):
            if file_name in files:
                final_path = os.path.join(root, file_name)

        return str(final_path)