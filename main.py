import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf


class window(Gtk.Window):
    def __init__(self):
        #super().__init__(title="PDFCompress")
        super(window, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.set_border_width(10) 
        
        #Grid
        grid = Gtk.Grid(row_spacing=10, column_spacing=10)
        self.set_title("PDFCompress")
        self.set_icon_from_file("logo.png")
        #images
        self.icon1 = GdkPixbuf.Pixbuf.new_from_file("logo.png")
        self.image1 = Gtk.Image()
        self.image1.set_from_pixbuf(self.icon1)

        #Buttons
        #inspdf
        inspdf = Gtk.Button(label="Insert PDF")

        #compdf
        compdf = Gtk.Button(label = "Compress")
        compdf.set_hexpand(True)
        compdf.set_vexpand(True)
        #Radio Buttons
        low = Gtk.RadioButton.new_with_label_from_widget(None, "Low Compression")
        low.connect("clicked", self.on_toggled, "low")

        medium = Gtk.RadioButton.new_with_label_from_widget(low, "Medium Compression")
        medium.connect("clicked", self.on_toggled, "medium")

        high = Gtk.RadioButton.new_with_label_from_widget(low, "High Compression")   
        high.connect("clicked", self.on_toggled, "high")

        #expand
        self.image1.set_hexpand(True)
        self.image1.set_vexpand(True)
        inspdf.set_hexpand(True)
        inspdf.set_vexpand(True)
        low.set_hexpand(True)
        low.set_vexpand(True)
        medium.set_hexpand(True)
        medium.set_vexpand(True)
        high.set_hexpand(True)
        high.set_vexpand(True)
        
        #grid stuff
        grid.attach(self.image1, 1, 0, 1, 1)
        grid.attach(inspdf,      1, 1, 1, 1)
        grid.attach(low,         0, 2, 1, 1)
        grid.attach(medium,      1, 2, 1, 1)
        grid.attach(high,        2, 2, 1, 1)
        grid.attach(compdf,      1, 3, 1, 1)
        self.add(grid)
    
    def on_toggled(self, widget, compress):
        if widget.get_active():
            state = "on"
            if compress == "low":
                print("Low")
            elif compress == "medium":
                print("Medium")
            elif compress == "high":
                print("High")
        else:
            pass

    def insert_pdf(self, widget):
        pass
    def compress(self, widget):
        pass

win = window()
win.connect("destroy", Gtk.main_quit)
#win.set_resizable(False)
win.show_all()
Gtk.main()
