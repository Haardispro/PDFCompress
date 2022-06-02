from gi.repository import Gtk, Gdk, GdkPixbuf

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Error")
        self.set_border_width(10)
        grid = Gtk.Grid()
        self.add(grid)
        
        error = Gtk.Label('Error')
        error.set_markup("<big>Error</big>")
        
        self.icon1 = GdkPixbuf.Pixbuf.new_from_file("error.png")
        self.image1 = Gtk.Image()
        self.image1.set_from_pixbuf(self.icon1)
        
        grid.attach(error, 1, 1, 1, 1)
        grid.attach(self.image1, 1, 2, 1, 1)
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.set_resizable(False)
window.show_all()
Gtk.main()


