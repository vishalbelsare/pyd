import pyd.support
from pyd.support import setup, Extension, pydexe_sanity_check

pydexe_sanity_check()
projName = 'struct_wrap'
ext_modules = setup(
    name=projName,
    version='1.0',
    ext_modules=[
        Extension("struct_wrap", ["struct_wrap.d"],
            d_unittest=True,
            build_deimos=True,
            d_lump=True,
        )
    ],
)
