from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(text, filepath):
    styles = getSampleStyleSheet()
    story = [Paragraph(t.replace("\n", "<br/>"), styles["Normal"]) for t in text.split("\n\n")]
    pdf = SimpleDocTemplate(filepath)
    pdf.build(story)
    return filepath
