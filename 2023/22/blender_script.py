import bpy
import uuid
import random


INPUT_FILE = "D:\\Code\\advent-of-code\\advent-of-code\\2023\\22\\input.txt"

mat_dict = {}

def brick_sort_bottom(b):
    return b["Z"][0]

def brick_sort_top(b):
    return b["Z"][1]

def interval_overlap(interval1, interval2):
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return False
    return True


def grant_gift_of_color(id):
    mat = bpy.data.materials.new(id)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (random.random()/2, random.random()/2, random.random()/2, 1)
    mat_dict[id] = mat
    return mat

def coat_thyself_in_sanguinary_hues_of_terror(id):
    mat = bpy.data.materials.new(id)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (0.75+random.random()/4, random.random()/4, 0, 1)
    mat_dict[id] = mat
    return mat

def thine_armored_shell_shalt_be_hued_azure_sky(id):
    mat = bpy.data.materials.new(id)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (0, random.random()/2, 0.75+random.random()/4, 1)
    mat_dict[id] = mat
    return mat


bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

for material in bpy.data.materials:
    # Remove the material
    bpy.data.materials.remove(material)

bricks = []
with open(INPUT_FILE, "r") as file:
    lines = list(file)
    id = 0
    for line in lines:
        
        uid = str(uuid.uuid4())
        
        line = line.rstrip("\n")
        coords = line.split("~")
        c1 = coords[0].split(",")
        c2 = coords[1].split(",")
        brick = {}
        brick["UUID"] = uid
        brick["Start"] = tuple(c1)
        brick["End"] = tuple(c2)
        brick["ID"] = id
        brick["X"] = (int(c1[0]), int(c2[0]))
        brick["Y"] = (int(c1[1]), int(c2[1]))
        brick["Z"] = (int(c1[2]), int(c2[2]))
        bricks.append(brick)
        id += 1
        
bricks.sort(key = brick_sort_bottom)


stable_bricks = []
stable_brick_map = {}
z_head_map = {}
z_butt_map = {}


for b in range(len(bricks)):
    brick = bricks[b]
#starting with the lowest brick, go toward the ground checking for collisions

    #try to lower the current brick checking for collisions with any bricks beneath it, working through them top to bottom
    fall_distance = brick["Z"][0] - 1
    for s in list(reversed(stable_bricks)):
        if interval_overlap(brick["X"], s["X"]) and interval_overlap(brick["Y"], s["Y"]):
            #set brick height to be 1 higher than the stable brick it has collided with
            fall_distance = brick["Z"][0] - (s["Z"][1] + 1)
            break

    butt = brick["Z"][0] - fall_distance
    head = brick["Z"][1] - fall_distance
    z_height = (butt, head)
    
    s = (brick["X"][0], brick["Y"][0], butt)
    e = (brick["X"][1], brick["Y"][1], head)
    
    stable_brick = {"Start":s , "End":e, "UUID": brick["UUID"], "ID": brick["ID"], "X": brick["X"], "Y": brick["Y"], "Z":z_height}

    stable_bricks.append(stable_brick)
    stable_bricks.sort(key = brick_sort_top)
    stable_brick_map[brick["ID"]] = stable_brick

    if butt not in z_butt_map.keys():
        z_butt_map[butt] = []
    z_butt_map[butt].append(stable_brick["ID"])

    if head not in z_head_map.keys():
        z_head_map[head] = []
    z_head_map[head].append(stable_brick["ID"])


for s in stable_bricks:
    above = []
    below = []
    butt = s["Z"][0]
    head = s["Z"][1]

    head_check = butt - 1
    butt_check = head + 1

    if head_check in z_head_map.keys():
        for brick_key in z_head_map[head_check]:
            below_brick = stable_brick_map[brick_key]
            if interval_overlap(s["X"], below_brick["X"]) and interval_overlap(s["Y"], below_brick["Y"]):
                below.append(brick_key)

    if butt_check in z_butt_map.keys():
        for brick_key in z_butt_map[butt_check]:
            above_brick = stable_brick_map[brick_key]
            if interval_overlap(s["X"], above_brick["X"]) and interval_overlap(s["Y"], above_brick["Y"]):
                above.append(brick_key)
    
    s["below"] = below
    s["above"] = above
    

for s in stable_bricks:
    safe_brick = True
    for a in s["above"]:
        above_brick = stable_bricks[a]
        if len(above_brick["below"]) < 2:
            safe_brick = False
            break
    if safe_brick:
        s["color"] = "blue"
    else:
        s["color"] = "red"


i = 0
for b in stable_bricks:
    i+= 1
    if i %100 == 0:
        print(i)
    # Add a cube
    offset = (int(b["Start"][0])+0.5, int(b["Start"][1])+0.5, int(b["Start"][2])+0.5)
    bpy.ops.mesh.primitive_cube_add(location= offset, size=1)
    cube = bpy.context.active_object
    # Switch to Edit Mode
    bpy.ops.object.mode_set(mode='EDIT')
    # Make sure that the mesh is in face select mode
    bpy.context.tool_settings.mesh_select_mode = (False, False, True)
    # Deselect all faces
    bpy.ops.mesh.select_all(action='DESELECT')
    # Switch to Object Mode to make the selection take effect
    bpy.ops.object.mode_set(mode='OBJECT')
    # Select a specific face (for example, the top face)
    # Cube faces are indexed from 0 to 5, let's select face index 4 (which is typically the top face)
    #0:left
    #1:back
    #2:right
    #3:front
    #4:bottom
    #5:top
    cube.data.polygons[2].select = True
    # Switch back to Edit Mode
    bpy.ops.object.mode_set(mode='EDIT')
    # Extrude the selected face
    stretch1 = int(b["End"][0]) - int(b["Start"][0])
    stretch2 = int(b["End"][1]) - int(b["Start"][1])
    stretch3 = int(b["End"][2]) - int(b["Start"][2])
    
    bpy.ops.mesh.extrude_region_move(
        TRANSFORM_OT_translate={"value":(stretch1, 0, 0)}  # This moves the extruded face along the Z-axis by 1 unit
    )
    
    
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    cube.data.polygons[1].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.extrude_region_move(
        TRANSFORM_OT_translate={"value":(0, stretch2, 0)}  # This moves the extruded face along the Z-axis by 1 unit
    )
    
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    cube.data.polygons[5].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.extrude_region_move(
        TRANSFORM_OT_translate={"value":(0,0,stretch3)}  # This moves the extruded face along the Z-axis by 1 unit
    )
    
    # Return to Object Mode
    bpy.ops.object.mode_set(mode='OBJECT')

    if b["color"] == "red":
        new_mat = coat_thyself_in_sanguinary_hues_of_terror(b["UUID"])
    
    elif b["color"] == "blue":
        new_mat = thine_armored_shell_shalt_be_hued_azure_sky(b["UUID"])
        
    cube.data.materials.append(new_mat)