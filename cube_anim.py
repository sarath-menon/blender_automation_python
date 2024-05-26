import bpy
import math

# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)

bpy.ops.mesh.primitive_cube_add(size=2)

# set anim end frame  
bpy.context.scene.frame_end = 100

# add keyframe at frame=0
bpy.context.object.location = (1,4, 1)

bpy.context.object.rotation_euler[0] = math.radians(45)
bpy.context.object.keyframe_insert(data_path="location", frame=0)
bpy.context.object.keyframe_insert(data_path="rotation_euler", frame=0)


# add keyframe at frame=10
bpy.context.object.location = (0,0,0)
bpy.context.object.rotation_euler[0] = math.radians(90)
bpy.context.object.keyframe_insert(data_path="location", frame=100)
bpy.context.object.keyframe_insert(data_path="rotation_euler", frame=100)

# play animation   
bpy.context.scene.frame_set(0)
bpy.ops.screen.animation_play()
  