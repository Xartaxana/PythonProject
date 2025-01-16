# Final Pythin Project

## Overview
This project includes automated UI and API tests for https://jsonplaceholder.typicode.com/ .

## Local Setup
1. Install Python 3.8+
2. Clone the repository: `git clone <https://github.com/Xartaxana/PythonProject.git>`
3. Navigate into the project directory: `cd Project`
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright: `playwright install`

## Running Tests

You can execute the tests using **pytest** with markers:

- To run all UI tests:

  ```bash
  pytest -m "ui"

- To run all API tests:

  ```bash
  pytest -m "api"
  
## Logging
Log files are generated and stored in the `logs/` directory.

## Reporting
Test reports are automatically generated and stored in the `reports/` directory after the execution of the corresponding tests.
To view the HTML report, simply open the `report.html` file in any web browser.
