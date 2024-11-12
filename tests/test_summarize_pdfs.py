import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest

from summarize_pdfs import summarize_pdfs_in_directory


class TestAnthropicAPI(unittest.TestCase):
    def test_summarize_pdf(self):
        """Test the summarize_pdf method with a sample PDF and prompt."""
        pdf_dir = '../data/pdfs'
        prompt_path = '../data/prompts/paper_summarization_v1.txt'
        output_file = '../data/emnlp2024_medical_qa.json'

        summarize_pdfs_in_directory(pdf_dir, prompt_path, output_file)


if __name__ == "__main__":
    unittest.main()
