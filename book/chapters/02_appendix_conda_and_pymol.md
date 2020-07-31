# Appendix: Conda and PyMol {-}

In bioinformatics, we install packages and programs for use in our analyses and pipelines. Sometimes, however, the versions of packages you need for one project conflicts with the versions you need for other projects that you work on in parallel. Such conflicts seem like an unsolvable problem. Would it not be fantastic if you could create a small world, insulated from the rest of your Anaconda installation. Then that small world could only contain the packages you needed for a single project. If each project had its own isolated world, then there would be no such conflicts. Fortunately, there is a tool that lets you do just that, and its name is Conda. The small worlds that Conda creates are called "environments," and you can create as many as you like, and then switch between them as you switch between your bioinformatics projects.

Conda also downloads and installs the packages for you and makes sure that the packages you install in each environment are compatible.  It even makes sure that packages needed by packages  (dependencies) are installed. Conda is truly awesome.

> Conda is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them.

## Creating an environment with PyMol {-}

When you install Anaconda, Conda makes a single base environment for you. It is called "base" and this is why it says "(base)" on your terminal.

Many of you take the course "Biomolecular Structure and Function" (let us call that BSF19) alongside this course. In BSF19, you need to install programs (e.g. PyMol) that may conflict with the packages you need for this course. So we will create an isolated Conda environment for BSF19 to avoid such conflicts. Conda is a program you run from the command line, just like `python` or `cd`. So open your terminal (i.e., the "Terminal" program if you are on a Mac and the "Anaconda Prompt" program if you are on Windows). Now copy/paste this line into the terminal and press return (enter):

```
conda create -n BSF19 -c schrodinger pymol python=3.7
```

This command runs the Conda program and tells it to create a new environment with name "BSF19" and to install pymol and python in that environment. Once you hit enter Conda works for some time and then writes a long list of packages in your terminal. These are all the packages and dependencies required by python and PyMol in versions that all fit together. It looks something like this:

```
  readline           pkgs/main/osx-64::readline-7.0-h1de35cc_5
  requests           pkgs/main/osx-64::requests-2.22.0-py37_0
  rigimol            schrodinger/osx-64::rigimol-1.3-2
  setuptools         pkgs/main/osx-64::setuptools-41.0.1-py37_0
  sip                pkgs/main/osx-64::sip-4.19.8-py37h0a44026_0
  six                pkgs/main/osx-64::six-1.12.0-py37_0
  sqlite             pkgs/main/osx-64::sqlite-3.29.0-ha441bb4_0
  tk                 schrodinger/osx-64::tk-8.6.9-x11tk0_2000
  urllib3            pkgs/main/osx-64::urllib3-1.24.2-py37_0
  wheel              pkgs/main/osx-64::wheel-0.33.4-py37_0
  xz                 pkgs/main/osx-64::xz-5.2.4-h1de35cc_4
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3
  zstd               pkgs/main/osx-64::zstd-1.3.7-h5bba6e5_0


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
#     $ conda activate BSF19
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

Conda tells you both how to enter (activate it) an environment and how to leave it (deactivate it). To activate your BSF19 environment, you enter:

```
conda activate BSF19
```

and press enter. Voila, you are now in the BSF19 environment. Notice how the command prompt changed from "(base)" to "(BSF19)" to show that you are now in the BSF19 environment. To run PyMol that you installed in this environment, just type

```
pymol
```

and hit enter.

Now try to close PyMol. Then go back to your terminal and type

```
conda deactivate
```

Notice how it now again says "(base)" on your command prompt. That is because you are back in your base environment. Try to type `pymol` (and hit enter), you terminal will tell you that it could not find anything called `pymol`. This is the way it should be. That is because PyMols is installed in the BSF19 environment, *not* in the base environment. It illustrates how the base environment is entirely separate from the BSF19 environment you just made.

## Starting PyMol {-}

From now on, you can start PyMol by typing these commands into the terminal (Anaconda Prompt on Windows):

```
conda activate BSF19
```

(hit enter)

```
pymol
```

(hit enter)

