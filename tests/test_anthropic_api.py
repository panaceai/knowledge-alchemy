import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import base64
import unittest

from anthropic_api import AnthropicAPI
from dotenv import load_dotenv


class TestAnthropicAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test environment and load API key."""
        # Load environment variables
        load_dotenv()
        cls.api_key = os.getenv("ANTHROPIC_API_KEY")

        # Ensure the API key is set
        if not cls.api_key:
            raise ValueError("API key not found. Make sure .env file is configured correctly.")

        # Initialize the API client
        cls.api_client = AnthropicAPI()

    def test_summarize_pdf(self):
        """Test the summarize_pdf method with a sample PDF and prompt."""
        # Read base64-encoded PDF data from a sample file
        pdf_path = '../data/pdf/2024.emnlp-main.1026.pdf'
        prompt_path = '../data/prompts/paper_summarization_v1.txt'

        try:
            with open(pdf_path, "rb") as pdf_file:
                pdf_data = base64.standard_b64encode(pdf_file.read()).decode("utf-8")
        except FileNotFoundError:
            self.fail(f"PDF file '{pdf_path}' not found.")

        # Read the prompt from a sample text file
        try:
            with open(prompt_path, 'r') as file:
                prompt = file.read()
        except FileNotFoundError:
            raise Exception(f"Error in reading prompt.")

        # Call the summarize_pdf method and check the result
        summary = self.api_client.summarize_pdf(pdf_data, prompt)
        self.assertIsNotNone(summary, "Summary should not be None")
        print("Summary:\n", summary.content)


if __name__ == "__main__":
    unittest.main()
