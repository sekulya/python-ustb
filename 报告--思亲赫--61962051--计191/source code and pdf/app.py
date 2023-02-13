import tkinter as tk
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger, pdf
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, askopenfilename
import tkinter.filedialog as fd
import fitz
import io 


# root is tkinter gui framework writes first and foremost 
# set background without geometry 
root = tk.Tk()

# set background using tkinter 
background = tk.Canvas(root, width=800, height=700, bg="light blue")
background.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg="light blue")
logo_label.image = logo
logo_label.grid(column=0, row=0,)

#instruction
instructions = tk.Label(root, text="Select", font="Arial", bg="light blue")
instructions.grid(columnspan=1, column=0, row=0)


# function extract image from pdf in this folder
def image():
    # use filedialog method to open files
    file = fd.askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    file = fitz.open(file)
        # iterate over PDF pages
    for page_index in range(len(file)):
    # get the page itself
        page = file[page_index]
        image_list = page.getImageList()
    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.getImageList(), start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = file.extractImage(xref)
        image_bytes = base_image["image"]
       
        image_ext = base_image["ext"]
       # open image bytes in image extract
        image_ext = Image.open(io.BytesIO(image_bytes))


    # save output file as png
    image_ext.save(open(f"image{page_index+1}_{image_index}.png", "wb"))
    
    # close outpufile
    image_ext.close()
    image_ext.set("extract image")
    
# text variable as stringvar
image_ext = tk.StringVar()
# create image extract button
image_btn = tk.Button(root, textvar=image_ext, command=lambda:image(), font="Arial", bg="#865ff8", fg="light blue", height=3, width=17)
# set the button
image_ext.set("extract image")
# button's whereabouts
image_btn.grid(column=1,row=0)



# text box for extracted text
text_box = tk.Text(root, height=10, width=48, padx=15, pady=15)
# place the text box in the center of interface
text_box.tag_configure("center", justify="center")
text_box.tag_add("center", 1.0, "end")
# text box's location
text_box.grid(column=1, row=2)

# extract text from pdf files
def extract_file():
    # while loading
    extract_text.set("loading...")
    # open file
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        # at first has to read files
        read_pdf = PdfFileReader(file)
        # page getpage
        page = read_pdf.getPage(0)
        # extract text from pages 
        page_content = page.extractText()
         

    text_box.insert(1.0, page_content)
 

    # set button extract text
    extract_text.set("extract text")
# module tk stringvar
extract_text = tk.StringVar()
# create extract text button
extract_btn = tk.Button(root, textvar=extract_text, command=lambda:extract_file(), font="Arial", bg="#865ff8", fg="light blue", height=3, width=16)
extract_text.set("extract text")
# button's location
extract_btn.grid(column=1, row=1)
 

# rotate pages within pdf file
# in example rotate page in 90 degrees
def rotate_pages():
    rotate_page.set("Loading...")
    # open file
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(file)
    # version of code that had bugs
    '''
    # Rotate page 90 degrees to the right
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    # Rotate page 90 degrees to the left
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    # Add a page in normal orientation
    pdf_writer.addPage(pdf_reader.getPage(2))
    rotate_page.set("rotate pages")    '''
    
    # iritate  pagenum in variable pdf reader numPages
    for pagenum in range(pdf_reader.numPages):
        # select page to rotate with variable getPage
        page = pdf_reader.getPage(pagenum)
        # rotate the page 
        page.rotateClockwise(90)
        # create rotated page
        pdf_writer.addPage(page)
    # output file
    pdf_out = open('rotated.pdf', 'wb')
    pdf_writer.write(pdf_out)
    # close output file
    pdf_out.close()
    rotate_page.set("rotate pages")
# tk module string rotate page variable 
rotate_page=tk.StringVar()
# make rotate pages button       
rotate_btn=tk.Button(root, textvar=rotate_page, command=lambda:rotate_pages(), font="Arial", bg="#865ff8", fg="light blue", height=3, width=16)
rotate_page.set("rotate pages")  
# button's location
rotate_btn.grid(column=2,row=1)



