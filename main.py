import os
import os.path
import subprocess
import textwrap
import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf


class window(Gtk.Window):
    def __init__(self):
        super(window, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.set_border_width(10)     
        #Grid
        self.grid = Gtk.Grid(row_spacing=10, column_spacing=10)
        self.set_title("PDFCompress")
        self.set_icon_from_file("logo.png")
        #images
        self.icon1 = GdkPixbuf.Pixbuf.new_from_file("logo.png")
        self.image1 = Gtk.Image()
        self.image1.set_from_pixbuf(self.icon1)

        #Buttons
        #inspdf
        self.inspdf = Gtk.Button(label="Insert PDF")
        self.inspdf.connect("clicked", self.insert_pdf)
        #compdf
        compdf = Gtk.Button(label = "Compress")
        compdf.connect("clicked", self.compress_pdf)
        #Radio Buttons
        self.low = Gtk.RadioButton.new_with_label_from_widget(None, "Low Compression")
        self.low.connect("clicked", self.on_toggled, "low")

        self.medium = Gtk.RadioButton.new_with_label_from_widget(self.low, "Medium Compression")
        self.medium.connect("clicked", self.on_toggled, "medium")

        self.high = Gtk.RadioButton.new_with_label_from_widget(self.low, "High Compression")   
        self.high.connect("clicked", self.on_toggled, "high")
        
        #self.filename = Gtk.Label()
        #expand
        self.image1.set_hexpand(True)
        self.image1.set_vexpand(True)
        self.inspdf.set_hexpand(True)
        self.inspdf.set_vexpand(True)
        compdf.set_hexpand(True)
        compdf.set_vexpand(True)
        self.low.set_hexpand(True)
        self.low.set_vexpand(True)
        self.medium.set_hexpand(True)
        self.medium.set_vexpand(True)
        self.high.set_hexpand(True)
        self.high.set_vexpand(True)#grid stuff
        self.grid.attach(self.image1, 1, 0, 1, 1)
        self.grid.attach(self.inspdf, 1, 1, 1, 1)
        self.grid.attach(self.low,    0, 3, 1, 1)
        self.grid.attach(self.medium, 1, 3, 1, 1)
        self.grid.attach(self.high,   2, 3, 1, 1)
        self.grid.attach(compdf,      1, 4, 1, 1)
        #self.grid.attach(self.filename,1, 2, 1, 1)
        
        self.add(self.grid)


    def on_toggled(self, widget, compress):
        if widget.get_active():
            state = "on"
            if compress == "low":
                #print("Low")
                pass
            elif compress == "medium":
                #print("Medium")
                pass
            elif compress == "high":
                #print("High")
                pass
        else:
            pass

    def insert_pdf(self, widget):
        self.dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        self.dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(self.dialog)

        response = self.dialog.run()
        if response == Gtk.ResponseType.OK:
            self.x = self.dialog.get_filename()
            txt = os.path.basename(self.x)
            self.inspdf.get_children()[0].set_label(txt)
            with open('input.txt', 'w') as pdf:
                pdf.write(self.x)

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        self.dialog.destroy()
       

    def add_filters(self, dialog):
        filter_py = Gtk.FileFilter()
        filter_py.set_name("PDF files")
        filter_py.add_mime_type("application/pdf")
        dialog.add_filter(filter_py)
    
    def compress_pdf(self, widget):
        if os.path.exists("input.txt") == False:
            os.system("python3 error.py")
        else:
            open_file = self.x        
            if self.low.get_active():
                command = subprocess.Popen(['bash', 'compress-button.sh', '-l'])
            if self.medium.get_active():
                command = subprocess.Popen(['bash', 'compress-button.sh', '-x'])
            if self.high.get_active():
                command = subprocess.Popen(['bash', 'compress-button.sh', '-m'])
            subprocess.Popen(['xdg-open', '{}'.format(open_file.replace(os.path.basename(open_file), ""))])

win = window()
win.connect("destroy", Gtk.main_quit)
win.set_resizable(False)
win.show_all()
Gtk.main()
