import bpy
import math

# delete all objects in the current scene
for obj in bpy.context.scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)

# Add a basic symmetrical bone character with a face, 2 arms, and 2 legs in a T pose
bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))
armature = bpy.context.object

if "Bone" in armature.data.edit_bones:
    armature.data.edit_bones.remove(armature.data.edit_bones["Bone"])

# Define bone positions
bone_data = [
    ("spine", (0, 0, 1), (0, 0, 2)),  # Adjusted spine to start from height 1
    ("left_arm", (0, 0, 2), (-1, 0, 2)),  # Adjusted arm positions for new spine height
    ("right_arm", (0, 0, 2), (1, 0, 2)),  # Adjusted arm positions for new spine height
    ("left_leg", (0, 0, 1), (-0.5, 0, 0)),  # Adjusted leg positions to make feet at height zero
    ("right_leg", (0, 0, 1), (0.5, 0, 0))  # Adjusted leg positions to make feet at height zero
]

# Create bones
for bone_name, head_pos, tail_pos in bone_data:
    bone = armature.data.edit_bones.new(bone_name)
    bone.head = head_pos
    bone.tail = tail_pos
    if bone_name in ["left_arm", "right_arm", "left_leg", "right_leg"]:
        bone.parent = armature.data.edit_bones["spine"]

# Add a spherical head just above the neck
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(0, 0.3, 0.0))
head = bpy.context.object
head.parent = armature
head.parent_type = 'BONE'
head.parent_bone = 'spine'

# Exit edit mode to save bones and head
bpy.ops.object.mode_set(mode='OBJECT')