# a function merge pdf files in one big pdf file
def merge_pdf():
    # open file
    files = fd.askopenfilenames(parent=root, title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    # split files
    files = root.tk.splitlist(files)
    merge_text.set('Loading...')
    # code that was bad
    '''pdf_writer=PdfFileWriter
    pdf_reader = PdfFileReader(files)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    pdf_out = open('merged.pdf','wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()'''
   
   #merge pdf files 
    merge = PdfFileMerger()
    for pdf in files:
        merge.append(pdf)
    merge.write('result.pdf')
    merge.close()
    merge_text.set("merge")
# merge tk tkinter stringvar
merge_text = tk.StringVar()
#merge button desigm
merge_btn = tk.Button(root, textvar=merge_text, command=lambda:merge_pdf(), font="Arial", bg="#865ff8", fg="light blue", height=3, width=16)
merge_text.set("merge")
# merge button location
merge_btn.grid(column=2, row=0)


# a function to protect the file from other 
# only you wil knnow the password and have access to it

def encrypt_pdf():
    # open file
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])

    # input pdf file read by pypdf2 module
    inpupdf = PdfFileReader(file)

    pages_no = inpupdf.numPages
    for i in range(pages_no):
     
     inputpdf = PdfFileReader(file)
     # pdffilewriter part of pypdf2 module 
     encrypt_file = PdfFileWriter()
     # encrypting pdf file
     # add page to inputfile 
     encrypt_file.addPage(inputpdf.getPage(i))
     encrypt_file.encrypt("password")
     # open outputfile
     with open("protected.pdf", "wb") as outputenc:
      encrypt_file.write(outputenc)

    # close output file
    file.close("protected.pdf")
    encrypt_file.set("encrypt")
# encrypt file tk 
encrypt_file = tk.StringVar()
# make encrypt button
encrypt_btn = tk.Button(root, textvar=encrypt_file, command=lambda:encrypt_pdf(), font="Arial", bg="#865ff8", fg="light blue", height=3, width=16)
encrypt_file.set("encrypt")   
# encrypt button whereabouts 
encrypt_btn.grid(column=0, row=2)


#a function to split pdf file in its pages. 
#In example if pdf consists of 2 pages then it splits the file in 2 pages

def split_pdf():
    # open file 
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    #pypdf2 module
    inputpdf = PdfFileReader(file)

    # code that failed
    '''     for pdf in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(pdf))
        output_filename = '{}_page_{}.pdf'.format(file+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))
    if __name__ == '__main__':
        split_text(file)'''
    
    # solit text in pdf file
    for i in range(inputpdf.numPages):
        split_text = PdfFileWriter()
        split_text.addPage(inputpdf.getPage(i))
        # split page by page 
        with open("doc-page%s.pdf"%(i+1), "wb") as outputStream:
            split_text.write(outputStream)
    # close splitted file
    file.close()

# split  text tkinter      
split_text = tk.StringVar()
# split button 
split_btn = tk.Button(root, textvar=split_text, command=lambda:split_pdf(), font="Arial", bg="#865ff8", fg="light blue", height=3, width=16)
# set split button
split_text.set("split")
# split button location
split_btn.grid(column=0, row=1)


def add_watermark():
    # failed attempt to water mark 
    '''file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    pdf_file = file()
    watermark = "watermark.pdf"
    merged_file = "addedwatermark.pdf"
    inputpdf = open(pdf_file,'rb')
    input_pdf = PdfFileReader(inputpdf,'rb')
    watermark_file = open(watermark)
    watermark_pdf = PdfFileReader(watermark_file,'rb')
    pdf_pg = input_pdf.getPage(0)
    watermark_page = watermark_pdf.getPage(0)
    pdf_pg.mergePage(watermark_page)
    wmoutput = PdfFileWriter()
    wmoutput.addPage(pdf_pg)
    merged_file = open(merged_file,'wb')
    wmoutput.write(merged_file)
    merged_file.close()
    watermark_file.close()
    file.close()'''
    # watermark file
    wmfile = open("watermark.pdf", 'rb')
    pdfwmreader = PdfFileReader(wmfile)
    # read file with pdffilereader and write in new variable eith pdffilewriter
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    pdfreader=PdfFileReader(file)
    pdfwriter = PdfFileWriter()
    
    for pageNum in range(pdfreader.numPages):
        pageObj = pdfreader.getPage(pageNum)
        pageObj.mergePage(pdfwmreader.getPage(0))
        pdfwriter.addPage(pageObj)

        wmoutput = open("watermarked.pdf", 'wb')
        pdfwriter.write(wmoutput)

        wmfile.close()
        file.close()
        wmoutput.close()

    wmoutput.set("add watermark")
wmoutput=tk.StringVar()

wmoutput_btn=tk.Button(root,textvar=wmoutput,command=lambda:add_watermark(), font="Arial", bg="#865ff8", fg="light blue", height=3, width=16)

wmoutput.set("add watermark")

wmoutput_btn.grid(column=2,row=2)



root.mainloop()

