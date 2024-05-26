import bpy
import math

# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)

# Path to the Mixamo character FBX file
fbx_path = 'path_to_your_fbx_file.fbx'

# Import the FBX file
bpy.ops.import_scene.fbx(filepath='resources/Running Jump.fbx')

# Print the names and types of all objects inside the ARMATURE object
armature = bpy.data.objects.get('Armature')
import csv

if armature:
    print("Saving Animation Data for Armature to CSV:")
    if armature.animation_data and armature.animation_data.action:
        with open('animation_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['FCurve', 'Array Index', 'Frame', 'Value'])
            for fcurve in armature.animation_data.action.fcurves:
                for keyframe_point in fcurve.keyframe_points:
                    writer.writerow([fcurve.data_path, fcurve.array_index, keyframe_point.co.x, keyframe_point.co.y])
    else:
        print("No animation data found.")
# # play animation   
# bpy.context.scene.frame_set(0)
# bpy.ops.screen.animation_play()
# bpy.ops.screen.animation_play()
  

