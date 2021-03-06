###!/usr/bin/env python
bl_info = {
    "name": "Snap_Targets_Menu",
    "author": "Alex McKonst",
    "version": (7, 10),
    "blender": (2, 79, 0),
    "location": "Mesh",
    "description": "",
    "warning": "WIP",
    "wiki_url": "",
    "tracker_url": "https://github.com/AlexMcKonst/SnapTarget",
    "category": "Mesh"}

import bpy
from bpy.props import *
             
def actva(self, context):
    if bpy.context.scene.Actv == True:
        bpy.data.scenes[bpy.context.scene.name].tool_settings.snap_target = 'ACTIVE'
        bpy.context.scene.Actv = False
    elif bpy.context.scene.Mdn == True:
        bpy.data.scenes[bpy.context.scene.name].tool_settings.snap_target = 'MEDIAN'
        bpy.context.scene.Mdn = False
    elif bpy.context.scene.Cntr == True:
        bpy.data.scenes[bpy.context.scene.name].tool_settings.snap_target = 'CENTER'
        bpy.context.scene.Cntr = False
    elif bpy.context.scene.Clst == True:
        bpy.data.scenes[bpy.context.scene.name].tool_settings.snap_target = 'CLOSEST'
        bpy.context.scene.Clst = False
    
bpy.types.Scene.Actv = BoolProperty(
        default = 0,
        update = actva,
        name = 'ACTIVE'
        )
bpy.types.Scene.Mdn = BoolProperty(
        default = 0,
        update = actva,
        name = 'MEDIAN'
        )
bpy.types.Scene.Cntr = BoolProperty(
        default = 0,
        update = actva,
        name = 'CENTER'
        )
bpy.types.Scene.Clst = BoolProperty(
        default = 0,
        update = actva,
        name = 'CLOSEST'
        )

class SnapTarget_menu(bpy.types.Menu):
    bl_label = "SnapTarget"
    bl_idname = "mesh.SnapTarget_menu"

    def draw(self, context):
#        scn = bpy.data.scenes[bpy.context.scene.name].tool_settings.snap_target
        scene = context.scene
        layout = self.layout
        toolsettings = context.tool_settings
        snap_element = toolsettings.snap_element        
#        layout.prop(scn)
        layout.prop(scene, 'Actv', text='ACTIVE')
        layout.prop(scene, 'Mdn', text='MEDIAN')
        layout.prop(scene, 'Cntr', text='CENTER')
        layout.prop(scene, 'Clst', text='CLOSEST')

def register():
    bpy.utils.register_class(SnapTarget_menu)
#    bpy.ops.wm.call_menu(name=SnapTarget_menu.bl_idname)    

def unregister():
    bpy.utils.unregister_class(SnapTarget_menu)

if __name__ == "__main__":
   register()
