# Assessment Document Builder

Combines 12 markdown files (00-11) into a password-protected HTML document with search and optional PDF export.

## Setup

```bash
pip install -r ../../../requirements.txt
```

## Usage

```bash
# HTML only
python build_assessment.py --password "your-password" --no-pdf

# HTML + PDF
python build_assessment.py --password "your-password"

# Using config file
cp config.json.example config.json
# Edit config.json, then:
python build_assessment.py --config config.json
```

## Output

- `assessment.html` - Self-contained, password-protected HTML
- `assessment.pdf` - Static PDF (requires weasyprint)

Share HTML directly or host on any static hosting. Password protection is client-side only.

