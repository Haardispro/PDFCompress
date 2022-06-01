import subprocess
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
        inspdf.connect("clicked", self.insert_pdf)
        #compdf
        compdf = Gtk.Button(label = "Compress")
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
        compdf.set_hexpand(True)
        compdf.set_vexpand(True)
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
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_py = Gtk.FileFilter()
        filter_py.set_name("PDF files")
        filter_py.add_mime_type("application/pdf")
        dialog.add_filter(filter_py)
        """
        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
        """
    def compress(self, widget):
        
        #command = subprocess.Popen(['bash', 'compress-button.sh', '-l'])
        #command = subprocess.Popen(['bash', 'compress-button.sh', '-x'])
        #command = subprocess.Popen(['bash', 'compress-button.sh', '-m'])
        pass

win = window()
win.connect("destroy", Gtk.main_quit)
#win.set_resizable(False)
win.show_all()
Gtk.main()
