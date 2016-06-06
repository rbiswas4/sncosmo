# Licensed under a 3-clause BSD style license - see LICENSES
from __future__ import print_function

from os.path import join, dirname

import sncosmo


def test_read_snana_ascii():
    fname = join(dirname(__file__), "data", "snana_ascii_example.dat")
    meta, tables = sncosmo.read_snana_ascii(fname, default_tablename="OBS")

    # only 1 table
    assert len(tables) == 1
    data = tables["OBS"]

    assert len(data) == 4  # 4 rows.
    assert len(data.colnames) == 13  # 13 columns.


def test_read_snana_fits():
    fname1 = join(dirname(__file__), "data", "snana_fits_example_head.fits")
    fname2 = join(dirname(__file__), "data", "snana_fits_example_phot.fits")
    sne = sncosmo.read_snana_fits(fname1, fname2)
    assert len(sne) == 2

def test_read_snana_fits_byn():
    fname1 = join(dirname(__file__), "data", "snana_fits_example_head.fits")
    fname2 = join(dirname(__file__), "data", "snana_fits_example_phot.fits")
    sne = sncosmo.read_snana_fits(fname1, fname2, n=1)
    assert len(sne['flux']) == 48
    assert len(sne) == 1
    assert len(sne[0]) == 48

def test_read_snana_simlib():
    fname = join(dirname(__file__), "data", "snana_simlib_example.dat")
    meta, obs_sets = sncosmo.read_snana_simlib(fname)
    assert len(obs_sets) == 2


def test_read_snana_simlib_noend():
    fname = join(dirname(__file__), "data", "snana_simlib_example_noend.dat")
    meta, obs_sets = sncosmo.read_snana_simlib(fname)
    assert len(obs_sets) == 2
