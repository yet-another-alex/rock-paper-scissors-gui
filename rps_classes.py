import json
import rps_constants as rpsc

"""RpsElement class containing a name of the element and a list 
of elements it can win against.
"""
class RpsElement:
    def __init__(self, name, win):
        """Initialization method for RpsElement.

        Args:
            name (string): name of the RpsElement
            win (list of string): list with strings of RpsElements it can win against
        """
        self.name = name
        self.win = win
    
    def __str__(self):
        """__str__ implementation that returns a string rather than RpsElement object.

        Returns:
            string: the name of the RpsElement
        """
        return self.name
    
    def eval(self, o_element):
        """Evaluation function to determine if the current RpsElement (self) can win against 
        an opponent.
        
        Args:
            o_element (RpsElement): the opponent
        
        Returns:
            string: set game condition from rps_constants that can either be win/draw/lose
        """
        if(o_element.name in self.win):
            return rpsc.GAME_CONDITION_WIN
        elif(o_element.name == self.name):
            return rpsc.GAME_CONDITION_DRAW
        else:
            return rpsc.GAME_CONDITION_LOSE

"""RpsGame class containing the filename and a list of RpsElement elements.
"""
class RpsGame:
    def __init__(self, filename):
        """Initialization function. Will accept a filename.

        Args:
            filename (string): filename of a JSON file with an RpsGame representation.
        """
        self.filename = filename
        self.elements = []

    def save(self):
        """Function to save the current RpsGame and its RpsElements with the provided filename.
        """
        f = open(self.filename, "w")
        f.write(self.toJSON())
        f.close()

    def load(self):
        """Function to load and initialize RpsGame with the provided filename.
        """
        # clear everything
        self.elements.clear()
        # open the file
        f = open(self.filename, "r")
        data = json.load(f)
        for el in data["elements"]:
            element = RpsElement(el["name"], el["win"])
            self.elements.append(element)
        f.close()

    def toJSON(self):
        """Quick and dirty JSON serialization.

        Returns:
            string: JSON representation of RpsGame and all of its RpsElements
        """
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)