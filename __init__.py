# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>


bl_info = {"name": "Image Resize",
           "author": "CDMJ",
           "version": (1, 1, 0),
           "blender": (2, 79, 0),
           "location": "Image Editor > UI > Image Resize",
           "description": "Image Resize for Active Image",
           "warning": "WIP Test version for later addition to EZ Paint",
           "wiki_url": "",
           "category": "Image"}

import bpy
from bpy.props import *
from bpy.types import Panel


##################################################################### Properties
def getWidth(self):
    for area in bpy.context.screen.areas :
        if area.type == 'IMAGE_EDITOR' :
            my_img = area.spaces.active.image

            if my_img != None and my_img.name != "Render Result":
                return my_img.size[0]

def getHight(self):
    for area in bpy.context.screen.areas :
        if area.type == 'IMAGE_EDITOR' :
            my_img = area.spaces.active.image

            if my_img != None and my_img.name != "Render Result":
                return my_img.size[1]


def setWidth(self, value):
    scn = bpy.context.scene
    for area in bpy.context.screen.areas :
        if area.type == 'IMAGE_EDITOR' :
            my_img = area.spaces.active.image
            if my_img != None and my_img.name != "Render Result":
                my_img.scale(value, scn.MyIntY)
    return None

def setHight(self, value):
    scn = bpy.context.scene
    for area in bpy.context.screen.areas :
        if area.type == 'IMAGE_EDITOR' :
            my_img = area.spaces.active.image
            if my_img != None and my_img.name != "Render Result":
                my_img.scale(scn.MyIntX, value)
    return None


def updateArea(self,context):

    for area in context.screen.areas :
        if area.type == 'IMAGE_EDITOR' :
            my_img = area.spaces.active.image
            if my_img != None and my_img.name != "Render Result":
                my_img.save()


bpy.types.Scene.MyIntX = bpy.props.IntProperty(name="Width", default=0, min=0, update=updateArea,  get=getWidth, set=setWidth )
bpy.types.Scene.MyIntY = bpy.props.IntProperty(name="Height", default=0, min=0, update=updateArea,  get=getHight, set=setHight )



def image_panel(self, context):
    scn = context.scene
    image = context.space_data.image

    layout = self.layout
    row = layout.row()
    if image != None and image.name != "Render Result":
        #row.label(text = str(image.name), icon='IMAGE_DATA')
        col = layout.column(align=True)
        col.prop(scn, "MyIntX")
        col.prop(scn, "MyIntY")
    elif image != None and image.name == "Render Result":
        rd = scn.render

        sub = row.column(align=True)
        sub.label(text="Resolution:")
        sub.prop(rd, "resolution_x", text="X")
        sub.prop(rd, "resolution_y", text="Y")
        sub.prop(rd, "resolution_percentage", text="")
    else:
        row.label(text="No Active Image", icon='ERROR')



####################################################################### REGISTER
def register():
    bpy.types.IMAGE_PT_image_properties.prepend(image_panel)


def unregister():
    bpy.types.IMAGE_PT_image_properties.remove(image_panel)


if __name__ == "__main__":
    register()
