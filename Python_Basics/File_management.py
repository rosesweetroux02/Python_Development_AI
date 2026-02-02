#Opening a file and writing some content to it
file = open("data.txt","w")
file.write("Hello, this is a sample file.\nIt contains multiple lines of text.\nThis is the third line.")
file.close()
#  Opening a file and reading its content
file =open("data.txt","r")
content = file.read()
print(content)
