# OCR Calculator
this is a logic boolean logic calculator which utilizes OCR to calculate logical problems from an image

# motivation

I just wanted to add OCR to one of my old projects

# How to use:

## Step 1: 

I recommend that you setup a virtual environment using anaconda or python venv

```python
conda create -n env_name python=3.8
```

## Step 2:

activate the environment using the following command

```python
conda activate env_name
```

## Step 3:

you should clone the repository if you haven't already using the following command or just by installing the project directly

```python
git clone https://github.com/UndeadZed/Calc_OCR
```

## Step 4:

install the requirements from the [requirements.txt file](link here) by typing the following command in the terminal

```python
pip install -r requirements.txt
```

## Step 5:

now we're done with the setup you can now use the calculator by typing this command in the terminal

```python
python gui.py
```

# Some notes about the calculator:

### the OCR is based on easyocr which can cause some problems during installation
to solve most of them I found out that just by uninstalling and reinstalling numpy most of the problems are solved and you can do that by using the following commands:

```python
pip uninstall numpy
```
```python
pip install numpy
```

### Example Runs:

starting the gui:
![example gui run](https://github.com/UndeadZed/Calc_OCR/blob/main/Screenshots/step%20(1).png)
selecing the folder:
![example gui run2](https://github.com/UndeadZed/Calc_OCR/blob/main/Screenshots/step%20(2).png)
selecting the image of the problem:
![example gui run3](https://github.com/UndeadZed/Calc_OCR/blob/main/Screenshots/step%20(3).png)
the output:
![example gui run4](https://github.com/UndeadZed/Calc_OCR/blob/main/Screenshots/step%20(4).png)


### the following image is the sample used in the example above:

![sample image](https://github.com/UndeadZed/Calc_OCR/blob/main/example.jpg)

# Credits:

all of the OCR was thanks to [JaidedAI easyocr library](https://github.com/JaidedAI/EasyOCR)






