# Installation instructions {-}

In this course, we use a distribution of Python called *Anaconda*. Anaconda is simply an easy way of installing Python on and PyMol.

## Install Python {-}

To install Anaconda, head to [this](https://www.anaconda.com/download) site. Scroll down a bit and click the big green Download button where it says **Python 3.7 version** (do *not* download version 2.7).

When the download has completed, you should follow the platform specific instructions:

* **For Windows:** Double-click the `.exe` file you just downloaded and follow the instructions on the screen. Make a default installation. The installer will also ask you if you want to download and install a program called Visual Studio Code. Do that too.
* **For OSX:** Double-click the `.pkg` file you just downloaded and follow the instructions on the screen. Make a default installation. The installer will also ask you if you want to download and install a program called Visual Studio Code. Do that too.

## Install PyMol {-}

If you are on a Windows machine, find the program called "Anaconda Prompt". If you are on a Mac, find the program called "Terminal". These are both programs where you can type commands to run other programs. When you open *Anaconda Prompt* you should see something like @fig:powershell. The OSX Terminal looks like @fig:terminal, possibly with a different background color.

![Screenshot of Anaconda Prompt](./images/anaconda_prompt.jpg){#fig:prompt}

![Screenshot of Terminal](./images/terminal.png){#fig:terminal}

Now paste this into Anaconda Prompt (or Terminal).

```
conda create -n BSF19 -c schrodinger pymol python=3.7
```

Then hit enter. Now the program works for some time and then writes a long list of packages. These are all the packages and dependencies required by python and PyMol in versions that all fit together. It looks something like this:

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

Just hit enter again to Proceed. Once you do that, the program starts to download and install all the packages. It takes a bit of time.

When installation is complete the program writes:

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

## Start PyMol {-}

From now on, you can start PyMol by typing these commands in Anaconda Prompt if you are on windows, or Terminal if you are on Mac:

```
conda activate BSF19
```

(hit enter)

```
pymol
```

(hit enter)
