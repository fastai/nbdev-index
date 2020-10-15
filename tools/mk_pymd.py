from nbdev.python_mods import *
from fastcore.all import *

def create_pymd(f):
    print(f"## All of the python 3.9 standard library\n", file=f)
    for m,n in mods.items():
        print(f"#### [{m}]({n})\n", file=f)
        print('<details>\n', file=f)
        s = syms[m]
        for o,p in s.items(): print(f"- [`{o}`]({p})", file=f)
        print('\n</details>\n', file=f)

def create_pystdlib(f):
    print(f"## All of the python 3.9 standard library\n", file=f)
    print(f"### Table of contents\n", file=f)
    for m in mods: print(f"- [{m}](#user-content-{m})", file=f)
    print(file=f)

    print(f"### Symbols by module\n", file=f)
    for m,n in mods.items():
        print(f"#### [{m}]({n})\n", file=f)
        s = syms[m]
        for o,p in s.items(): print(f"- [`{o}`]({p})", file=f)
        print('\n[^toc](#user-content-table-of-contents)\n', file=f)

with open("py.md", 'w') as f: create_pymd(f)
with open("py_stdlib.md", 'w') as f: create_pystdlib(f)
