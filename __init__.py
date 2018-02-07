import bpy

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
                
                my_img.scale(2048,2048)
        
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

        image = bpy.context.space_data.image

        row = layout.row()
        row.label(text="Image Scale Test Panel", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active image is: " + image.name)
        row = layout.row()
        row.prop(image, "name")
        row = layout.row()
        row.operator("object.generic_operator", text="scale it")
        
        

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
