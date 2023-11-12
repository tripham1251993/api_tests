# API Testing
## Introduction
This project with main purpose is to use pytest-bdd to do automated testing

## Project structure
```
api-test/                                   # root project directory
├── conftest.py                             # file used to setup test configurations
├── core_lib/                               # libs directory
│   ├── make_tree_path.py                   # api that used to generate the tree path
│   └── utilities.py                        # utilities
├── data/                                   # data directory
├── format_code.sh                          # format code helper used to format code and check lint
├── locators/                               # locator directory
│   ├── LoginPage.py                        # Login Page locators
│   └── MainMenu.py                         # Main Menu locators
├── pom/                                    # page object model directory
│   └── api/                                # api object model directory 
├── pyproject.toml                          # Configuration file for black tool and other tools
├── README.md                               # README
├── requirements.txt                        # store all required python libs
├── resources/                              # resources directory
├── run.py                                  # run helper file that used to run tests
└── tests/                                  # test root directory
    └── api/                                # test api root directory
        ├── features/                       # used to store api test features
        ├── steps_def/                      # step difinitions for test feature in api
        └── test_steps_and_scenarios.py     # store all scenarios and test steps used on api testing
```

## Setup environment
- You have to install nodejs, npm, python 3.9+ 
```shell
# open git bash if you use windows
# run command
chmod a+x *.sh
# install requirements libraries
# allure commandline, python libs
./install.sh
```

## Run test script
- using `run.py` to run tests:
    + It will install required libraries
    + Cleanup old report
    + Update list scenarios / test steps definition to ensure new features / steps added
    + Check and reformat code
    + Check linting
    + Then run tests with your expected variables
```shell
python run.py \        # change to python3 if you running on macOS or Linux
-t tag_1 -t tag_2 \    # (optional) run test with tags, remove param to run all tests
-n nof_threads \       # (optional) run parallel test
-l log_level \         # (optional) enable log level (default is INFO)
-d report_dir \        # (optional) report directory (default is allure-report)
--install-libraries \  # (optional) Install libraries before running, --no-install-libraries to disabled it (default is --install-libraries)
--show-report          # (optional) show report after running, --no-show-report or remove pram to skip showing report (default is --no-show-report)
```

# Improve in the future:
- ✅ Structure the payload into json file
- ✅ Validate the response with more complicated case
- ✅ Adding validate response time if needed
- ✅ Adding visual report for the test
- ✅ Running the test parallel to save time
- ✅ Split the test into multiple suites like: smoke test, sanity test, regression test....
