import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf

class window(Gtk.Window):
    def __init__(self):
        super(window, self).__init__()
        self.main_ui()
    def main_ui(self):
        self.set_title("Success")
        self.set_border_width(20)
        self.set_icon_from_file("logo.png")
        
        grid = Gtk.Grid(row_spacing = 10, column_spacing=10)

        heading = Gtk.Label()
        heading.set_markup("<big>       Your file has been\ncompressed successfully ✅</big>")
        
#        note = Gtk.Label(label="Note:'Low compression' doesn't always compress your pdf.\nUse Medium or High compression instead")
#        grid.attach(note, 1, 2, 1, 1) 
        grid.attach(heading, 1, 1, 1, 1)
        self.add(grid)
win = window()
win.connect("destroy", Gtk.main_quit)
win.set_resizable(False)
win.show_all()
Gtk.main()
