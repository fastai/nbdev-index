__all__ = ['NbdevLookup']

from nbdev import python_mods

class NbdevLookup():
    def __init__(self):
        py_syms = {k:v for k_,v_ in python_mods.syms.items() for k,v in v_.items()}
        self.syms = {**py_syms, **python_mods.mods}

    def doc_link(self, s): return self.syms.get(s, None)

