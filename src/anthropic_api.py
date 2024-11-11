import os
import base64
import argparse
import anthropic

from dotenv import load_dotenv


class AnthropicAPI:
    def __init__(self, model="claude-3-5-sonnet-20241022"):
        """
        Initialize the AnthropicAPI class with the API key and model.

        Parameters:
        - api_key (str): Your Anthropic API key.
        - model (str): The model to use for generating responses.
        """
        # Load environment variables from .env file
        load_dotenv()

        self.client = anthropic.Anthropic()
        self.model = model
        self.betas = ["pdfs-2024-09-25", "prompt-caching-2024-07-31"]
        self.max_tokens = 1024

    def summarize_pdf(self, pdf_data, prompt):
        """
        Summarizes the content of a PDF using a prompt.

        Parameters:
        - pdf_data (str): The base64 encoded PDF data.
        - prompt (str): The prompt to use for summarizing the content.

        Returns:
        - str: The summarized content from the API response.
        """
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


# Example usage
if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Summarize a PDF using Anthropic API")
    parser.add_argument('--pdf-path', type=str, required=True, help="Path to the base64 encoded PDF file")
    parser.add_argument('--prompt-path', type=str, required=True, help="Path to the .txt file containing the prompt")

    args = parser.parse_args()

    # Read the PDF data
    try:
        with open(args.pdf_path, "rb") as pdf_file:
            pdf_data = base64.standard_b64encode(pdf_file.read()).decode("utf-8")
    except FileNotFoundError:
        raise Exception(f"Error: PDF file '{args.pdf}' not found.")

    # Read the prompt from the provided text file
    try:
        with open(args.prompt_path, 'r') as file:
            prompt = file.read()
    except FileNotFoundError:
        raise Exception(f"Error in reading prompt.")

    # Initialize the API client
    api_client = AnthropicAPI()

    # Call the summarize_pdf method
    summary = api_client.summarize_pdf(pdf_data, prompt)
    if summary:
        print("Summary:", summary.content)
    else:
        print("Failed to retrieve summary.")
