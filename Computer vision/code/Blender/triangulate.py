import bpy
import sys
sys.path.insert(0, '/home/mshpakovych/Work/Projects/facerec/syntetic_data')
import numpy as np
from camera_matrix import get_3x4_P_matrix_from_blender, project_by_object_utils
from mathutils import Matrix, Vector


cam1 = bpy.data.objects["Camera_1"]
cam2 = bpy.data.objects["Camera_2"]

C1 = get_3x4_P_matrix_from_blender(cam1)[0]
C2 = get_3x4_P_matrix_from_blender(cam2)[0]

np.save('/home/mshpakovych/Work/Projects/facerec/syntetic_data/C1', np.array(C1))
np.save('/home/mshpakovych/Work/Projects/facerec/syntetic_data/C2', np.array(C2))


p1_2d = project_by_object_utils(cam1, Vector([2.0, -2.0, 0.25]))
p2_2d = project_by_object_utils(cam2, Vector([2.0, -2.0, 0.25]))
