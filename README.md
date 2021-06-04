# shapes
Learn Python by implementing simple drawing application▪️🔺🔹

## Development
### PyCharm

> PyCharm is an integrated development environment used in computer programming, specifically for the Python language.

It features code completion, syntax highlighting and smart navigation. You can use any other editor (for example Visual Studio Code), but PyCharm is much friendlier :)

Install PyCharm: https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone

### Python

In order to code in Python you need to have Python installed. You can install Python globally or use virtual environments. 

If you want to installl Python globally use: https://www.python.org/downloads/

However, **preferred way is to use virtual environments**.

#### Virtual Environment

> The main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

So for example imagine you are working on multiple projects, project A uses `numpy==1.20.3`, project B uses `numpy==0.9.6` or different version of Python.  Without virtual environment (using global Python installation) you would need to uninstall and install dependencies every time you switch between projects. With virtual environment you don't have to worry about it, because each project have its own, separate environment that can run different dependencies.

Install pyenv: check documentation - https://github.com/pyenv/pyenv#homebrew-on-macos or **use this nice tutorial https://youtu.be/-5vd5GEpF-w** (there are number of tutorial for other operating systems)

And then go inside `shapes` project in the terminal, and prepare virtual environment: 

```bash
$ cd shapes
$ pyenv install 3.8.2
$ pyenv virtualenv 3.8.2 shapes
```

#### Configuring PyCharm to use the virtual environment

- Preferences (eg. MacOS: `⌘` + `,`)
- Project: `shapes` / Project interpreter
- Click on the "gear" icon, and then select "Add"
- Virtualenv environment
- Existing environment
- Choose Python 3.8.2 (shapes) that should me located in `~/.pyenv/versions/shapes/bin/shapes`

After fulfilling the steps above, just for safety, **restart the PyCharm**.

- Open terminal in PyCharm and execute `pip install -r requirements-all.txt`

## Scenario

You have joined Awesome Drawings Inc. as a Software Engineer. You will be responsible for extending company's core application - `shapes` - that was started by other engineers and requires finishing. 

`shapes` is basically a high level interface for `matplotlib` library. Instead of using raw objects from the `matplotlib` library user can describe image in JSON format and application will draw it. 

You will have to solve number of tasks to make this application better and more powerful. 

## Code structure

Let's focus on the code organisation for a while.

```
shapes/                - root directory
  res/                 - folder with resources (JSON files), that can be used as input for the program
  src/                 - folder with Python code       
    data.py            - everything related to data manipulation (saving, loading)
    drawing.py         - everything related to drawing
    errors.py          - custom errors
    models.py          - shapes definition
  .gitignore           - paths that are excluded from version control system
  README.md            - file you are currently reading
  requirements.txt     - dependencies that are used by the program during runtime
  requirements-all.txt - requirements.txt + requirements-dev.txt (joined together)
  requirements-dev.txt - dependencies that are used during development
  shapes.py            - script that is starting the application 
```

This structure was proposed by some other engineer, feel free to change the structure if you think it can be arranged in a better way.

## Run the app

```bash
$ ./shapes.py res/house.json
```

This will save an image in the `out` directory. Open `house.png` to see the result.

## Tasks

#### TASK 1 - Add Square

It is possible to draw squares as rectangles, but it would be nice to support shorter syntax for squares. 

1. Add `Square` class in `models.py`. 
2. Update `Drawing` class
3. Add `draw_square` function in `drawing.py`
4. Check if your solution works, add some square to `house.json` (you can define `building` as a square)

#### TASK 2 - XXX

#### TASK 3 - XXX

#### TASK 4 - XXX

#### TASK 5 - XXX

### Example solution

I highly encourage you to solve the tasks on your own and then check the example solution.

https://github.com/pkardas/shapes/tree/example-solution

