# How to Use VSCode Like a Boss
### Alex Knowlton
This is a collection of notes I have compiled that have helped me use
VSCode effectively for Python, Java, and Web development. It covers
useful extensions, cool tools, and how to move to developing with VSCode from
a place like jGrasp.

## Python
### What is a virtual environment?
It is usually a good idea to avoid installing Python globally on your computer,
since there are so many plugins that things would get hard to track. Instead,
we generally set up a virtual environment for a particular task or project,
so that everything stays organized. It's basically a box that you put Python
in with some specific tools, instead of leaving everything around. For this
purpose, we use a *package manager* called Anaconda. Anaconda does 2 things:
allows us to manage virtual environments, and install packages and libraries
in specific virtual environments. There are two ways to set up a virtual
environment - using a provided `.yaml` file, and creating one from scratch.
For both of these methods, you will need to download and install Anaconda
from [their website](https://www.anaconda.com/products/individual). If you
are concerned with memory management, you can also install
[Miniconda](https://docs.conda.io/en/latest/miniconda.html), which is
just the bare bones. In that case, I recommend setting your environment up
from scratch.

### Setting up a virtual environment with a `.yaml` file
Download the `.yaml` file that you want to use and store it somewhere on
your computer (it doesn't matter where as long as you remember where it is).
Open up the Anaconda navigator to the Environments page and select 'import'.
Name the environment something you can remember, such as 'cse-classwork', and
navigate the the `.yaml` file. Click 'import', and wait for it to finish.
You're done! You've now set up a virtual environment that you can now use to
develop Python.

### Setting up a virtual environment manually
This option is nice if you want to learn a little more about how Anaconda
works. I recommend doing it this way, since you will then be better prepared
to go out on your own. To start, open the Anaconda Command Prompt from the
Anaconda navigator. You should see this: `(base) C:\users\yourname>`.
In that prompt, type `conda create -n <environment name> python`, where
'environment name' is the name of the environment you want to create, such as
'cse-classwork'. Wait for it to finish, then activate it with
`conda activate <environment name>`. Once the environment is active, you will
see the environment name in parentheses, like `(cse-classwork)`. You can then
install libraries using `conda` or `pip`. See the library documentation
for how it should be installed (the command is just `pip install <library name>`).
For cse163, the required libraries are:
- `pandas`
- `seaborn`
- `geopandas`
- `scikit-learn`
- `matplotlib`
Further, I would recommend installing `flake8`, which is a linter, or a style
checker to make sure everything is formatted properly. Additionally, here are
some other libraries that you may want to use:
- `jupyter` - for running jupyter notebooks locally
- `altair` - for interactive, simple data vizualization
- `pytorch` - another library for machine learning
- `flask` - an easy way to write Python for the web (like Express for those
            people who have used Node.js)

### Making VSCode run with Anaconda
This is actually very easy to do. First, install the Python extension in VSCode
and create a new `.py` file, then open it. At the bottom left of the VSCode window,
you should see a line of text saying "Python interpreter: ". Click on it,
then from the dropdown that appears, select the environment you just made in
Anaconda. Then, there are just semantics - configuring the linter, and
configuring the default number of spaces. Go to the 'View' dropdown and select
'Command Palette'. In the dropdown, enter 'Python: Select Linter', and click
that option when it appears, and select 'flake8'. Then, at the bottom of the
window, in the blue ribbon, click the 'spaces' button and select
'indent using spaces', and select '4'. Now, you can run any `.py` file from
VSCode, using the green arrow that appears when you open a `.py` file.

### Running Jupyter Notebooks in VSCode
For this to work, you need two things: You need the `jupyter` package installed
in your virtual environment. If you don't, open up the terminal, make sure your
virtual environment is active, and type `conda install jupyter`. Then install
the Jupyter extension in VSCode. To create a new notebook, I would say the
easiest way is to select 'View > Command Palette > Create new blank jupyter notebook',
wait for it to load in the VSCode window, then in the top right, make sure your virtual
environment is selected as the Python interpreter (for the notebook - this
is different from selecting it in your VSCode window).

### Installing Java and getting VSCode to recognize it
For this to work, you need to have Java installed. Download Java and install
it (I recommend JDK 11 if you're planning on doing web development, since
that is the latest supported by Spring Boot at the time of writing). Then,
follow [this article](https://www.codejava.net/java-core/how-to-set-java-home-environment-variable-on-windows-10)
to create a `JAVA_HOME` environment variable. To test that this works,
open up a new terminal in VSCode and type `java -v`, and you should see
information about your java installation on your screen. Then, simply install
the Java extension pack from the extensions library in VSCode, and you're ready
to go!

### Installing Apache Maven and getting VSCode to use it
If you're doing anything more complex than CSE 143, you will likely need to
use Maven at some point. Maven is like Anaconda - it manages *dependencies* -
bits of code or packages that your program depends on. To install it, all
you have to do is install Maven and then create a `MAVEN_HOME` environment
variable, just like `JAVA_HOME`. If you have the Java extensions installed,
VSCode will then automatically recognize Maven and be able to use it.

### The .vscode folder and settings.json

### Connecting to GitHub

### Web Development with VSCode and useful tools

### My favorite random/useful extensions
1. ES7 React/Redux/GraphQL/React-Native snippets
  * This has awesome keyboard shortcuts for working with React.js in VSCode
2. Winter is Coming theme
  * Dark and Light color themes for Game of Thrones fans out there
3. Trailing Spaces
  * Deletes trailing spaces on every line when a document is saved
4. VS Code Jupyter Notebook
  * For viewing Notebooks in the VSCode window
5. TODO Highlight
  * Highlights TODO tags so that they are easy to return to