#####################################################################
#                                                                   #
# /PulseblasterESRpro500.py                                         #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of labscript_devices, in the labscript suite    #
# (see http://labscriptsuite.org), and is licensed under the        #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
from __future__ import division, unicode_literals, print_function, absolute_import
from labscript_utils import PY2
if PY2:
    str = unicode

from labscript_devices import labscript_device, BLACS_tab, BLACS_worker, runviewer_parser
from labscript_devices.PulseBlaster_No_DDS import PulseBlaster_No_DDS, Pulseblaster_No_DDS_Tab, PulseblasterNoDDSWorker


@labscript_device
class PulseBlasterESRPro200(PulseBlaster_No_DDS):
    description = 'SpinCore PulseBlaster ESR-PRO-200'
    clock_limit = 200.0e6
    clock_resolution = 5e-9
    n_flags = 21


@BLACS_tab    
class pulseblasteresrpro200(Pulseblaster_No_DDS_Tab):
    # Capabilities
    num_DO = 21
    def __init__(self,*args,**kwargs):
        self.device_worker_class = PulseblasterESRPro200Worker 
        Pulseblaster_No_DDS_Tab.__init__(self,*args,**kwargs)
    
    
@BLACS_worker
class PulseblasterESRPro200Worker(PulseblasterNoDDSWorker):
    core_clock_freq = 200.0
    
     
