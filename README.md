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

#### TASK 2 - Add Polygon

Right now it is not possible to draw more advanced shapes, for example triangles. Similarly to TASK 1 add `Polygon` shape.

`matplotlib` supports drawing polygons - `plt.Polygon`, this object expects lists of nodes defined as (X, Y) pairs.

Test your solution using following JSON:

```json
"polygons": [
  {
    "name": "roof",
    "points": [
      {
        "x": 100,
        "y": 110
      },
      {
        "x": 150,
        "y": 140
      },
      {
        "x": 200,
        "y": 110
      }
    ],
    "color": "red"
  }
]
```



#### TASK 3 - Get rid of explicit order

Right now user have to explicitly define order or shapes:

```json
"order": [
  "sun",
  "building",
  "window_0",
  "window_1",
  "door",
  "grass",
  "roof"
]
```

which is slightly annoying, because you have to remember about various objects and edit JSON in two places when adding a new element.

Purpose of this task is to get rid of explicit order and allow user to define shapes as follows:

```json
...
"shapes": [
  {
    "name": "sun",
    ...
  },
  {
    "name": "grass",
    ...
  },
  ...
]
```

So `shapes` should be just list of objects, order in the list will define drawing order.

Start by updating `Drawing` in `models.py`. Get rid of `circles`, `rectangles`, `squares`, `polygons` `order`, and replace them with single attribute - `shapes: List[Union[Circle, Rectangle, Square, Polygon]]`.

Remove `get_shape` method from `Shape`. Update `draw` function in `drawing.py`.

#### TASK 4 - XXX

#### TASK 5 - XXX

### Example solution

I highly encourage you to solve the tasks on your own and then check the example solution.

https://github.com/pkardas/shapes/tree/example-solution

