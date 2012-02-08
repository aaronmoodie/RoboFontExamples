import vanilla
import mojo

class ObjectBrowserController():

        def __init__(self, inspectObject):

            if inspectObject is None:
                raise TypeError, "can not inspect None value"

            self.w = vanilla.Window((400, 400),
                                   "inspect %s" %inspectObject,
                                   minSize=(100, 100))
            self.w.b = vanilla.ObjectBrowser((0, 0, -0, -0),
                                   inspectObject)
            self.w.open()


#obj = vanilla
#obj = mojo
obj = CurrentFont()

ObjectBrowserController(obj)