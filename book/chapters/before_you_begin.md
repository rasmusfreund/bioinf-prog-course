# Before you begin {-}

> This chapter serves to get the practicalities out of the way so you can start programming.

## Install Python {-}

In this course, we use a distribution of Python called *Anaconda*. Anaconda is simply an easy way of installing Python on Windows, macOS (Mac), and Linux.

To install Anaconda, head to [this](https://www.anaconda.com/products/individual) site. Click "Download" And select the graphical installer for your platform. Make sure to select **Python 3.7 version** (do *not* download version 2.7).

When the download has completed, you should follow the platform specific instructions:

* **For Windows:** Double-click the file you just downloaded and follow the instructions on the screen. Make a default installation. The installer will also ask you if you want to download and install a program called Visual Studio Code. Do that too.
* **For OSX:** Double-click the file you just downloaded and follow the instructions on the screen. Make a default installation. The installer will also ask you if you want to download and install a program called Visual Studio Code. Do that too.

## Install the text editor {-}

You will also need a *text editor*. A text editor is where you write your Python code and for this course, we will use one called *Sublime Text*. To install *Sublime Text*, go to
[this](https://www.sublimetext.com/3) site. Again, you'll have to download the version of Sublime Text that fits your platform. At the top of the page, click **Windows 64 bit** if you're running Windows and **OSX** if you are on a Mac.

* **For Windows:** Double-click the `.exe` file you just downloaded and follow the instructions on the screen.
* **For OSX:** Double click the `.dmg` file you just downloaded. A small window should open showing you two icons: *Applications* and *Sublime Text*. Drag the *Sublime Text* icon onto the *Applications* icon. You can now close the window.

You should now have *Sublime Text* installed. If you open *Sublime Text*, you should see something like [@fig:figure0]:

![Sublime Text, screenshot](./images/sublime.png){#fig:figure0}

## The terminal {-}

The last thing you need is a tool to make Python run the programs you write. Fortunately, that is already installed. On OSX and Linux this is a program called *Terminal*. You can find it by typing "Terminal" in Spotlight Search. On Windows it is called the *Anaconda Prompt* and was installed along with Anaconda Python. You should be able to find it from Start menu.

What is *Anaconda Prompt* and this *Terminal* thing, you ask! Both programs are what we call *terminal emulators*. They are programs used to run other programs, such as the ones you are going to write. I will informally refer to both *Terminal* and *Anaconda Prompt* as "the terminal" So if I write something like "open the terminal" later in the book you should open *Anaconda Prompt* if you are running Windows. If you are running OS X, you should open the *Terminal* application.

If you open *Anaconda Prompt* you should see something like @fig:powershell. The OSX Terminal looks like @fig:terminal, possibly with a different background color.

![Screenshot of Anaconda Prompt](./images/anaconda_prompt.jpg){#fig:prompt}

![Screenshot of Terminal](./images/terminal.png){#fig:terminal}

The terminal is a very useful tool. However, to use it you need to know a few basics. First of all, a terminal lets you execute commands on your computer. You simply type the command you want and then hit enter. The place where you type is called a prompt and it may look a little different depending on which terminal emulator you use. In this book we represent the prompt with the character `$`.

When you open the terminal you'll be located in a folder. You can see which folder you are in by typing `pwd` on OSX and `cd` on windows, and then press `Enter` on the keyboard. When you press `Enter` you tell the terminal to execute the command you just wrote. In this case, the command you typed simply tells you the path of the folder we are in. If I do it I get:

```
$ pwd
/Users/kasper/programming
```

If I had been on a windows machine it would have looked something like: 

```
$ cd
C:\Users\kasper\programming
```

So right now I am in the folder `programming`. `/Users/kasper/programming` is the "full address" of the folder with dashes (or backslashes on windows) separating folders. So `programming` is a subfolder of `kasper` which is a subfolder of `Users`. That way you not only know which folder you are in but also where that folder is. Let us see what is in this folder. On OSX you type the `ls` command (l as in Lima and s as in Sierra). On windows you type `dir`. When I do that and press `Enter` I get:

```
$ ls
notes projects
```

It seems that there are two other folders, one called `notes` and another called `projects`. If you are curious about what's inside `notes` you can "walk" into the folder with the `cd` command. To use this command you must specify which folder we want to walk into (in this case `notes`). We do this by typing `cd`, then a space and the then name of the folder. This is the same OSX and Windows. When I press enter I get:

```
$ cd notes
$
```

It seems that nothing really happened, but if I run the `pwd` command (`cd` on Windows) now to see which folder I am in, I get:

```
$ pwd
/Users/kasper/programming/notes
```

Just to keep track of what is happening: before we ran the `cd` command we were in the directory `/Users/kasper/programming` folder, and now we're in `/Users/kasper/programming/notes`. This means that we can now use the `ls` command (`dir` on Windows) to see what is in the `notes` folder:

```
$ ls
$
```

Again it seems like nothing happened. Well, `ls` and `dir` do not show anything if the folder we are in is empty. So `notes` must be empty. Let us go back to where we came from. To
walk "back" or "up" to `/Users/kasper/programming` we again use the `cd` command, but this time we do not tell it to go to a specific folder. Instead, we use the special name `..` to say that we wish to go to the parent folder called `programming`, i.e. the folder we just came from:

```
$ cd ..
$ pwd
/Users/kasper/programming
```

Now when we run the `pwd` (or `cd`) command we see that we are back where we started. Let us see if the two folders are still there:

```
$ ls
notes projects
```

They are! 

Hopefully, you are now able to use navigate your folders and see what is in them. You will need this later to go to the folders with the code you write for the exercises and projects during the course.

| Action | Windows | OSX |
|:---|:---|:---|
| Show current folder | `cd` | `pwd` |
| List folder content | `dir` | `ls` |
| Go to subfolder "notes" | `cd notes` | `cd notes` |
| Go to parent folder | `cd ..` | `cd ..` |


## You are all set {-}

Well done! You are all set to start the course. Have a cup of coffee and look forward to your first program. While you sip your coffee I need to you take an oath (one of three related to this course). Raise your right hand! (put your coffee in the left).

> **Oath 1:** I swear never to copy and paste examples from this book into *Sublime Text*. I will *always* read the examples in the book and and *type* them into my editor.

This serves three purposes (as if one was not enough):

1. You will be fully aware of each and every bits of each example.
2. You will learn to write code correctly and without omissions and mistakes.
3. You will get Python “into your fingers”. It sounds silly, but it *will* get into your fingers.









