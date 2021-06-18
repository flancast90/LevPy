# LevPy
> Text-based games made easy!

[![stable version badge](https://img.shields.io/badge/Stable-v.2.1-brightgreen)](https://github.com/flancast90/LevPy/releases/latest)[![repo size badge](https://img.shields.io/badge/size-2.276kb-informational)](https://www.github.com/flancast90/LevPy)

# About 
LevPy is a simple python file/function that allows the creation of text-based games easily through JSON data. For example, in ```main.py```, you could include the following "level": 
```python
firstVar = '{"greeting":"Hello and welcome to LevPy! Type \"tell me more\" to learn more","tell me more":"LevPy is a python library that makes making games easy!"}'
```

# Walk-Through/How-To
As you can see, the initial JSON value ```greeting``` has the output of ```Hello and welcome ...```, and when the user types in "tell me more", we want LevPy to output ```LevPy is a python lib ...```. So how do we actually give the outputs and listen for the inputs? Easy, just tell the LevPy.py file what to do like so: 
```python
# Change
# def Command1_(update): to
def firstVar_(update):

#and all of this
#if update != "COMMAND TO SEND USER SOMEWHERE ELSE":
#        pos = "CHANGE PLAYER POS"
#        mainLoop(update)
#    else:
#        pos = "SAME POS"
#        mainLoop(update)
#
#mainLoop ("COMMAND TO BEGIN WITH") to

if update != "tell me more":
        print("Ended Program.")
    else:
        pos = "firstVar"
        mainLoop(update)

mainLoop("greeting")
```

To make a more advanced program, say a full-fledged game, obviously you would need much more than a single function. Instead, just set multiple variable names in ```main.py```, which LevPy will interpret as different levels or rooms. In ```LevPy.py```, you must then create functions that share the names of the variables with an underscore ```_``` added afterwards. To refer from one function to another, just update the ```pos``` value. For example, if your new JSON var was called secondVar: 

```python
def firstVar_(update):
if update != "tell me more":
        pos = "secondVar"
        mainLoop(update)
    else:
        pos = "firstVar"
        mainLoop(update)

mainLoop("greeting")
```

# Contributing/Issues
Anyone is welcome to contribute to LevPy; It is fully community-funded and open-source. To do so, just create a Pull Request and add your wanted code. Any issues or bugs in the code, feel free to make a <a href="https://github.com/flancast90/LevPy/issues/new">New Issue</a>, and I will attempt to figure out what is going-on.

# License 
Apache 2.0. See https://www.apache.org/licenses/LICENSE-2.0 for more details.
