# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#

"""
This has been copied from the main clause of the models module

.. moduleauthor:: Marmaduke Woodman <mw@eml.cc>
"""

raise ImportError('module needs to be rewritten')


if __name__ == "__main__":
    # Do some stuff that tests or makes use of this module...
    LOG.info("Testing %s module..." % __file__)
    # Check that the docstring examples, if there are any, are accurate.
    import doctest
    doctest.testmod()

    #Initialise Models in their default state:
    WILSON_COWAN_MODEL = WilsonCowan()
    REDUCED_SET_FITZHUGH_NAGUMO_MODEL = ReducedSetFitzHughNagumo()
    REDUCED_SET_HINDMARSH_ROSE_MODEL = ReducedSetHindmarshRose()
    JANSEN_RIT_MODEL = JansenRit()
    GENERIC_2D_MODEL = Generic2dOscillator()
    BRUNEL_WANG_MODEL = BrunelWang()
    WONG_WANG_MODEL = WongWang()


    LOG.info("All Models initialised in their default state without error...")
