
#
# PS Move API - An interface for the PS Move Motion Controller
# Copyright (c) 2012 Thomas Perl <m@thp.io>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#


import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'build'))

import psmove

if psmove.count_connected() < 1:
    print('No controller connected')
    sys.exit(1)

move = psmove.PSMove()
tracker = psmove.PSMoveTracker()

while tracker.enable(move) != psmove.Tracker_CALIBRATED:
    pass

# Loop and update the controller
while True:
    tracker.update_image()
    tracker.update()

    # Check the tracking status
    status = tracker.get_status(move)
    if status == psmove.Tracker_TRACKING:
        x, y, radius = tracker.get_position(move)
        distance = tracker.distance_from_radius(radius)
        print 'Position: (%5.2f, %5.2f), Distance: %3.2fcm' % (x, y, distance)
    else:
        print 'Not currently tracking.'

