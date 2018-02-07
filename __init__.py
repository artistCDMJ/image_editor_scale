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
           "version": (1, 00),
           "blender": (2, 79, 0),
           "location": "Image Editor > UI > Image Resize",
           "description": "Image Resize for Active Image",
           "warning": "WIP Test version for later addition to EZ Paint",
           "wiki_url": "",
           "category": "Image"}





import bpy
from bpy.props import *
#image.size[0]= width
#image.size[1]=height



def initSceneProperties(scn):
    
    for area in bpy.context.screen.areas :
        if area.type == 'IMAGE_EDITOR' :
            my_img = area.spaces.active.image
            area.spaces.active.image = my_img
    
    
    bpy.types.Scene.MyIntX = IntProperty(
        name = "Scale X", 
        description = "Enter an integer")
    scn['MyIntX'] = my_img.size[0]
    #bpy.types.Scene.MyIntX = IntProperty(default=1024)
    bpy.types.Scene.MyIntY = IntProperty(
        name = "Scale Y", 
        description = "Enter an integer")
    scn['MyIntY'] = my_img.size[1]
    #bpy.types.Scene.MyIntY = IntProperty(default=1024)
    
    return


initSceneProperties(bpy.context.scene)



class ResizeOper(bpy.types.Operator):
    """Resize Operator"""
    bl_idname = "object.resize_operator" 
     
    bl_label = "Resize Active Image"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):  

        for area in bpy.context.screen.areas :
            if area.type == 'IMAGE_EDITOR' :
                my_img = area.spaces.active.image
                area.spaces.active.image = my_img
                
                my_img.scale(context.scene.MyIntX,context.scene.MyIntY)
                
        return {'FINISHED'}

class GetsizeOper(bpy.types.Operator):
    """Get Size Operator"""
    bl_idname = "object.getsize_operator" 
     
    bl_label = "Get Size of Active Image"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):  

        for area in bpy.context.screen.areas :
            if area.type == 'IMAGE_EDITOR' :
                my_img = area.spaces.active.image
                area.spaces.active.image = my_img
                
                bpy.context.scene['MyIntX'] = my_img.size[0]
                bpy.context.scene['MyIntY'] = my_img.size[1]
                
        return {'FINISHED'}



class ImageScalePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Image Scale"
    bl_idname = "OBJECT_PT_imagescale"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
   
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        image = bpy.context.space_data.image

        row = layout.row()
        row.label(text="", icon='WORLD_DATA')

        #row = layout.row()
        row.label(text="Active image is:")
        row = layout.row()
        row.prop(image, "name")
        row = layout.row()
        row.operator("object.getsize_operator", text="GET SIZE")
        row.operator("object.resize_operator", text="RESIZE")
        row = layout.row()
        row.prop(scn, 'MyIntX', icon='BLENDER', toggle=True)
        row = layout.row()
        row.prop(scn, 'MyIntY', icon='BLENDER', toggle=True)
        
        

        #row = layout.row()
        #row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(ImageScalePanel)
    bpy.utils.register_class(GetsizeOper)
    bpy.utils.register_class(ResizeOper)


def unregister():
    bpy.utils.unregister_class(ImageScalePanel)
    bpy.utils.unregister_class(GetsizeOper)
    bpy.utils.unregister_class(ResizeOper)

if __name__ == "__main__":
    register()
