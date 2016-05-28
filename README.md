CAS Categorization
==================

[![Join the chat at https://gitter.im/WildCAS/CASCategorization](https://badges.gitter.im/WildCAS/CASCategorization.svg)](https://gitter.im/WildCAS/CASCategorization?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Circle CI](https://circleci.com/gh/WildCAS/CASCategorization/tree/develop.svg?style=svg)](https://circleci.com/gh/WildCAS/CASCategorization/tree/develop)

CAS Categorization is a playground the test the categorizing CAS Activities.
Because of the limitations of Heroku, this application will be employing
[Conda](http://conda.pydata.org/docs/) to manage our libraries. Check out
our hosted versions:
- [Stable](http://wildcats.herokuapp.com/)
- [Beta](https://wildcats-staging.herokuapp.com/)

## System Requirements:
- Python 3
- PostgreSQL

## Local Setup:
1. Ensure that Python 3 is installed on your local machine.
2. Install Miniconda with the instructions
[here](http://conda.pydata.org/docs/install/quick.html).
3. Set up the Conda environment with the specified settings using
`conda env create -f environment.yml`.
    - If you have a Mac and run into issues at this stage, please completely
    remove `libgfortran=1.0=0` and `scipy=0.17.0=np110py35_1` from
    `environment.yml` and try again.
4. Activate Conda environment: `source activate cas`
    - If you had to omit those lines mentioned in 3, please
    manually reinstall the packages with the following commands:
    `conda install -n cas scipy`.
7. Install the pip requirements: `pip install -r requirements.txt`

## Package/Requirements File:
Pip is our main package management file, as such, please install packages using
Pip whenever possible. Thus, when executing `pip freeze > requirements.txt`,
please ensure that the requirements.txt file does **not** have scipy.

**Requirement file notes:** Scipy cannot be installed via pip
because of its required dependencies (BLAS/Lapack). Therefore, it is not in
requirements.txt file.

## License
Copyright 2016 The WildCAS Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS-IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
