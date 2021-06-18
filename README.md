# LevPy
> Text-based games made easy!

# About 
LevPy is a simple python file/function that allows the creation of text-based games easily through JSON data. For example, in ```main.py```, you could include the following "level": 
```python
firstVar = '{"greeting":"Hello and welcome to LevPy! Type \"tell me more\" to learn more","tell me more":"LevPy is a python library that makes making games easy!"}'
```
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
#mainLoop("COMMAND TO BEGIN WITH") to

if update != "tell me more":
        pos = "CHANGE PLAYER POS"
        mainLoop(update)
    else:
        pos = "SAME POS"
        mainLoop(update)

mainLoop("greeting")
```

Documentation isn't done, please hold on.
