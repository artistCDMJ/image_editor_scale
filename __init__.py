import bpy
from bpy.props import *


def initSceneProperties(scn):
    bpy.types.Scene.MyIntX = IntProperty(
        name = "Scale X", 
        description = "Enter an integer")
    scn['MyIntX'] = 1024

    bpy.types.Scene.MyIntY = IntProperty(
        name = "Scale Y", 
        description = "Enter an integer")
    scn['MyIntY'] = 1024
    return

initSceneProperties(bpy.context.scene)


class GenericOper(bpy.types.Operator):
    """Generic Operator"""
    bl_idname = "object.generic_operator" 
                                     
     
    bl_label = "Generic Operator Template"
    bl_options = { 'REGISTER', 'UNDO' }
    
    
    
    def execute(self, context):        
        
        
        
        for area in bpy.context.screen.areas :
            if area.type == 'IMAGE_EDITOR' :
                my_img = area.spaces.active.image
                area.spaces.active.image = my_img
                prop('MyIntX', scn)
                prop('MyIntY', scn)
                my_img.scale(MyIntX,MyIntY)
        
        return {'FINISHED'}




class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Image Scale"
    bl_idname = "OBJECT_PT_imagescale"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    #bl_context = "object"

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        image = bpy.context.space_data.image

        row = layout.row()
        row.label(text="Image Scale Test Panel", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active image is: " + image.name)
        row = layout.row()
        row.prop(image, "name")
        row = layout.row()
        row.operator("object.generic_operator", text="scale it")
        row = layout.row()
        row.prop(scn, 'MyIntX', icon='BLENDER', toggle=True)
        row = layout.row()
        row.prop(scn, 'MyIntY', icon='BLENDER', toggle=True)
        
        

        #row = layout.row()
        #row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(HelloWorldPanel)
    
    bpy.utils.register_class(GenericOper)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    
    bpy.utils.unregister_class(GenericOper)

if __name__ == "__main__":
    register()
