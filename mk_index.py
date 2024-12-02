#!/usr/bin/env python

from pprint import pprint
from io import BytesIO
from sphinx.util.inventory import InventoryFile
from urllib.parse import urljoin
from collections import defaultdict
from pathlib import Path
from nbdev.doclinks import create_index
from fastcore.all import *

mappings = dict(
    stdlib='https://docs.python.org/3',

    numpy='https://numpy.org/doc/stable',
    scipy='https://docs.scipy.org/doc/scipy/reference',
    sympy='https://docs.sympy.org/latest',
    matplotlib='https://matplotlib.org',
    pandas='https://pandas.pydata.org/docs',
    h5py='https://docs.h5py.org/en/latest',
    pandasdatareader='https://pandas-datareader.readthedocs.io/en/latest',
    # https://github.com/scikit-learn-contrib/sklearn-pandas
    # https://github.com/astanin/python-tabulate
    # https://github.com/Kaggle/docker-python
    altair='https://altair-viz.github.io',
    pytorch='https://pytorch.org/docs/stable',
    cudf='https://docs.rapids.ai/api/cudf/stable',
    # https://github.com/pola-rs/polars-book#status-of-the-code-snippets
    arrow='https://arrow.apache.org/docs',
    dask='https://docs.dask.org/en/stable',
    daskml='https://ml.dask.org',
    daskdistributed='https://distributed.dask.org/en/stable',
    # daskjobqueue='https://jobqueue.dask.org/en/latest'
    # daskcloudprovider='https://cloudprovider.dask.org/en/latest',
    sklearn='https://scikit-learn.org/stable',
    yellowbrick='https://www.scikit-yb.org/en/latest',
    featuretools='https://featuretools.alteryx.com/en/stable',
    
    sphinx='https://www.sphinx-doc.org/en/stable',
    attrs='https://www.attrs.org/en/stable',
    sarge='https://sarge.readthedocs.io/en/latest',
    django='https://django.readthedocs.org/en/latest',
    jinja2='https://jinja.readthedocs.org/en/latest',
    pytest='https://docs.pytest.org/en/stable',
    
    linux='https://docs.kernel.org/',
)

class SphinxIndex:
    def __init__(self, url, pre=None):
        if pre is None: pre=url+"/"
        invs = urlread(f'{url}/objects.inv', decode=False)
        self.idx = InventoryFile.load(stream=BytesIO(invs), uri=pre, joinfunc=urljoin)
        typs = 'module','class','method','function'
        self.d = {o:self._get(o) for o in typs}
        self.syms = defaultdict(dict)
        for o in typs:
            for k,v in self.d[o].items():
                modparts = k.split(".")[:-2 if o=='method' else -1]
                if modparts: self.syms['.'.join(modparts)][k] = v

    def _get(self, o): return {k:v[2] for k,v in self.idx[f'py:{o}'].items() if k[0]!='_'}

@call_parse
def make_index(
    nm: str # Name of library to index
):
    "Make index for `nm`"
    url = mappings.get(nm)
    print(nm, url)
    if not url: return
#     idx = SphinxIndex(url)
    syms = create_index(url)
    lib_path = Path(f"nbdev_{nm}")
    lib_path.mkdir(exist_ok=True)
    with (lib_path/'_modidx.py').open('w') as f:
        f.write("# Autogenerated by get_module_idx.py\n\nd = ")
        d = dict(syms=dict(syms), settings={'lib_path':lib_path.name})
        pprint(d, f, width=160, indent=2, compact=True)
