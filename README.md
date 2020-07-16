# cse-ta-material
This is a repository that contains the notebooks and other material I created for the CSE 163 class
while working as a
TA for the Allen School at the University of Washington. It has Jupyter Notebooks for all my
research into different libraries for course development, and notebooks with practice problems,
named by topic. Any notebook with 'Notes' in the name is a detailed notebook with notes on the
library named in the title, and any notebook with 'Practice' has practice problems on the topic
named in the title. Practice notebooks also have solutions included. Folders with `.py` files are
similarly named - `Classes Practice` has a practice problem set for classes and objects.
There is also a `data` folder in which I keep all `.csv` files and `.py` files that are related
to creating datasets.

## Altair Notes
This notebook introduces the `altair` library based on JavaScript's `vega.js` library. Much of the
code is copied from Jake Vanderplas and the `altair` documentation, but the experiments, with the
exception of the Seattle Weather plot, is my own.

## Pandas Practice
This notebook has extra practice problems for working with basic functions of the `pandas` library.
This is mostly with filtering, and a little bit of work with `.loc`. It uses the `barley` dataset
from `vega_datasets`.

## Groupby-Loc Practice
This notebook has extra practice problems and some notes on advanced material using the `.groupby`
function of `pandas`. It has some basic `groupby` problems, but it also shows how to use `.groupby`
in a couple more advanced ways, including resetting the index and grouping on multiple columns.
This is particularly useful when dealing with `pd.merge`, as joining on the index column
may be necessary in some cases. This notebook uses a dataset that I came up with surrounding
hypothetical student expenses during college.

## Data Viz and ML Practice
This notebook is more of a guided playground for working with `seaborn` and the basics of
`scikit-learn`. It has practice problems for the main figure-level plots of `seaborn`. This
notebook uses the `barley` and `cars` datasets from `vega-datasets`. The accompanying plots
are stored in `ml_dataviz_img` and `.png` files.

## Classes Practice
This folder has the spec, solutions, and test file to a practice problem for classes and objects,
targeted to be practice for homework #4. Therefore, there is a simple object for data storage, and a
more complex object that is a client of the simpler one. Part of the spec is to implement sorting
and more complex data storage, for example of a `dict` that maps from `String`s to `List`s.

## Environment Notes
This is a markdown file that has my notes for how to use VSCode and Anaconda effectively, in
addition to research and notes I have done that may make it useful to people coming from other
introductory CSE courses, like CSE 143 and 154. It covers:
- what a virtual environment is
- how to set one up using the provided `.yaml` file
- how to make your own environment and install new libraries
- how to configure VSCode to work nicely with Anaconda
- how to run Jupyter Notebooks in VSCode
- how to install Java and configure VSCode to run it
- how to install Apache Maven and configure VSCode to run it
- how to change the settings to get VSCode to work how you want
- how to install Git and connect to GitHub with a new SSH key
- web development in VSCode (very basic)
- useful extensions and what they do