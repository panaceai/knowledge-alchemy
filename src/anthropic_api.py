import httpx
import base64
import anthropic

from dotenv import load_dotenv
from urllib.parse import urlparse


class AnthropicAPI:
    def __init__(self, model="claude-3-5-sonnet-20241022"):
        """
        Initialize the AnthropicAPI class with the API key and model.

        Parameters:
        - model (str): The model to use for generating responses.
        """
        # Load environment variables from .env file
        load_dotenv()

        self.client = anthropic.Anthropic()
        self.model = model
        self.betas = ["pdfs-2024-09-25", "prompt-caching-2024-07-31"]
        self.max_tokens = 1024

    def summarize_pdf(self, pdf_path, prompt_path):
        """
        Summarizes the content of a PDF using a prompt.

        Parameters:
        - pdf_data (str): The base64 encoded PDF data.
        - prompt (str): The prompt to use for summarizing the content.

        Returns:
        - str: The summarized content from the API response.
        """

        pdf_data = None

        # Check if the provided path is a URL
        if self.is_url(pdf_path):
            pdf_data = base64.standard_b64encode(httpx.get(pdf_path).content).decode("utf-8")
        else:
            # reading a local PDF file
            with open(pdf_path, "rb") as pdf_file:
                pdf_data = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

        if not pdf_data:
            print("Failed to read PDF data.")
            return None

        try:
            with open(prompt_path, 'r') as file:
                prompt = file.read()
        except FileNotFoundError:
            raise Exception(f"Error in reading prompt.")

        try:
            # Prepare the message payload for the API call
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "document",
                            "source": {
                                "type": "base64",
                                "media_type": "application/pdf",
                                "data": pdf_data
                            },
                            "cache_control": {"type": "ephemeral"}
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]

            # Make the API call
            response = self.client.beta.messages.create(
                model=self.model,
                betas=self.betas,
                max_tokens=self.max_tokens,
                messages=messages
            )

            # Return the content from the response
            return response

        except Exception as e:
            print(f"Error during API call: {e}")
            return None

    @staticmethod
    def is_url(path):
        """Check if the given path is a valid URL."""
        try:
            result = urlparse(path)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
