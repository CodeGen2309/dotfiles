# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You can import any python module as needed.
import os
from PIL import ImageOps, Image

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import Command


# Any class that is a subclass of "Command" will be integrated into ranger as a
# command.  Try typing ":my_edit<ENTER>" in ranger!
class my_edit(Command):
    # The so-called doc-string of the class will be visible in the built-in
    # help that is accessible by typing "?c" inside ranger.
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # The execute method is called when you run this command in ranger.
    def execute(self):
        # self.arg(1) is the first (space-separated) argument to the function.
        # This way you can write ":my_edit somefilename<ENTER>".
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.rest(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path

        # This is a generic function to print text in ranger.
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # Using bad=True in fm.notify allows you to print error messages:
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # This executes a function from ranger.core.actions, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        self.fm.edit_file(target_filename)

    # The tab method is called when you press tab, and should return a list of
    # suggestions that the user will tab through.
    # tabnum is 1 for <TAB> and -1 for <S-TAB> by default
    def tab(self, tabnum):
        # This is a generic tab-completion function that iterates through the
        # content of the current directory.
        return self._tab_directory_content()



class setpaper (Command):
  """ :setpaper """
  def execute(self, monitor = 'left'):
    # self.fm.execute_console('echo "EPTA"')
    currFile   = self.fm.thisfile
    test = self.setWallpaper(monitor, currFile)
    
    return False


  def setWallpaper (self, monitor, file):
    monList = {"left": "HDMI-A-1", "right": "DVI-D-1"}
    currMonitor= monList[monitor]

    preload = f"hyprctl hyprpaper preload {file}"
    wallpaper = f"hyprctl hyprpaper wallpaper {currMonitor}, {file}"
    test = self.fm.execute_console("hyprctl")
    # return test


class batchGScale(Command):
  """
    :batchGScale
  """

  def execute(self):
    selection = self.fm.thistab.get_selection()

    for item in selection:
      self.gScaleFile(item)

    return True


  def testFile(self, file):
    name = file.basename
    
    self.fm.notify(name)
    return True


  def gScaleFile(self, file):
    name = file.basename
    parent = self.fm.thisdir.path
    savePath = f"{parent}/dim/"

    if not file.image: 
      self.fm.notify('NOT AN IMAGE')
      return False


    if not os.path.exists(savePath):
      self.fm.mkdir(savePath)

    image = Image.open(file.path)
    dimmed = ImageOps.grayscale(image)
    result = dimmed.save(f"{savePath}/{name}")
    return True



class batchRename(Command):
  """
    :batchRename
  """

  def execute(self):
    counter = 1
    selection = self.fm.thistab.get_selection()

    for item in selection:
      self.renFile(item, counter)
      counter += 1

    self.fm.notify('rename done!')
    return True


  def testFile(self, file):
    name = file.basename
    ext = file.extension
    
    self.fm.notify(ext)
    return True



  def renFile(self, file, newName):
    filePath = file.path
    fileExt = file.extension
    currDir = self.fm.thisdir.path
    renDir = f"{currDir}/renamed"
    newPath = f"{renDir}/{newName}.{fileExt}"

    if not os.path.exists(newPath):
      self.fm.mkdir(renDir)

    self.fm.rename(file, newPath)
    return True
