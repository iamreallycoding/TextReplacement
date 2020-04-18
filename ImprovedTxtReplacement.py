class TextFile:
    def __init__(self, path):
        self.path = path
        self.__update()

    def __update(self):
        f = open(self.path, "r")
        document = f.read()
        self.__lines = document.split("\n")
        self.__words = document.split(" ")
        f.close()

    def index_replace_line(self, index, replacement):
        self.__lines[index] = replacement

    def __write_document_line(self, list_to_file):
        f = open(self.path, "r+")
        for item in list_to_file:
            f.write(f"{item}\n")
        f.close()
        self.__update()

    def replace_line_whole(self, line, replacement):
        index = [i for i, x in enumerate(self.__lines) if x == line]
        for i in index:
            self.__lines[i] = replacement
        self.__write_document_line(self.__lines)

    def replace_line_partial(self, partial_line, replacement):
        index = [i for i, x in enumerate(self.__lines) if partial_line in x]
        for i in index:
            self.__lines[i] = replacement
        self.__write_document_line(self.__lines)

    def add_line_before(self, line, addition):
        index = [i for i, x in enumerate(self.__lines) if x == line]
        for i in index:
            self.__lines.insert(i, addition)
        self.__write_document_line(self.__lines)

    def add_line_after(self, line, addition):
        index = [i for i, x in enumerate(self.__lines) if x == line]
        for i in index:
            self.__lines.insert((i + 1), addition)
        self.__write_document_line(self.__lines)

    def __write_document_word(self, list_to_file):
        f = open(self.path, "r+")
        for item in list_to_file:
            f.write(f"{item} ")
        f.close()
        self.__update()

    def index_replace_word(self, index, replacement):
        self.__words[index] = replacement

    def replace_word(self, word, replacement):
        index = [i for i, x in enumerate(self.__words) if word in x]
        for i in index:
            self.__words[i] = self.__words[i].replace(word, replacement)
        self.__write_document_word(self.__words)

    def add_word_before(self, word, addition):
        index = [i for i, x in enumerate(self.__words) if word in x]
        for i in index:
            self.__words[i] = self.__words[i].replace(word, f"{addition} {word}")
        self.__write_document_word(self.__words)

    def add_word_after(self, word, addition):
        index = [i for i, x in enumerate(self.__words) if word in x]
        for i in index:
            self.__words[i] = self.__words[i].replace(word, f"{word} {addition}")
        self.__write_document_word(self.__words)
