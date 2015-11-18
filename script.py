
import os, sys
 
def module_path():
    if hasattr(sys, "wxPython"):
        return os.path.dirname(
            unicode(sys.executable, sys.getfilesystemencoding( ))
        )
    return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))

print module_path()
