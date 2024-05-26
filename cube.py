import bpy
 
# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)


bpy.ops.mesh.primitive_cube_add(size=2)
bpy.context.object.location = (1,4, 1)

