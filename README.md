# MediaMonks challenge

## Challenge description
The requirements of the challenge are found in the document [challenge_description.md](./documentation/challenge_description.md).

## Installation

```bash
Uncompres the files or:

git clone https://github.com/VulturARG/MediaMonks-challenge.git
cd MediaMonks-challenge
git checkout add_filters

# Virtualenv instalación (Linux)
virtualenv venv
source venv/bin/activate

# Virtualenv instalación (Windows)
virtualenv venv
.\venv\Scripts\activate

pip3 install -r requirements.txt
```
## Running the application

```bash
python filters.py -h
python filters.py --help

python filters.py input.jpg --grayscale output.jpg
python filters.py input.jpg --rotate -10 output.jpg
python filters.py input.jpg --overlay file.png output.jpg
python filters.py input.jpg --sepia output.jpg

python filters.py input.jpg --grayscale --rotate -10 --overlay file.png --rotate 50 output.jpg
```

## Running the tests

```bash
python -m unittest
```

## Check test coverage

### Run test suite with coverage:

```bash
coverage run -m unittest
```

### Report on the results:

```bash
coverage report
```

### HTML Report:

```bash
coverage html
```
See the report in: `htmlcov/index.html`

## Add a new filter

To add a new filter, add a file in the filters folder, e.g: `new_filter.py`. 
In this file create a new class that inherits from Filter(ABC) (e.g: `NewFilter(Filter)`)
The new filter will be automatically added to the rest of the filters and the help message will show the new filter.

```python
from PIL import Image

from domain.filters import Filter


class NewFilter(Filter):
    """Add a New Filter."""

    ARGUMENTS = 1  # Number of arguments for the filter
    HELP = "Help"  # Help message for the filter

    def transform(self, image: Image, *args, **kwargs) -> Image:
        """Apply filter."""

        # Filter code here
        return image

    @classmethod
    def build_filter(cls) -> Filter:
        """Build the filter."""

        return cls()
```
