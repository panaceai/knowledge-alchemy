# Knowledge Alchemy
![Knowledge Alchemy Logo](assets/knowledge_alchemy_logo.png)

### Installation 🛠️

#### Step 1: Clone the repository
```bash
git clone https://github.com/panaceai/knowledge-alchemy.git
cd knowledge-alchemy
```

#### Step 2: Set up a virtual environment (recommended)
```bash
python3 -m venv alchemy-env
source alchemy-env/bin/activate  # On Windows: alchemy-env\Scripts\activate
```

#### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

## Summarize PDF Tool
The tool takes a directory of PDF files and a prompt stored in a `.txt` file as input and returns a json file containing the summarizes of PDFs.

## Usage 🚀

```bash
python src/summarize_pdfs.py --pdfs-dir path/to/pdfs/dir --prompt-path path/to/txt/prompt/file --output-file path/to/output/json/file
```

### Example
```bash
python src/summarize_pdfs.py --pdfs-dir data/pdfs/ --prompt-path data/prompts/paper_summarization_v1.txt --output-path data/result.json
```

## Testing ✅
The project includes unit tests to validate its functionality. To run the tests, use:

```bash
cd src
pytest ../tests/
```

Make sure to have `pytest` installed by running:
```bash
pip install pytest
```
