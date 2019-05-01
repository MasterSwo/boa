from CreateHTML import CreateHTML

# main function
if __name__ == "__main__":
    f = CreateHTML("index.html")
    f.addTitle("Hello world", "title-1")
    f.editTitle("new title", "title-1")
