

# Copyright (c) 2013 Johan Ceuppens.
# All rights reserved.

# Redistribution and use in source and binary forms are permitted
# provided that the above copyright notice and this paragraph are
# duplicated in all such forms and that any documentation,
# advertising materials, and other materials related to such
# distribution and use acknowledge that the software was developed
# by the Johan Ceuppens.  The name of the
# Johan Ceuppens may not be used to endorse or promote products derived
# from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *

class Heart:
	def __init__(self):
        	self.image = pygame.image.load('./pics/heart.bmp').convert()
        	self.image.set_colorkey((0,0,0))
        	#self.imagemax = pygame.image.load('./pics/life1.bmp').convert()
        	#self.imagemax.set_colorkey((0,0,0))
		

class Meter:
    "life or mana meter"
    def __init__(self):
	self.max = 50 
	self.index = 50
	self.hearts = []
	for i in range(0,3):
		self.hearts.append(Heart())
 
    def draw(self,screen):
	# KLUDGY
	j = 0
	###for i in range(0,self.index/10):
	for i in range(0,self.index):
        	screen.blit(self.hearts[0].image, (17+j*12, 26))
		j += 1
