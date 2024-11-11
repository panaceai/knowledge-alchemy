import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest

from anthropic_api import AnthropicAPI


class TestAnthropicAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test environment and load API key."""
        # Initialize the API client
        cls.api_client = AnthropicAPI()

    def test_summarize_pdf(self):
        """Test the summarize_pdf method with a sample PDF and prompt."""
        # Read base64-encoded PDF data from a sample file
        pdf_path = '../data/pdf/2024.emnlp-main.1026.pdf'
        prompt_path = '../data/prompts/paper_summarization_v1.txt'

        # Call the summarize_pdf method and check the result
        summary = self.api_client.summarize_pdf(pdf_path, prompt_path)
        self.assertIsNotNone(summary, "Summary should not be None")

        print("Summary:\n", summary.content)


if __name__ == "__main__":
    unittest.main()
