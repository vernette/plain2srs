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

Generate JSON file from the antifilter list:

```bash
./plain2srs.py -o output_filename
```

Generate JSON file and compile an SRS file from a plain text file:

> [!NOTE]
> sing-box must be in the path to compile the SRS file

```bash
./plain2srs.py -i domains.txt -o output_filename -c
```
