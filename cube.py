import bpy
 
D = bpy.data
C = bpy.context

bpy.ops.mesh.primitive_cube_add(size=2)
bpy.context.object.location = (1, 2, 5)

