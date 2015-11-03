bl_info = {
    "name": "Move X Axis",
    "category": "Object",
}

import bpy


class ObjectMoveX(bpy.types.Operator):
    """My Object Moving Script"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.move_x"        # unique identifier for buttons and menu items to reference.
    bl_label = "Move X by One"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        return {'FINISHED'}            # this lets blender know the operator finished successfully.


class OBJECT_PT_pingpong(bpy.types.Panel):
    bl_label = "Ping Pong"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Create"
    bl_context = "objectmode"

    is_left = True

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="PHYSICS")

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        split = row.split(percentage=0.5)
        col_left = split.column()
        col_right = split.column()

        if self.is_left:
            col_left.operator("object.pingpong", text="Ping")
        else:
            col_right.operator("object.pingpong", text="Pong")


class OBJECT_OT_pingpong(bpy.types.Operator):
    bl_label = "Ping Pong Operator"
    bl_idname = "object.pingpong"
    bl_description = "Move the ball"

    def execute(self, context):
        OBJECT_PT_pingpong.is_left = not OBJECT_PT_pingpong.is_left
        self.report({'INFO'}, "Moving the ball")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ObjectMoveX)
    bpy.utils.register_class(OBJECT_OT_pingpong)
    bpy.utils.register_class(OBJECT_PT_pingpong)


def unregister():
    bpy.utils.unregister_class(ObjectMoveX)
    bpy.utils.unregister_class(OBJECT_OT_pingpong)
    bpy.utils.unregister_class(OBJECT_PT_pingpong)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()