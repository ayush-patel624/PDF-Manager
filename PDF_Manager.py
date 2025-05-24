from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder

def merge_pdfs():
    print("\n📎 Merge PDFs")
    writer = PdfWriter()
    count = int(input("How many PDFs would you like to merge? "))

    for i in range(count):
        file_path = input(f"Enter the path for PDF #{i+1}: ")
        reader = PdfReader(file_path)
        for page in reader.pages:
            writer.add_page(page)

    output = input("Name the output file (e.g., merged.pdf): ")
    with open(output, "wb") as f:
        writer.write(f)
    print(f"✅ Successfully merged {count} PDFs into '{output}'.")

def append_pdf():
    print("\n➕ Append a PDF to another")
    base_path = input("Enter the base PDF file path: ")
    extra_path = input("Enter the PDF you want to append: ")
    writer = PdfWriter()

    for path in [base_path, extra_path]:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)

    output = input("Name the combined output file: ")
    with open(output, "wb") as f:
        writer.write(f)
    print(f"✅ Appended and saved as '{output}'.")

def clone_pdf():
    print("\n📄 Clone a PDF")
    source = input("Enter the source PDF file path: ")
    clone_name = input("Name the cloned file: ")
    reader = PdfReader(source)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open(clone_name, "wb") as f:
        writer.write(f)
    print(f"✅ Cloned '{source}' as '{clone_name}'.")

def add_watermark():
    print("\n💧 Add Watermark")
    main_pdf = input("Enter the main PDF file: ")
    watermark_pdf = input("Enter the watermark PDF (should have 1 page): ")
    output = input("Name the output file: ")

    main_reader = PdfReader(main_pdf)
    watermark_page = PdfReader(watermark_pdf).pages[0]
    writer = PdfWriter()

    for page in main_reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output, "wb") as f:
        writer.write(f)
    print(f"✅ Watermark added. Saved as '{output}'.")

def crop_pdf():
    print("\n✂️ Crop PDF Pages")
    input_pdf = input("Enter the PDF to crop: ")
    output_pdf = input("Name the output file: ")

    left = float(input("Left crop (points): "))
    bottom = float(input("Bottom crop (points): "))
    right = float(input("Right crop (points): "))
    top = float(input("Top crop (points): "))

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        page.mediabox.lower_left = (left, bottom)
        page.mediabox.upper_right = (right, top)
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"✅ Cropped and saved as '{output_pdf}'.")

def read_annotations():
    print("\n🔍 Read Annotations from PDF")
    pdf_path = input("Enter the PDF file: ")
    reader = PdfReader(pdf_path)

    for i, page in enumerate(reader.pages, start=1):
        annotations = page.get("/Annots")
        if annotations:
            print(f"\n📄 Page {i} Annotations:")
            for annot in annotations:
                annot_obj = annot.get_object()
                print(f" - Type: {annot_obj.get('/Subtype')}, Text: {annot_obj.get('/Contents')}")
        else:
            print(f"📄 Page {i} has no annotations.")

def write_annotation():
    print("\n📝 Write Text Annotation")
    input_pdf = input("Enter the PDF to annotate: ")
    output_pdf = input("Name the output file: ")
    page_index = int(input("Page number to annotate (starting from 1): ")) - 1

    text = input("Enter the annotation text: ")
    x = int(input("X position: "))
    y = int(input("Y position: "))

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Copy pages first
    for page in reader.pages:
        writer.add_page(page)

    # Create and add annotation
    annotation = AnnotationBuilder.free_text(
        text=text,
        rect=(x, y, x + 150, y + 50),
        font="Helvetica",
        bold=True,
        font_size="12pt"
    )
    writer.add_annotation(page_number=page_index, annotation=annotation)

    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"✅ Annotation added to page {page_index + 1} and saved as '{output_pdf}'.")

def main():
    while True:
        print("\n📘 Welcome to PDF Manager")
        print("1️⃣  Merge PDFs")
        print("2️⃣  Append one PDF to another")
        print("3️⃣  Clone a PDF")
        print("4️⃣  Add a Watermark")
        print("5️⃣  Crop PDF Pages")
        print("6️⃣  Read Annotations")
        print("7️⃣  Write Annotation")
        print("8️⃣  Exit")

        choice = input("Choose an option (1-8): ")

        if choice == '1':
            merge_pdfs()
        elif choice == '2':
            append_pdf()
        elif choice == '3':
            clone_pdf()
        elif choice == '4':
            add_watermark()
        elif choice == '5':
            crop_pdf()
        elif choice == '6':
            read_annotations()
        elif choice == '7':
            write_annotation()
        elif choice == '8':
            print("👋 Exiting PDF Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 8.")

if __name__ == "__main__":
    main()
