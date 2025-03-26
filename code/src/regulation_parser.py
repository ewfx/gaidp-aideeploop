from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import PyPDF2


class RegulationParser:
    def __init__(self, model_name="google/flan-t5-large"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def extract_requirements(self, regulatory_document):
        # Convert PDF to text
        text = self._pdf_to_text(regulatory_document)

        # Use LLM to extract data requirements
        prompt = f"""
        Extract all data reporting requirements from this regulatory document.
        For each requirement, identify:
        - The data field needed
        - Expected format
        - Validation rules
        - Frequency of reporting

        Document: {text[:10000]}... [truncated if long]
        """

        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=2000)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def _pdf_to_text(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = "\n".join([page.extract_text() for page in reader.pages])
        return text