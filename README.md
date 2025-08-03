# sparcats

A Python tool to generate synthetic augmented physiological data based on date available through the SPARC Data Portal. 

![Python 3](https://img.shields.io/badge/Python->=3.9-blue)
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GitHub issues-closed][issues-closed-shield]][issues-url]
[![License][license-shield]][license-url]
[![Contributor Covenant][code-of-conduct-shield]](CODE_OF_CONDUCT.md)
[![PyPI version fury.io][pypi-shield]][pypi-url]
[![Conventional Commits][conventional-commits-shield]][conventional-commits-url]

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-codeathon/sparcats.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-codeathon/sparcats/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-codeathon/sparcats.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-codeathon/sparcats//stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-codeathon/sparcats/.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-codeathon/sparcats/issues
[issues-closed-shield]: https://img.shields.io/github/issues-closed/SPARC-FAIR-codeathon/sparcats.svg
[issues-closed-url]: https://GitHub.com/SPARC-FAIR-Codeathon/sparc-me/issues?q=is%3Aissue+is%3Aclosed
[license-shield]: https://img.shields.io/github/license/SPARC-FAIR-codeathon/sparcats.svg?style=flat-square
[license-url]: https://github.com/SPARC-FAIR-codeathon/sparcats/blob/master/LICENSE
[code-of-conduct-shield]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[pypi-shield]: https://badge.fury.io/py/sparcats.svg
[pypi-url]: https://pypi.python.org/pypi/sparcats/
[conventional-commits-shield]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
[conventional-commits-url]: https://conventionalcommits.org



## Table of contents
* [About](#about)
* [Introduction](#introduction)
* [The problem](#the-problem)
* [Our solution - (sparcats)](#our-solution---(sparcats))
* [Impact](#impact)
* [Contributing](#contributing)
* [Setting up sparcats](#setting-up-sparcats)
* [Reporting issues](#reporting-issues)
* [Contributing](#contributing)
* [FAIR practices](#fair-practices)
* [License](#license)
* [Team](#team)
* [Acknowledgements](#acknowledgements)


## About
This is the repository of team sparcats (Team #F) of the 2025 SPARC Codeathon. Information about the 2025 SPARC Codeathon can be found [here](https://sparc.science/news-and-events/events/2025-sparc-fair-codeathon). 

No work was done on this project prior to the Codeathon. 
## Introduction
The NIH Common fund program *Stimulating Peripheral Activity to Relieve Conditions* ([SPARC](https://commonfund.nih.gov/sparc)) seeks to understand how electrical signals control internal organ function. In doing so it explores how therapeutic devices might modulate nerve activity to treat conditions like hypertension, heart failure, and gastrointestinal disorders. To this end, data have been compiled from 60+ research groups, involving 3900+ subjects across 8 species from  49 different anatomical structures.  

The SPARC Portal offers a user-friendly interface to access and share resources from the SPARC community. It features well-curated, high-impact data, SPARC projects, and computational simulations, all available under the “[Find Data](https://sparc.science/data?type=dataset)” section.
## The problem


### Limited Accessibility:
- 
### Poor Interoperability:
- 
### Difficulties in Reusability:
- Without a standardized approach to data augmentation, researchers may struggle to replicate or pipelines for different datasets or research contexts.

## Our solution - (sparcats)
We have developed a robust data augmentation toolkit in Python (sparcats) that runs within o<sup>2</sup>S<sup>2</sup>PARC to generate synthetic datasets. This Python module enhancess the **FAIR**ness of SPARC data by:

- **F**indable
  - 
- **A**ccessible
  - 
- **I**nteroperable
  - 
- **R**eusable
  - 
    
## Impact
### Develops new capabilities of SPARC tools within oSPARC



### Increase visibility of the value within SPARC's public data 



## Setting up sparcats
### Pre-requisites 
- [Git](https://git-scm.com/)
- Python versions:
   - 3.9 *TODO*
###  Installing via PyPI

Here is the [link](https://pypi.org/project/sparcats/) to our project on PyPI *TODO*
```
pip install sparcats
```
### From source code
#### Downloading source code
Clone the sparcats repository from github, e.g.:
```
git clone git@github.com:SPARC-FAIR-codeathon/sparcats *TODO* 
```

### Installing dependencies
```
pip install requirements.txt *TODO*
```

## Using sparcats
Sparcats has been developed to be used within o<sup>2</sup>S<sup>2</sup>PARC with little to node coding experience required. To demonstrate this and showcase the steps required to implement we have a series of tutorials and demo usecases: 

<table>
<thead>
  <tr>
    <th> Tutorial *TODO*</th>
    <th> Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="tutorials/tutorial_1_getting_started.ipynb">
    Tutorial 1: 
    </a></td>
    <td> <b>Getting started</b> - In this tutorial we ...</td>
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_2_importing_data.ipynb">
    Tutorial 2: 
    </a></td>
    <td> <b>Finding scaffolds</b> - In this tutorial we ...</td>
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_3_augmenting_data.ipynb">
    Tutorial 3: 
    </a></td>
    <td> <b>Generating analytics</b> - In this tutorial we ...</td>
  </tr>
  <tr>
    <td><a href="tutorials/use_case_1_Predictive.ipynb">
    Tutorial 4: 
    </a></td>
    <td> <b>New tags</b> - In this tutorial we ...</td>
  </tr> 
  <tr>
    <td><a href="tutorials/use_case_2_Classification.ipynb">
    Tutorial 5: 
    </a></td>
    <td> <b>Into the flow</b> - In this tutorial we ...
  </tr>
</tbody>
</table>
<p align="center">
</p>
<br/>

## Reporting issues 
To report an issue or suggest a new feature, please use the [issues page](https://github.com/SPARC-FAIR-codeathon/sparcats/issues). 
Please check existing issues before submitting a new one.

## Contributing
To contribute: fork this repository and submit a pull request. Before submitting a pull request, please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md). If you found this tool helpful, please add a GitHub Star to support further developments!

### Project structure
* `/src/` - Directory of sparcats python module.
* `/tutorials/` - Directory of tutorials and use cases showcasing sparcats python module in use.
  

## FAIR practices
We have assessed the FAIRness of our sparcats tool against the FAIR Principles established for research software. The details are available in the following [sparcats-Fairness](/docs/sparcats-FAIRness.docx)
*TODO*
## License
Sparcats is open source and distributed under the Apache License 2.0. See [LICENSE](https://github.com/SPARC-FAIR-Codeathon/2025-team-F/blob/main/LICENSE) for more information.
## Team
* [Michael Hoffman](https://github.com/Moffhan) (Writer)
* [Mathias Roesler](https://github.com/mathiasroesler) (Developer)
* [Mishaim Malik](https://github.com/Mmal151) (Developer)
* [Omkar Athavale](https://github.com/OmkarAthavale) (Lead, SysAdmin)
## Acknowledgements
- We would like to thank the 2025 SPARC Codeathon organizers for their guidance and support during this Codeathon.