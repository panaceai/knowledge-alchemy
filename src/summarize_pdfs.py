import json
import argparse

from anthropic_api import AnthropicAPI
from pathlib import Path


def summarize_pdfs_in_directory(input_dir, prompt_path, output_file):
    """
    Summarizes all PDF files in a given directory and saves the results to a JSON file.

    Parameters:
    - input_dir (str): Path to the directory containing PDF files.
    - prompt_path (str): Path to .txt file containing prompt
    - output_file (str): Path to the output JSON file.
    """
    # Initialize the Anthropic API client
    api_client = AnthropicAPI()

    # Prepare a dictionary to store results
    summaries = {}

    # Process each PDF file in the directory
    for pdf_file in Path(input_dir).glob("*.pdf"):
        summary = api_client.summarize_pdf(str(pdf_file), prompt_path)

        if summary:
            # Store the summary in the dictionary
            result = "\n".join(d.text for d in summary.content)
            summaries[pdf_file.name] = result
        else:
            print(f"Failed to summarize: {pdf_file.name}")

    # Save the summaries to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(summaries, json_file, ensure_ascii=False, indent=4)

    print(f"Summaries saved to {output_file}")


if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Summarize a PDF using Anthropic API")
    parser.add_argument('--pdf-path', type=str, required=True, help="Path to the base64 encoded PDF file")
    parser.add_argument('--prompt-path', type=str, required=True, help="Path to the .txt file containing the prompt")
    parser.add_argument('--output-file', type=str, required=True, help="Path to the .json file to store the output",
                        default="../data/result.json")

    args = parser.parse_args()

    summarize_pdfs_in_directory(args.pdf_path, args.prompt_path, args.output_file)
