from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def create_answer_sheet(filename, mode):
    """
    mode options:
    "200" -> Numbers 1 to 200
    "100" -> Numbers 1 to 100 (twice)
    "50"  -> Numbers 1 to 50 (four times)
    """
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # --- Configuration ---
    margin_left = 10 * mm
    margin_right = 10 * mm
    margin_top = 10 * mm    
    margin_bottom = 11 * mm 
    header_height = 10 * mm
    footer_height = 8 * mm
    
    # Calculate usable height for questions
    usable_height = height - margin_top - margin_bottom - header_height - 2*mm
    
    cols = 4
    rows_per_col = 50
    total_slots = cols * rows_per_col # 200 slots
    
    col_width = (width - margin_left - margin_right) / cols
    row_height = usable_height / rows_per_col
    
    # --- Draw Header ---
    c.setLineWidth(1)
    header_y = height - margin_top
    
    # Header Box
    c.rect(margin_left, header_y - header_height, width - 20*mm, header_height)
    
    c.setFont("Helvetica-Bold", 10)
    text_y = header_y - header_height + 3*mm
    c.drawString(margin_left + 5*mm, text_y, "Chapter: ______________________")
    c.drawString(margin_left + 120*mm, text_y, "Date: ____/____/______")
    
    # --- Draw Grid & Numbers ---
    c.setFont("Helvetica-Bold", 10)
    
    start_y = header_y - header_height
    
    for i in range(total_slots):
        current_col = i // rows_per_col
        current_row = i % rows_per_col
        
        x = margin_left + (current_col * col_width)
        y = start_y - (current_row * row_height) - row_height
        
        # --- Numbering Logic ---
        q_num = 0
        if mode == "200":
            q_num = i + 1
        elif mode == "100":
            q_num = (i % 100) + 1
        elif mode == "50":
            q_num = (i % 50) + 1
            
        # Draw Number
        c.drawString(x + 2*mm, y + 2*mm, f"{q_num}.")
        
        # Draw Horizontal Line
        c.setLineWidth(0.5)
        c.setStrokeColorRGB(0.7, 0.7, 0.7) # Light Grey
        c.line(x, y, x + col_width - 2*mm, y)
        
        # Draw Vertical Lines (only top of column)
        if current_row == 0 and current_col < cols:
            # Determine Line Style
            c.setStrokeColorRGB(0, 0, 0) # Black
            
            # Special case for "100" mode: thicker line in the middle
            if mode == "100" and current_col == 2:
                c.setLineWidth(1.5)
            else:
                c.setLineWidth(0.5)
                
            # Draw Vertical Line
            c.line(x + col_width, start_y, x + col_width, start_y - usable_height)

    # --- Draw Footer ---
    c.setLineWidth(1)
    c.setStrokeColorRGB(0, 0, 0) # Black
    
    footer_y = margin_bottom - footer_height
    c.rect(margin_left, footer_y, width - 20*mm, footer_height)
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_left + 5*mm, footer_y + 3*mm, "Correct: _______")
    c.drawString(margin_left + 50*mm, footer_y + 3*mm, "Incorrect: _______")
    c.drawString(margin_left + 100*mm, footer_y + 3*mm, "Total Marks: _________")

    c.save()
    print(f"Generated: {filename}")

# --- Main Execution ---
if __name__ == "__main__":
    # 1. Generate 1 to 200
    create_answer_sheet("OMR_1_to_200.pdf", mode="200")
    
    # 2. Generate 1 to 100 (Two sets)
    create_answer_sheet("OMR_1_to_100_x2.pdf", mode="100")
    
    # 3. Generate 1 to 50 (Four sets)
    create_answer_sheet("OMR_1_to_50_x4.pdf", mode="50")
