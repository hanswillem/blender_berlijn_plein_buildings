'''
Searches for all objects inside an empty named 'buildings'.
It then applies a cosine function to the y position based on the x position.
'''

import bpy
import math

def draw(scene):
    obs = bpy.data.objects['buildings'].children
    for i in obs:
        xpos = i.matrix_world.translation.x
        i.location.z = i.dimensions.z * (math.cos(xpos / 10) - 1)
                    
bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(draw)
