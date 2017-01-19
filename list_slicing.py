# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:00:11 2017

@author: Diptark Bose
"""

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
intermediate=garbled[::-1]
message=intermediate[::2]
print message