# Automation Test

## Project dependencies
- pytest, pytest-bdd, gherkin, python, pytest-html and selenium

## Project setup
- Clone the git repo
- Solve the dependencies
- `config.cfg` has all the env variables
- Run `pytest --html=Reports/report.html`

## Project Structure
- `base`: Initiate the driver
- `features`: Gherkin feature files
- `lib`: middleware for reading selectors and config elements
- `pages`: All the actions for different page functionalities
- `selectors`: All the selectors are under this directory
- `tests`: All the test cases written
