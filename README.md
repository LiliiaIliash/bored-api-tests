# bored_api_tests
API-testing framework and tests for the free API at <https://bored-api.appbrewery.com/>

## Run the project
How to build and run the project from scratch.

### Prerequisites
Make sure **Git** and **Python 3** (≥ 3.8) are installed on your machine.

1 — Clone the repository
```bash
git clone https://github.com/LiliiaIliash/bored-api-tests.git

2 — Go to the project directory
cd bored-api-tests/

3 — Create and activate a virtual environment
python -m venv venv            # or: virtualenv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

4 — Install the dependencies
pip install -r requirements.txt

5 — (If needed) Export the project to PYTHONPATH
Most users can skip this step because tests import everything via
relative paths, but if you need to add the root to PYTHONPATH:

Linux / macOS
export PYTHONPATH=$(pwd):$PYTHONPATH

Windows (cmd)
set PYTHONPATH=%cd%;%PYTHONPATH%

6 — Run the tests
pytest -v                # all tests

Happy testing! 🎉