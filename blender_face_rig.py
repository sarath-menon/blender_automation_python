import bpy
import math

# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)


# Open the specified .blend file
bpy.ops.wm.open_mainfile(filepath='resources/sprite_rig.blend', use_scripts=False)

# Print all objects in the scene after opening the .blend file
print("Scene Contents:")
for obj in bpy.data.objects:
    print(f"Object: {obj.name}, Type: {obj.type}")



# # play animation   
# bpy.context.scene.frame_set(0)
# bpy.ops.screen.animation_play()
