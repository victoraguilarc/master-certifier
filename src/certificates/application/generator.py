from dataclasses import dataclass
from decimal import Decimal
from io import BytesIO
from typing import Dict, Tuple, Optional

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas

from src.certificates.domain.models.certificate import Certificate
from src.certificates.domain.models.metadata import TextMetadata
from src.certificates.domain.models.replacement import Replacement
from src.certificates.domain.repositories.certificate import CertificateRepository
from src.certificates.domain.repositories.replacement import ReplacementRepository
from src.certificates.domain.repositories.template import TemplateRepository
from src.common.domain.interfaces.filebucket import FileBucket


@dataclass
class CertificateGenerator(object):
    certificate_id: str
    template_id: str
    group: str
    context: dict
    template_repository: TemplateRepository
    replacement_repository: ReplacementRepository
    certificate_repository: CertificateRepository
    certificate_bucket: FileBucket

    def execute(self) -> Optional[Certificate]:
        # Get replacements by template
        template = self.template_repository.find_template(self.template_id)
        certificate = self._build_certificate(template_key=template.file_path)
        certificate_url = self.certificate_bucket.upload(
            file_name=f'{self.template_id}/{self.certificate_id}.pdf',
            file_content=certificate.getvalue(),
            content_type='application/pdf',
        )
        instance = Certificate(
            id=self.certificate_id,
            template_id=self.template_id,
            group=self.group,
            file_path=certificate_url,
        )
        self.certificate_repository.persist(instance)
        return instance

    def _build_certificate(self, template_key: str) -> BytesIO:
        output_buffer = BytesIO()
        output_writer = PdfWriter()

        template_bytes = BytesIO(self.certificate_bucket.get_file(template_key))
        template_reader = PdfReader(template_bytes)
        num_pages = len(template_reader.pages)
        template_page = template_reader.pages[0]
        page_size = (template_page.mediabox.width, template_page.mediabox.height)

        replaced_reader = self._get_replaced_document(num_pages, page_size)

        for page_index, _ in enumerate(template_reader.pages):
            input_page = template_reader.pages[page_index]
            input_page.merge_page(page2=replaced_reader.pages[page_index])
            output_writer.add_page(input_page)

        output_writer.write(output_buffer)
        return output_buffer

    def _get_replacements_map(self) -> Dict[str, Replacement]:
        replacements = self.replacement_repository.filter_by_template(self.template_id)
        return {replacement.name: replacement for replacement in replacements}

    def _get_replaced_document(
        self,
        num_pages: int,
        page_size: Tuple[Decimal, Decimal],

    ) -> PdfReader:
        collection = self.replacement_repository.get_collection(self.template_id)
        output_buffer = BytesIO()
        canvas_pdf = Canvas(output_buffer, pagesize=page_size)
        for page_index in range(num_pages):
            replacements = collection.get_page_items(page_index)
            for replacement in replacements:
                if replacement.is_text:
                    self._draw_text(
                        canvas_pdf=canvas_pdf,
                        axis_x=replacement.axis_x,
                        axis_y=replacement.axis_y,
                        text=self.context.get(replacement.name, ''),
                        text_metadata=TextMetadata.from_dict(replacement.metadata),
                    )
            canvas_pdf.showPage()

        canvas_pdf.save()
        return PdfReader(output_buffer)

    @classmethod
    def _draw_text(
        cls,
        canvas_pdf: canvas.Canvas,
        text_metadata: TextMetadata,
        axis_x: float,
        axis_y: float,
        text: str,
    ):
        canvas_pdf.setFont(text_metadata.font_family, text_metadata.font_size)
        if text_metadata.is_text_center:
            canvas_pdf.drawCentredString(float(axis_x), float(axis_y), text)
        elif text_metadata.is_text_left:
            canvas_pdf.drawString(float(axis_x), float(axis_y), text)
        elif text_metadata.is_text_right:
            canvas_pdf.drawRightString(float(axis_x), float(axis_y), text)




