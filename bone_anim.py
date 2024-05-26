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


# Ensure we're in object mode and select the armature
bpy.ops.object.mode_set(mode='OBJECT')
armature = bpy.context.object
bpy.context.view_layer.objects.active = armature
bpy.ops.object.select_all(action='DESELECT')
armature.select_set(True)

# Switch to pose mode to animate bones
bpy.ops.object.mode_set(mode='POSE')

# Get the pose bones
pose_bones = armature.pose.bones

# Make sure the bone names are correct
if 'right_arm' in pose_bones:
    # Frame 1: Initial position
    bpy.context.scene.frame_set(1)
    pose_bones['right_arm'].rotation_euler[0] = 0
    pose_bones['right_arm'].keyframe_insert(data_path="rotation_euler", index=0)

    # Frame 10: Move right arm up
    bpy.context.scene.frame_set(10)
    pose_bones['right_arm'].rotation_euler[0] = 1.5  # Rotate by 1.5 radians
    pose_bones['right_arm'].keyframe_insert(data_path="rotation_euler", index=0)

    # Frame 20: Return to initial position
    bpy.context.scene.frame_set(20)
    pose_bones['right_arm'].rotation_euler[0] = 0
    pose_bones['right_arm'].keyframe_insert(data_path="rotation_euler", index=0)

    # Set animation playback range
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 20

    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Play animation
    bpy.ops.screen.animation_play()
else:
    print("Bone 'right_arm' not found. Check bone names.")

bpy.ops.screen.animation_play()  
 