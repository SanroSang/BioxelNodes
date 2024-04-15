import bpy
from .convert import ConvertToMesh
from .io import ExportVDB, ImportDICOM


def TOPBAR_FILE_IMPORT(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(ImportDICOM.bl_idname)


def TOPBAR_FILE_EXPORT(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(ExportVDB.bl_idname)


def VIEW3D_OBJECT(self, context):
    layout = self.layout
    layout.operator(ConvertToMesh.bl_idname)
    layout.separator()


def create_menu():
    bpy.types.TOPBAR_MT_file_import.append(TOPBAR_FILE_IMPORT)
    bpy.types.TOPBAR_MT_file_export.append(TOPBAR_FILE_EXPORT)
    bpy.types.VIEW3D_MT_object_context_menu.prepend(VIEW3D_OBJECT)


def remove_menu():
    bpy.types.TOPBAR_MT_file_import.remove(TOPBAR_FILE_IMPORT)
    bpy.types.TOPBAR_MT_file_export.remove(TOPBAR_FILE_EXPORT)
    bpy.types.VIEW3D_MT_object_context_menu.remove(VIEW3D_OBJECT)