
from fpdf import FPDF

def export_projection_to_pdf(data: list, filename: str = "projection_report.pdf") -> str:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Roth IRA Projection Report", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 8)
    headers = list(data[0].keys())
    col_width = pdf.w / len(headers) - 2
    for header in headers:
        pdf.cell(col_width, 6, str(header), border=1)
    pdf.ln()

    pdf.set_font("Arial", '', 7)
    for row in data:
        for value in row.values():
            pdf.cell(col_width, 6, str(round(value, 2) if isinstance(value, float) else value), border=1)
        pdf.ln()

    output_path = f"/tmp/{filename}"
    pdf.output(output_path)
    return output_path
