import bpy
import math

# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)

bpy.ops.mesh.primitive_uv_sphere_add(radius=1)

# set anim end frame  
bpy.context.scene.frame_end = 100

# add keyframe at frame=0
frame = 0
bpy.context.object.location = (0,0,0)
bpy.context.object.keyframe_insert(data_path="location", frame=frame)

# add keyframe at frame=3
frame = 3
bpy.context.object.location = (0,0,3)
bpy.context.object.keyframe_insert(data_path="location", frame=frame)


# add keyframe at frame=3
frame = 6
bpy.context.object.location = (0,0,0)
bpy.context.object.keyframe_insert(data_path="location", frame=frame)

# play animation   
bpy.context.scene.frame_set(0)
bpy.ops.screen.animation_play()
  