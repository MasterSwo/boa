class CreateHTML:
    def __init__(self, filename):
        self.filename = filename
        file = open(self.filename, "w")
        file.write("<html> \n<body> \n</body> \n</html>")
        file.close()

    def addTitle(self, title, idd):
        file = open(self.filename, "r")
        title = "<h1 id='" + idd + "' > " + title + " </h1> <br/> \n"
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].startswith("</body>"):
                lines[i] = title + lines[i]
        file.close()
        file = open(self.filename, "w+")
        for i in lines:
            file.write(i)
        file.close()

    def editTitle(self, title, idd):
        file = open(self.filename, "r")
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].startswith("<h1"):
                temp = lines[i].split(" ")
                if temp[1] == "id='"+idd+"'":
                    lines[i] = "<h1 id='" + idd + "' >" + title + " </h1> <br/> \n"
        file.close()
        file = open(self.filename, "w+")
        for i in lines:
            file.write(i)
        file.close()


    def addParagraph(self, content, idd):
        file = open(self.filename, "r")
        content = "<p id='" + idd + "'>" + content + " </p> <br/> \n"
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].startswith("</body>"):
                lines[i] = content + lines[i]
        file.close()
        file = open(self.filename, "w+")
        for i in lines:
            file.write(i)
        file.close()

    def addStyle(self, idd, style):
        return
        # find the id and apply inline style to the element

    def Idris(self):
        #Checking if im connected.
