#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) [YEAR] [YOUR NAME], [YOUR EMAIL]
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
This extension deletes selected objects under a given size
"""

import inkex

class DeleteSmallPaths(inkex.EffectExtension):
    """EffectExtension to delete selected objects under a given size"""
    def add_arguments(self, pars):
        pars.add_argument("--minimumwidth", type=float, default=1.0, help="Minimum Width")
        pars.add_argument("--minimumheight", type=float, default=1.0, help="Minimum Height")

    def effect(self):
        for elem in self.svg.selection:
            if elem.bounding_box().width < self.options.minimumwidth:
                elem.delete()
            if elem.bounding_box().height < self.options.minimumheight:
                elem.delete()

if __name__ == '__main__':
    DeleteSmallPaths().run()
