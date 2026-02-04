from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm


def create_answer_sheet(filename, mode):
    """
    Generates a single-page A4 answer sheet with bold black grid lines.

    Modes:
    "200" -> 1–200 continuous
    "100" -> 1–100 repeated twice
    "50"  -> 1–50 repeated four times
    """

    c = canvas.Canvas(filename, pagesize=A4)
    page_width, page_height = A4

    # Fixed layout (edge-to-edge)
    header_height = 12 * mm
    footer_height = 10 * mm
    usable_height = page_height - header_height - footer_height

    # Grid geometry
    rows_per_column = 25
    columns = 8
    total_slots = rows_per_column * columns

    column_width = page_width / columns
    row_height = usable_height / rows_per_column

    # Header
    c.setLineWidth(1.5)
    c.rect(0, page_height - header_height, page_width, header_height)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(5 * mm, page_height - 8 * mm, "Chapter: ______________________")
    c.drawString(page_width - 70 * mm, page_height - 8 * mm, "Date: ____/____/______")

    # Answer grid
    c.setFont("Helvetica-Bold", 9)
    grid_top = page_height - header_height

    for i in range(total_slots):
        col = i // rows_per_column
        row = i % rows_per_column

        x = col * column_width
        y = grid_top - (row + 1) * row_height

        if mode == "200":
            q = i + 1
        elif mode == "100":
            q = (i % 100) + 1
        elif mode == "50":
            q = (i % 50) + 1

        c.drawString(x + 2 * mm, y + row_height / 3, f"{q}.")
        c.setLineWidth(1)
        c.line(x, y, x + column_width, y)

        if row == 0:
            c.setLineWidth(1.2)
            c.line(x + column_width, grid_top,
                   x + column_width, grid_top - usable_height)

    # Footer
    c.setLineWidth(1.5)
    c.rect(0, 0, page_width, footer_height)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(5 * mm, 4 * mm, "Correct: _______")
    c.drawString(50 * mm, 4 * mm, "Incorrect: _______")
    c.drawString(110 * mm, 4 * mm, "Total Marks: _________")

    c.save()
    print(f"Generated: {filename}")


if __name__ == "__main__":
    create_answer_sheet("OMR_1_to_200.pdf", "200")
    create_answer_sheet("OMR_1_to_100_x2.pdf", "100")
    create_answer_sheet("OMR_1_to_50_x4.pdf", "50")
