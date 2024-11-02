# plain2srs

## Installation

```bash
git clone git@github.com:vernette/plain2srs.git
cd plain2srs
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Print the help message:

```bash
./plain2srs.py -h
```

Compile a SRS file from a plain text file:

```bash
./plain2srs.py -i domains.txt -o output_filename -c
```
