# rock-paper-scissors-gui

## Rock, Paper, Scissor but a Tkinter Python tutorial

This code was created to highlight some of the interesting things you can do with Python, Tkinter, JSON and a very boring and overused example (rock, paper, scissors).
The entire code was created in a specific way to highlight some specific things for a tutorial.

The tutorial series to go alongside the code can be found [here](https://alex-does.hashnode.dev/series/python-rps).

## GUI

![Basic screenshot of the GUI](https://raw.githubusercontent.com/yet-another-alex/rock-paper-scissors-gui/master/screens/basic.png)

The GUI is Tkinter based and allows for you to choose one of the provided options (e.g. rock, paper or scissors) - the opponent will choose one at random as well.
The "load"-Button will allow to load a different JSON-configuration file that will present you with more or different options to choose from.
Included in this repository is one for rock, paper, scissors, lizard, spock (rps.json).

![Screenshot of RPSLS](https://raw.githubusercontent.com/yet-another-alex/rock-paper-scissors-gui/master/screens/rps.png)

## JSON

The JSON is very simple and basically consists of a filename and a list of elements. Each element has a list of string that he can win against.
The very basic standard example can be found below or in the repo:

```
{
    "elements": [
        {
            "name": "rock",
            "win": [
                "scissors"
            ]
        },
        {
            "name": "paper",
            "win": [
                "rock"
            ]
        },
        {
            "name": "scissors",
            "win": [
                "paper"
            ]
        }
    ],
    "filename": "vanilla.json"
}
```
