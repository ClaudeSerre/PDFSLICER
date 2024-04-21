import fitz  # Importer PyMuPDF


def split_pdf_into_a4_pages_with_uniform_margins(input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)
    page = doc[0]  # Charger la première page, supposant une seule grande page
    rect = page.rect

    # Dimensions A4 en points PDF
    a4_width, a4_height = 595, 842
    margin = 5  # Marge uniforme pour les côtés, le haut et le bas

    # Calculer le nombre de pages nécessaires, ajusté pour les marges
    total_content_height = rect.height - (2 * margin)  # Hauteur totale du contenu ajustée pour les marges
    content_per_page = a4_height - (2 * margin)  # Contenu par page ajusté pour les marges
    num_splits = int(total_content_height / content_per_page) + (1 if total_content_height % content_per_page else 0)

    new_doc = fitz.open()

    for split_num in range(num_splits):
        # Calculer le décalage Y pour chaque segment, sans ajuster pour la marge supérieure
        y_offset = content_per_page * split_num

        # Ajouter une nouvelle page A4 dans le nouveau document
        new_page = new_doc.new_page(-1, width=a4_width, height=a4_height)

        # Calculer le rectangle de clipping pour le contenu à copier
        clip_rect = fitz.Rect(0, y_offset + margin, rect.width, y_offset + content_per_page + margin)

        # Copier le contenu de la page source vers la nouvelle page en utilisant le rectangle de clipping
        new_page.show_pdf_page(new_page.rect, doc, 0, clip=clip_rect)

    # Enregistrer le nouveau document PDF
    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()

# Chemin du PDF source et chemin du PDF de sortie
input_pdf_path = "/Users/claude-emmanuelserre/Downloads/Rapport Plateforme ORLY.pdf"
output_pdf_path = "/Users/claude-emmanuelserre/Downloads/PDFCUT8test1.pdf"

# Exécuter la fonction pour découper le PDF en pages A4 avec des marges uniformes
split_pdf_into_a4_pages_with_uniform_margins(input_pdf_path, output_pdf_path)


