from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

mypass = "7698"  # use your own password
mydatabase = "library"  # The database name

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()  # cur -> cursor

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25
# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight))
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(100, 440, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
headingLabel = Label(headingFrame1, text="Chào mừng bạn đến với thư viện", bg="blue", font=("Courier", 14))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Thêm chi tiết Book", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Xóa Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Xem danh sách Book", bg='black', fg='white', command=view)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Phát hành Book", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Trả Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

root.mainloop()
