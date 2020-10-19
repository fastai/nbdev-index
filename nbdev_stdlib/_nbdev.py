__all__ = ['NbdevLookup', 'modidx']
from . import _modidx
modidx = _modidx.d

class NbdevLookup():
    def __init__(self):
        py_syms = {k:v for k_,v_ in modidx['syms'].items() for k,v in v_.items()}
        self.syms = {**py_syms, **m['mods']}

    def doc_link(self, s): return self.syms.get(s, None)
