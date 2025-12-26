from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Files to include snippets from
FILES = [
    'README.md',
    'conftest.py',
    'base/basepage.py',
    'pages/practice_page.py',
    'steps/practice_page_steps.py',
    'tests/test_conceptDemo.py',
]


def read_file_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f'Could not read {path}: {e}'


def add_heading(doc, text, level=1):
    h = doc.add_heading(level=level)
    run = h.add_run(text)
    run.bold = True


def main():
    doc = Document()
    doc.core_properties.title = 'Automation Framework Architecture & Flow'

    # Title
    title = doc.add_heading(level=0)
    r = title.add_run('Automation Framework: Architecture & Code Flow')
    r.bold = True
    r.font.size = Pt(18)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Overview
    doc.add_heading('Overview', level=1)
    doc.add_paragraph('This document summarizes the current architecture and code flow of the automation framework present in this repository. It is intended to help new contributors understand responsibilities, interactions, and test execution flow.')

    # Project structure
    doc.add_heading('Project Structure', level=1)
    structure = doc.add_paragraph()
    structure.add_run('Key folders and files:').bold = True
    items = [
        ('base/', 'Contains BasePage with low-level Selenium helpers (click, type, wait, etc.)'),
        ('pages/', 'Page objects; represent pages and page-specific behaviors'),
        ('steps/', 'Higher-level flows or step helpers (composition with pages)'),
        ('tests/', 'Pytest tests expressing intent using fixtures and pages'),
        ('conftest.py', 'Driver and page fixtures (setup / teardown)'),
        ('requirements.txt', 'External Python dependencies (selenium, pytest, webdriver-manager)'),
    ]
    for name, desc in items:
        paragraph = doc.add_paragraph(style='List Bullet')
        paragraph.add_run(f'{name}').bold = True
        paragraph.add_run(f' — {desc}')

    # Responsibilities
    doc.add_heading('Responsibility by Layer', level=1)
    doc.add_paragraph('Tests ➜ Pages ➜ BasePage ➜ WebDriver')
    responsibilities = [
        ('Tests', 'Express business intent and assertions; use fixtures to get page instances'),
        ('Pages', 'Encapsulate locators and page-specific actions; may delegate to Steps helpers (composition)'),
        ('Steps', 'Hold higher-level flows and use a page instance (composition) to orchestrate multiple page actions'),
        ('BasePage', 'Provide low-level interactions and common waits for reliable operations'),
        ('conftest', 'Fixtures for driver lifecycle and page instantiation'),
    ]
    for name, desc in responsibilities:
        p = doc.add_paragraph()
        p.add_run(name + ': ').bold = True
        p.add_run(desc)

    # Sequence / Execution Flow
    doc.add_heading('Execution Flow (Typical Test)', level=1)
    steps = [
        'Pytest collects tests and fixtures',
        '`driver` fixture starts a browser and navigates to base URL',
        '`practice_page` fixture constructs a `PracticePage(driver)` instance',
        'Test calls page methods (e.g., `practice_page.click_show_button()`)',
        'Page methods use BasePage helpers (e.g., `clickit`, `typeit`) to interact with WebDriver',
        'For complex flows, Page delegates to `PracticePageSteps` (composition) which uses the page instance',
        'Alerts / dialogs and other browser interactions are handled via BasePage helpers (e.g., `switch_to_alert`)',
        'Assertions verify expected behavior, and fixtures teardown closes the browser',
    ]
    for s in steps:
        doc.add_paragraph(s, style='List Number')

    # Current implementation notes
    doc.add_heading('Current Implementation Notes', level=1)
    doc.add_paragraph('Recent changes: `PracticePage` now instantiates `PracticePageSteps(self)` and delegates higher-level flows to it. This uses composition rather than inheritance for steps/flows.')

    # Architecture diagram (generated PNG)
    doc.add_heading('Architecture Diagram', level=1)
    # ensure diagram exists (generated below) and insert it
    diagram_path = os.path.join(ROOT, 'Architecture_diagram.png')
    if not os.path.exists(diagram_path):
        create_architecture_diagram(diagram_path)
    # insert diagram sized to fit
    try:
        from docx.shared import Inches
        doc.add_picture(diagram_path, width=Inches(6))
    except Exception as e:
        doc.add_paragraph(f'Could not insert diagram: {e}')

    # How to run tests
    doc.add_heading('How to Run Tests', level=1)
    doc.add_paragraph('1. Create a virtual environment (recommended)')
    doc.add_paragraph('2. Install dependencies: `pip install -r requirements.txt`')
    doc.add_paragraph('3. Run tests: `python -m pytest -q`')

    # Tips & Next steps
    doc.add_heading('Tips & Next Steps', level=1)
    tips = [
        'Consider adding a README for each folder describing its intent',
        'Add automatic doc generation or a diagram export for visualization',
        'Add unit tests for Steps classes by injecting fake page objects to validate orchestration logic',
        'Consider adding a simple architecture diagram (PNG) into the docs folder',
    ]
    for t in tips:
        doc.add_paragraph(t, style='List Bullet')

    # Save
    out_path = os.path.join(ROOT, 'Architecture.docx')
    doc.save(out_path)
    print(f'Architecture document written to: {out_path}')


# --- Diagram generation using Pillow ---
from PIL import Image, ImageDraw, ImageFont

def create_architecture_diagram(out_path):
    """Create a simple OO-style architecture diagram and save as PNG."""
    W, H = 1200, 600
    img = Image.new('RGB', (W, H), color='white')
    d = ImageDraw.Draw(img)
    # fonts
    try:
        font_bold = ImageFont.truetype('arialbd.ttf', 18)
        font = ImageFont.truetype('arial.ttf', 14)
    except Exception:
        font_bold = ImageFont.load_default()
        font = ImageFont.load_default()

    # box positions
    boxes = {
        'Tests': (480, 20, 720, 80),
        'Pages': (80, 140, 360, 220),
        'Steps': (440, 140, 760, 220),
        'BasePage': (80, 300, 360, 380),
        'WebDriver': (480, 300, 760, 380),
    }

    # draw boxes
    for label, (x1, y1, x2, y2) in boxes.items():
        d.rectangle([x1, y1, x2, y2], outline='black', width=2, fill='#f3f4f6')
        bbox = d.textbbox((0, 0), label, font=font_bold)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        d.text((x1 + (x2 - x1 - w) / 2, y1 + (y2 - y1 - h) / 2), label, fill='black', font=font_bold)

    # arrows (Tests -> Pages, Tests -> Steps)
    def arrow(a, b):
        ax = (a[0] + a[2]) / 2
        ay = a[3]
        bx = (b[0] + b[2]) / 2
        by = b[1]
        d.line((ax, ay, bx, by), fill='black', width=2)
        # arrowhead
        d.polygon([(bx-6, by-10), (bx+6, by-10), (bx, by)], fill='black')

    arrow(boxes['Tests'], boxes['Pages'])
    arrow(boxes['Tests'], boxes['Steps'])
    arrow(boxes['Pages'], boxes['BasePage'])
    arrow(boxes['Steps'], boxes['BasePage'])
    arrow(boxes['BasePage'], boxes['WebDriver'])

    # labels for responsibilities
    d.text((420, 90), 'Test execution → orchestrates pages and asserts behavior', fill='black', font=font)
    d.text((420, 110), 'Pages delegate to Steps for complex flows; BasePage holds low-level interactions', fill='black', font=font)

    img.save(out_path)



if __name__ == '__main__':
    main()
