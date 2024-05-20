from __future__ import print_function

import sys

if sys.version_info[0] < 3:
    print(u"Hello World! Pass this test, please.")
else:
    print("Hello World! Pass this test, please.")

