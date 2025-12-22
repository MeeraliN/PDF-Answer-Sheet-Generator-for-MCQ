# PDF Answer Sheet Generator

A lightweight Python script that generates printable, MCQ answer sheets without options printed for exams and quizzes using the `reportlab` library.

## Features
Generates three distinct PDF layouts in a single run:
* **1 to 200** (Standard full-page sequence)
* **1 to 100** (Two sets per page, side-by-side)
* **1 to 50** (Four sets per page, vertical columns)

All layouts include:
* **Format:** A4 size with optimized margins for maximum writing space.
* **Header:** Fields for "Chapter" and "Date".
* **Footer:** Scoring sections for Correct, Incorrect, and Total Marks.
* **Layout:** Clear vertical separation and horizontal grid lines.

## Requirements

```bash
pip install reportlab
```

## Usage

Run the script to generate all three PDF variations at once:

```bash
python main.py
```

The script will output the following files in your directory:

```bash
OMR_1_to_200.pdf
OMR_1_to_100_x2.pdf
OMR_1_to_50_x4.pdf
```
