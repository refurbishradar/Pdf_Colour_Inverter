import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Function to invert colors in a PDF file
def invert_colors(pdf_path, output_path):
    try:
        pdf_reader = PyPDF2.PdfFileReader(pdf_path)
        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page.mergePage(page)
            page.compressContentStreams()  # Compress the content for smaller file size
            pdf_writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
        messagebox.showinfo("Success", "PDF colors inverted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to handle the "Open" button click
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        if output_path:
            invert_colors(file_path, output_path)

# Create the GUI window
root = tk.Tk()
root.title("PDF Color Inverter")

# Create and configure the "Open" button
open_button = tk.Button(root, text="Open PDF File", command=open_file)
open_button.pack(pady=20)

# Start the GUI application
root.mainloop()
