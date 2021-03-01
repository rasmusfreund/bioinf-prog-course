# Appendix: Conda and PyMol

In bioinformatics, we install packages and programs so we can use them in our analyses and pipelines. Sometimes, however, the versions of packages you need for one project conflicts with the versions you need for other projects that you work on in parallel. Such conflicts seem like an unsolvable problem. Would it not be fantastic if you could create a small world, insulated from the rest of your Anaconda installation? Then that small world could only contain the packages you needed for a single project. If each project had its own isolated world, then there would be no such version conflicts. Fortunately, there is a tool that lets you do just that, and its name is Conda.

> Conda is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them.

The small worlds that Conda creates are called "environments". You can create as many environments as you like, and then use each one for a separate bioinformatics project, course, bachelor project, or whatever you would like to insulate from everything else. Conda also downloads and installs the packages for you and it makes sure that the software packages you install in each environment are compatible. It even makes sure that packages needed by packages (dependencies) are installed. Conda is truly awesome.


## Creating an environment with PyMol {-}

When you install Anaconda, Conda makes a single base environment for you. It is called "base" and this is why it says "(base)" on your terminal.

Many of you take the course "Biomolecular Structure and Function" (let us call that BSF) alongside this course. In BSF, you need to install programs (e.g. PyMol) that may conflict with the packages you need for this course. So we will create an isolated Conda environment for BSF to avoid such conflicts. Conda is a program you run from the command line, just like `python` or `cd`. So open your terminal (i.e., the "Terminal" program if you are on a Mac and the "Anaconda Prompt" program if you are on Windows). Now copy/paste this line into the terminal and press return (enter):

```
conda create -n BSF -c schrodinger pymol
```

This command runs the Conda program and tells it to create a new environment with name "BSF" and to install pymol and python in that environment. Once you hit enter Conda works for some time and then writes a long list of packages in your terminal. These are all the packages and dependencies required by python and PyMol in versions that all fit together. The end of the list looks something like this:

```
  pymol              schrodinger/osx-64::pymol-2.4.0-py38h4268d49_0
  pyopenssl          pkgs/main/noarch::pyopenssl-19.1.0-py_1
  pyqt               pkgs/main/osx-64::pyqt-5.9.2-py38h655552a_2
  pysocks            pkgs/main/osx-64::pysocks-1.7.1-py38_1
  python             pkgs/main/osx-64::python-3.8.3-h26836e1_2
  qt                 pkgs/main/osx-64::qt-5.9.7-h468cd18_1
  readline           pkgs/main/osx-64::readline-8.0-h1de35cc_0
  requests           pkgs/main/noarch::requests-2.24.0-py_0
  rigimol            schrodinger/osx-64::rigimol-1.3-2
  setuptools         pkgs/main/osx-64::setuptools-49.2.0-py38_0
  sip                pkgs/main/osx-64::sip-4.19.8-py38h0a44026_0
  six                pkgs/main/noarch::six-1.15.0-py_0
  sqlite             pkgs/main/osx-64::sqlite-3.32.3-hffcf06c_0
  tk                 pkgs/main/osx-64::tk-8.6.10-hb0a8c7a_0
  urllib3            pkgs/main/noarch::urllib3-1.25.9-py_0
  wheel              pkgs/main/osx-64::wheel-0.34.2-py38_0
  xz                 pkgs/main/osx-64::xz-5.2.5-h1de35cc_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3
  zstd               pkgs/main/osx-64::zstd-1.4.5-h41d2c2f_0


Proceed ([y]/n)?
```

Just hit enter again to Proceed. Once you do that, Conda starts to download and install all the packages. It takes a bit of time.

At the end Conda writes:

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate BSF
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

Conda tells you both how to enter (activate it) an environment and how to leave it (deactivate it). To activate your BSF environment, you enter:

```
conda activate BSF
```

and press enter. Voila, you are now in the BSF environment. Notice how the command prompt changed from "(base)" to "(BSF)" to show that you are now in the BSF environment. To run PyMol that you installed in this environment, just type

```
pymol
```

and hit enter.

Now try to close PyMol. Then go back to your terminal and type

```
conda deactivate
```

Notice how it now again says "(base)" on your command prompt. That is because you are back in your base environment. Try to type `pymol` (and hit enter), you terminal will tell you that it could not find anything called `pymol`. This is the way it should be. That is because PyMols is installed in the BSF environment, *not* in the base environment. It illustrates how the base environment is entirely separate from the BSF environment you just made.

## Starting PyMol {-}

From now on, you can start PyMol by typing these commands into the terminal (Anaconda Prompt on Windows):

```
conda activate BSF
```

(hit enter)

```
pymol
```

(hit enter)

