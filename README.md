# QR Code Generator

A simple and lightweight QR Code Generator built with Python.
It allows you to create QR codes from URLs or any text and save them as PNG images.

## Features

- Generate QR codes from URLs or text
- Save QR codes as PNG files
- Simple command-line interface
- Fast and easy to use
- Beginner-friendly Python project

## Requirements

Before installing, make sure you have:

- Python 3.x installed
- pip package manager

Check Python version:

```bash
python --version
```

Check pip:

```bash
pip --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/e2e3c/QR-Code-Generator.git
```

### 2. Enter the project folder

```bash
cd QR-Code-Generator
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install qrcode[pil]
```

## Usage

Run the program:

```bash
python main.py
```

Enter your URL or text:

```text
Enter URL or Text: https://github.com/e2e3c
```

The QR code will be created:

```text
qrcode.png
```

## Project Structure

```
QR-Code-Generator/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Example

Input:

```
https://github.com/e2e3c
```

Output:

```
qrcode.png
```

## Technologies Used

- Python 3
- qrcode Library
- Pillow

## Author

**Ayman Mohammed**

GitHub:
https://github.com/e2e3c

## License

This project is licensed under the MIT License.
This project is licensed under the MIT License.
