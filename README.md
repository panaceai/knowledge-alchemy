# Knowledge Alchemy
<img src="assets/knowledge_alchemy_logo.png" alt="Knowledge Alchemy Logo" width="300"/>

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

#### Step 4: Set up API Keys 🔑
1. Create a `.env` file in the root directory of the project.
2. Add the following line to the `.env` file:
    ```
    ANTHROPIC_API_KEY=your_api_key_here
    ```

## PDF Summarization Tool
The tool takes PDF files and a prompt stored in a `.txt` file as input and returns a json file containing the summarizes of PDFs.

### Usage 🚀

```bash
python src/summarize_pdfs.py --pdfs-dir path/to/pdfs/dir --prompt-path path/to/txt/prompt/file --output-file path/to/output/json/file
```

#### Example
```bash
python src/summarize_pdfs.py --pdfs-dir data/pdfs/ --prompt-path data/prompts/paper_summarization_v1.txt --output-path data/result.json
```

### Testing ✅
```bash
cd src
pytest ../tests/
```

Make sure to have `pytest` installed by running:
```bash
pip install pytest
```
