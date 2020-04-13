#!/usr/bin/env python3
# encoding: utf-9

import os
from distutils.core import setup, Extension

strCompilerCommonFlagsSuffix = " -fpermissive -fPIC -std=c++11 -Wno-error=parentheses -Wno-error=char-subscripts"
os.environ["CC" ] = "gcc-9" + strCompilerCommonFlagsSuffix
os.environ["CXX"] = "g++-9" + strCompilerCommonFlagsSuffix
os.environ["LD" ] = "ld" + strCompilerCommonFlagsSuffix

dkgpython_module = Extension('dkgpython',
                             sources = ['dkgpython.cpp'],
                             include_dirs = ['..', '../bls', '../dkg', '../third_party', '../deps/',
                             '../deps/deps_inst/x86_or_x64/include',
                             '../deps/deps_inst/x86_or_x64/include/libff'],

                             library_dirs = ['../build', '../deps/deps_inst/x86_or_x64/lib',
                             '../deps/deps_inst/x86_or_x64/lib/libff'],

                             libraries = ['bls', 'ff', 'gmpxx', 'gmp']
                             )

setup(name = 'dkgpython',
      version = '0.1.0',
      description = 'dkgpython module written in C++',
      ext_modules = [dkgpython_module]
      )
