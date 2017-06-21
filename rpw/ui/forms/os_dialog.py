""" Standard IO Dialogs

Original code by github.com/eirannejad/pyRevit

"""  #

from rpw.ui.forms.resources import *

def select_folder():
    """
    Selects a Folder Path using the standard OS Dialog.
    Uses Forms.FolderBrowserDialog(). For more information see:
    https://msdn.microsoft.com/en-us/library/system.windows.forms.openfiledialog.

    >>> folderpath = select_folder()
    'C:\\folder\\path'
    """

    form = Forms.FolderBrowserDialog()
    if form.ShowDialog() == Forms.DialogResult.OK:
        return form.SelectedPath


def select_file(extensions='All Files (*.*)|*.*',
                title="Select File",
                multiple=False,
                restore_directory=True):
    """
    Selects a File Path using the standard OS Dialog.
    Uses Forms.OpenFileDialog
    https://msdn.microsoft.com/en-us/library/system.windows.forms.filedialog.filter

    >>> filepath = select_file('Revit File ('*.rvt)|*.rvt')
    'C:\\folder\\file.rvt'

    Args:
        extensions (str, optional): File Extensions Filtering options. Default is All Files (*.*)|*.*
        title (str, optional): File Extensions Filtering options
        multiple (bool): Allow selection of multiple files. Default is `False`
        restore_directory (bool): Restores the directory to the previously selected directory before closing

    """
    form = Forms.OpenFileDialog()
    form.Filter = extensions
    form.Title = title
    form.Multiselect = multiple
    form.RestoreDirectory = restore_directory
    if form.ShowDialog() == Forms.DialogResult.OK:
        return form.FileName

# Tests
if __name__ == '__main__':
    print(select_folder())
    print(select_file('Python Files|*.py'))
