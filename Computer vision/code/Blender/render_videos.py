import bpy


scn = bpy.data.scenes["Scene"]
scn.frame_start = 1
scn.frame_end = 60

kf = [1, 17, 40, 60]



for obj in bpy.data.objects:
    obj.select = False

obj = bpy.data.objects['Sphere']
obj.select = True
bpy.context.scene.objects.active = obj
obj.animation_data_clear()

obj.location = (2,0,0.25)
bpy.context.scene.frame_set(kf[0])
obj.keyframe_insert(data_path='location')

bpy.context.scene.frame_set(kf[1])
bpy.ops.transform.translate(value=(-3, 0, 0))
obj.keyframe_insert(data_path='location')


bpy.context.scene.frame_set(kf[2])
bpy.ops.transform.translate(value=(0, 2, 0))
obj.keyframe_insert(data_path='location')


bpy.context.scene.frame_set(kf[3])
bpy.ops.transform.translate(value=(3, -4, 0))
obj.keyframe_insert(data_path='location')



scn.render.filepath = "//../Work/cam1.avi"
scn.camera = bpy.data.objects["Camera_1"]
bpy.ops.render.render(animation=True)

scn.render.filepath = "//../Work/cam2.avi"
scn.camera = bpy.data.objects["Camera_2"]
bpy.ops.render.render(animation=True)
