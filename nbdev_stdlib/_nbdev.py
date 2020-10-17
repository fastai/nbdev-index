__all__ = ['NbdevLookup']

from .module_idx import *

class NbdevLookup():
    def __init__(self):
        py_syms = {k:v for k_,v_ in syms.items() for k,v in v_.items()}
        self.syms = {**py_syms, **mods}

    def doc_link(self, s): return self.syms.get(s, None)
