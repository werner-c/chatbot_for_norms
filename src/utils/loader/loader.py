import logging
import os
from typing import Generator, List, Tuple

from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTFigure, LTImage, LTTextBoxHorizontal, LTTextLineHorizontal
from tqdm import tqdm

from .cleaner import TextCleaner
from ..wrapper import Document

# Konfiguration des Loggings
#logging.basicConfig(
#    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#)
#logger = logging.getLogger("PDFExtractor")


class PDFExtractor:
    def __init__(self, directory_path: str):
        """
        Initialisiert die PDFExtractor-Klasse mit einem Verzeichnispfad.

        :param directory_path: Pfad zu einem Verzeichnis, das PDF-Dokumente enthält.
        """
        self.directory_path = directory_path
        self.pdf_paths = self._get_pdf_paths()
        #logger.info(f"PDFExtractor initialized with directory: {directory_path}")

    def _get_pdf_paths(self) -> List[str]:
        """
        Konvertiert den Verzeichnispfad in eine Liste von vollständigen Pfaden der PDF-Dokumente.

        :return: Liste der vollständigen Pfade der PDF-Dokumente.
        """
        pdf_paths = [
            os.path.join(self.directory_path, file)
            for file in os.listdir(self.directory_path)
            if file.endswith(".pdf")
        ]
        #logger.debug(f"Found PDF files: {pdf_paths}")
        return pdf_paths

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extrahiert den gesamten Text aus einem PDF-Dokument.

        :param pdf_path: Pfad zu einem PDF-Dokument.
        :return: Der gesamte extrahierte Text.
        """
        #logger.info(f"Extracting text from: {pdf_path}")
        
        text = extract_text(pdf_path)

        text = TextCleaner.clean_text(txt=text)
        #logger.debug(
        #    f"Extracted text from {pdf_path}: {text[:100]}..."
        #)  # Log only the first 100 characters
        return text

    def extract_tables_from_pdf(self, pdf_path: str) -> List[str]:
        """
        Extrahiert alle Tabellen aus einem PDF-Dokument.

        :param pdf_path: Pfad zu einem PDF-Dokument.
        :return: Liste der extrahierten Tabellen als Text.
        """
        #logger.info(f"Extracting tables from: {pdf_path}")
        tables = []
        for page_layout in tqdm(
            extract_pages(pdf_path), desc="Extracting tables", unit="page"
        ):
            for element in page_layout:
                if isinstance(element, LTTextBoxHorizontal):
                    for text_line in element:
                        if isinstance(text_line, LTTextLineHorizontal):
                            if self._is_table(text_line.get_text()):
                                tables.append(text_line.get_text())
        #logger.debug(f"Extracted tables from {pdf_path}: {tables}")
        return tables

    def extract_images_from_pdf(self, pdf_path: str) -> List[LTImage]:
        """
        Extrahiert alle Bilder aus einem PDF-Dokument.

        :param pdf_path: Pfad zu einem PDF-Dokument.
        :return: Liste der extrahierten Bilder.
        """
        #logger.info(f"Extracting images from: {pdf_path}")
        images = []
        for page_layout in tqdm(
            extract_pages(pdf_path), desc="Extracting images", unit="page"
        ):
            for element in page_layout:
                if isinstance(element, LTFigure):
                    for image in element:
                        if isinstance(image, LTImage):
                            images.append(image)
        #logger.debug(f"Extracted images from {pdf_path}: {len(images)} images found")
        return images

    def _is_table(self, text: str) -> bool:
        """
        Überprüft, ob ein Text eine Tabelle darstellt.

        :param text: Zu überprüfender Text.
        :return: True, wenn der Text eine Tabelle darstellt, sonst False.
        """
        # Einfache Heuristik zur Erkennung von Tabellen (kann angepasst werden)
        is_table = "\t" in text or "|" in text
        #logger.debug(
        #    f"Text is table: {is_table} - {text[:100]}..."
        #)  # Log only the first 100 characters
        return is_table

    def process_documents(self, options=[]):
        """
        Gibt einen Generator zurück, der jeweils den gesamten extrahierten Text, die Tabellen und die Bilder eines Dokuments liefert.

        :return: Generator, der den gesamten extrahierten Text, die Tabellen und die Bilder eines Dokuments liefert.
        """
        for pdf_path in tqdm(self.pdf_paths, desc="Processing PDFs", unit="file"):
            #logger.info(f"Processing document: {pdf_path}")
            tables, images = None, None
            text = self.extract_text_from_pdf(pdf_path)
            text = TextCleaner.clean_text(text)
            if "tables" in options:
                tables = self.extract_tables_from_pdf(pdf_path)
            if "images" in options:
                images = self.extract_images_from_pdf(pdf_path)
            yield Document(pdf_path, text), tables, images
            #logger.info(f"Finished processing document: {pdf_path}")
