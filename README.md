# SPARCats

A o<sup>2</sup>S<sup>2</sup>PARC tool to accellerate data discovery by AI bring take breakthroughs in the laboratory into healthcare. SPARCats generate synthetic augmented physiological data available through the SPARC Data Portal to improve AI training. 

![alt text][logo]

[logo]: https://github.com/SPARC-FAIR-Codeathon/2025-team-F/res/sparcats.jpg

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
* [Our solution - (SPARCats)](#our-solution---(SPARCats))
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
This is the repository of team SPARCats (Team #F) of the 2025 SPARC Codeathon. Information about the 2025 SPARC Codeathon can be found [here](https://sparc.science/news-and-events/events/2025-sparc-fair-codeathon). 

No work was done on this project prior to the Codeathon. 
## Introduction
The NIH Common fund program *Stimulating Peripheral Activity to Relieve Conditions* ([SPARC](https://commonfund.nih.gov/sparc)) seeks to understand how electrical signals control internal organ function. In doing so it explores how therapeutic devices might modulate nerve activity to treat conditions like hypertension, heart failure, and gastrointestinal disorders. To this end, data have been compiled from 60+ research groups, involving 3900+ subjects across 8 species from  49 different anatomical structures.  

The SPARC Portal offers a user-friendly interface to access and share resources from the SPARC community. It features well-curated, high-impact data, SPARC projects, and computational simulations, all available under the “[Find Data](https://sparc.science/data?type=dataset)” section.
## The problem
AI can produce powerful tools for predicting and analysing a wide range of physiological biomarkers. Researchers want to use physiological time series data train AI models to answer scientific questions and distill impactful medical insights. They need a tool that allows them to seamlessly discover and generate augmented data from publicly available physiological data. 

### Limited Accessibility:
- SPARC boasts a trove of datasets and tools, but these can be difficult to access and deploy for users that are not proficient in coding. 
### Poor Findability
- There is no tool to easily search and collect relevant datafiles from the data sets available on SPARC, leaving data underutilised.   
### Difficulties in Reusability:
- Without a standardized approach to data augmentation, researchers may struggle to replicate or pipelines for different datasets or research contexts.
- There is limited data available that is similar enough to be used for training a given AI tool. Data augmentation 

## Our solution - (SPARCats)
We have developed a robust data augmentation toolkit in Python (SPARCats) that runs within o<sup>2</sup>S<sup>2</sup>PARC to generate synthetic datasets. 

SPARCats has been developed to adhere to and enhance the [FAIR](https://www.nature.com/articles/sdata201618) and [TRUST](https://www.nature.com/articles/s41597-020-0486-7) principles core to SPARC
    
## Impact
This can be used to enhance understanding of the autonomic and peripheral nervous systems and drive

### Develops new capabilities of SPARC tools within o<sup>2</sup>S<sup>2</sup>PARC


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
    <td><a href="tutorials/tutorial_1_setting_up.ipynb">
    Tutorial 1: 
    </a></td>
    <td> <b>Getting started</b> - In this tutorial we ...
    absolute basics for no code new to osparc
    Show how data augmentation improves performance & generalization of the resulting AI.
    </td>
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_2_training_with_your_own_data.ipynb">
    Tutorial 2: 
    </a></td>
    <td> <b>Finding scaffolds</b> - In this tutorial we ...
    Augment your data, train AI, evaluate
    </td>
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_3_training_with_existing_data.ipynb">
    Tutorial 3: 
    </a></td>
    <td> <b>Generating analytics</b> - In this tutorial we ...
    Augment published data, train AI, evaluate. 
    </td>
  </tr>
    <tr>
    <td><a href="tutorials/tutorial_4_Using_existing_models.ipynb">
    Tutorial 3: 
    </a></td>
    <td> <b>Generating analytics</b> - In this tutorial we ...
    Augment data, evaluate with pre-trained AI. Emphasise model should be trained on data similar to evaluation. 
    </td>
  </tr>

  <tr>
    <td><a href="tutorials/tutorial_5_transfer_learning.ipynb">
    Tutorial 5: 
    </a></td>
    <td> <b>Into the flow</b> - In this tutorial we ...
    Import data, augment, train AI. Import own data, augment, train AI more, evaluate. Emphasise that data should be similar.
    </td>
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
