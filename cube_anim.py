import bpy
 
# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)

bpy.ops.mesh.primitive_cube_add(size=2)
bpy.context.object.location = (1,4, 1)

# add keyframe
bpy.context.object.keyframe_insert(data_path="location", frame=0)

bpy.context.object.location = (0,0,0)

bpy.context.object.keyframe_insert(data_path="location", frame=100)

# play animation  
bpy.context.scene.frame_set(0)
bpy.ops.screen.animation_play()
