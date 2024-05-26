import bpy

def switch_to_2d_animation_workspace():
    # Switch to the 2D Animation workspace
    workspace_name = '2D Animation'
    if workspace_name in bpy.data.workspaces:
        bpy.context.window.workspace = bpy.data.workspaces[workspace_name]
    else:
        print(f"The workspace '{workspace_name}' does not exist.")

def create_grease_pencil_object():
    # Create a new grease pencil object if it doesn't exist
    if "GPencil" not in bpy.data.objects:
        bpy.ops.object.gpencil_add(location=(0, 0, 0))
    gpencil = bpy.data.objects["GPencil"]
    return gpencil

def create_grease_pencil_layer(gpencil):
    # Create a new layer if it doesn't exist
    if "GPlayer" not in gpencil.data.layers:
        gpencil.data.layers.new(name="GPlayer", set_active=True)
    layer = gpencil.data.layers["GPlayer"]
    return layer


def create_grease_pencil_frame(layer):
    # Create a new frame if it doesn't exist
    if not layer.frames:
        frame = layer.frames.new(0)
    else:
        frame = layer.frames[0]
    return frame

def switch_view(type):
    if type == 'FRONT':
        bpy.ops.view3d.view_axis(type='FRONT')
    elif type == 'BACK':
        bpy.ops.view3d.view_axis(type='BACK')
    elif type == 'TOP':
        bpy.ops.view3d.view_axis(type='TOP')
    elif type == 'BOTTOM':
        bpy.ops.view3d.view_axis(type='BOTTOM')
    elif type == 'LEFT':
        bpy.ops.view3d.view_axis(type='LEFT')
    elif type == 'RIGHT':
        bpy.ops.view3d.view_axis(type='RIGHT')
    else:
        print(f"Invalid view type: {type}")

def create_2d_animation_workspace():
    # Create a new 2D Animation workspace
    workspace_name = '2D Animation'
    if workspace_name not in bpy.data.workspaces:
        bpy.data.workspaces.add(name=workspace_name)
    bpy.context.window.workspace = bpy.data.workspaces[workspace_name]

create_2d_animation_workspace()

switch_to_2d_animation_workspace()

gpencil = create_grease_pencil_object()



# Ensure we're in draw mode
bpy.ops.object.mode_set(mode='PAINT_GPENCIL')



layer = create_grease_pencil_layer(gpencil)

frame = create_grease_pencil_frame(layer)


switch_view('FRONT')

# Create a new stroke
stroke = frame.strokes.new()
stroke.display_mode = '3DSPACE'  # Set the stroke to 3D space

# Define stroke geometry
stroke.points.add(count=2)
stroke.points[0].co = (0, 0, 0)
stroke.points[1].co = (2, 2, 2)

# Return to object mode
bpy.ops.object.mode_set(mode='OBJECT')


