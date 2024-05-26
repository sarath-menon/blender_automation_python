import bpy
import math

# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)

bpy.ops.mesh.primitive_uv_sphere_add(radius=1)

# set anim end frame  
bpy.context.scene.frame_end = 100

# Add keyframes for a realistic bounce
frames = [0, 3, 6, 9, 12, 15]  # Time frames
heights = [0, 3, 0, 2, 0, 1]  # Corresponding heights at each frame

for frame, height in zip(frames, heights):
    bpy.context.object.location = (0, 0, height)
    bpy.context.object.keyframe_insert(data_path="location", frame=frame)

# Ensure the object is selected and active
bpy.context.view_layer.objects.active = bpy.context.object
bpy.context.object.select_set(True)

# Get the animation data of the object
animation_data = bpy.context.object.animation_data

# Check if the object has animation data and action
if animation_data and animation_data.action:
    fcurves = animation_data.action.fcurves

    # Loop through all fcurves
    for fcurve in fcurves:
        # Check if the fcurve is for the location property
        if fcurve.data_path == "location": 
            # Loop through all keyframe points
            for keyframe_point in fcurve.keyframe_points:
                # Set the interpolation type to 'BEZIER' for smoother transitions
                keyframe_point.interpolation = 'BEZIER'
                # Set handle types
                keyframe_point.handle_left_type = 'ALIGNED'
                keyframe_point.handle_right_type = 'ALIGNED' 
                # Adjust handles for more realistic bounce
                keyframe_point.handle_left.x = keyframe_point.co.x - 1
                keyframe_point.handle_left.y = keyframe_point.co.y + (0.5 if keyframe_point.co.y != 0 else 0)
                keyframe_point.handle_right.x = keyframe_point.co.x + 1
                keyframe_point.handle_right.y = keyframe_point.co.y + (0.5 if keyframe_point.co.y != 0 else 0)

# play animation      
bpy.context.scene.frame_set(0)    
bpy.ops.screen.animation_play() 
bpy.ops.screen.animation_play() 
