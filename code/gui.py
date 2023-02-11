from tkinter import *
from tkinter import filedialog
import PIL
from PIL import Image
from ocr import use_ocr
from calculator_backend import *




# Create the main window
root = Tk()
root.title("Simple logic calculator")

# Create a list to store the file paths of the images
files = []

# Create a function to open the file explorer to select an image
def selectImage():
    # Open the file explorer
    filepath = filedialog.askopenfilename()
    return filepath


# Create a function to run the image through a test1() function
def solve():
    # Get the file path of the image
    filepath = selectImage()
    # Open the image using the file path
    img = PIL.Image.open(filepath)
    # Run the image through the test1() function
    output = use_ocr(img)
    # Display the test1() output in a text area
    out = str(solve_problem(cleaning_input(output)))+"\n"
    outputText.insert(END, out)


# Create a button to run the test1() function
runButton = Button(root, text="Select Problem", command=solve)
# Create a text area to display the test1() output
outputText = Text(root)

# Pack the widgets
runButton.pack()
outputText.pack()

# Run the main window
root.mainloop()