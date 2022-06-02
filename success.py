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
        heading = Gtk.Label(label="Your file has been compressed\nsuccessfully")
        #open_file_path = Gtk.Button("Open File Directory")
        #open_file_path.connect("clicked", self.open_file)
        #grid.attach(open_file_path, 1, 2, 1, 1)
        grid.attach(heading, 1, 1, 1, 1)
        self.add(grid)
    #def open_file(self, widget):
        #command = subprocess.Popen(['xdg-open', '.'])
win = window()
win.connect("destroy", Gtk.main_quit)
win.set_resizable(False)
win.show_all()
Gtk.main()
