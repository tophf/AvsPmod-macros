[AvsPmod](https://github.com/AvsPmod/AvsPmod) macros.
==============

# A. rfs-scene.
##### Effort saving companion for per-scene filtering with [rfs()](http://forum.doom9.org/showpost.php?p=1644971&postcount=28 RemapFrames) avisynth plugin.
Requires you to load video scenecuts as bookmarks first.
Use [SCXvid](http://ivtc.vapoursynth.com/yatta%20support/) avisynth plugin or xvid 1st pass (works in VirtualDub too) to generate the log and then load it in AvsPmod via 'macros->import bookmarks from file' macro.

1. [**rfs-scene**](rfs-scene/rfs-scene.py): inserts current scene frame span at cursor position
2. [**rfs-scene1**](rfs-scene/rfs-scene1.py): insert current scene frame span in a comment-tagged **rfs(filter(), "[frames]")** <span style="color:blue"><b>#1</b></span><br/>
Nine macros are provided, each looks for a corresponding comment tag: [#2](rfs-scene/rfs-scene2.py), [#3](rfs-scene/rfs-scene3.py), [#4](rfs-scene/rfs-scene4.py), [#5](rfs-scene/rfs-scene5.py), [#6](rfs-scene/rfs-scene6.py), [#7](rfs-scene/rfs-scene7.py), [#8](rfs-scene/rfs-scene8.py), [#9](rfs-scene/rfs-scene9.py).<br/>
Just assign handy hotkeys for as many macros from this set you would need, like Alt-1, Alt-2, Alt-3, etc or whatever you prefer.
3. [**find RFS for current frame**](rfs-scene/find%20RFS%20for%20current%20frame): finds a frame span that includes the current video frame and selects it.<br/>
You may want to assign e.g. Alt-F3 for convenience.
