import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="PDFCompress")
        self.set_border_width(10)
        box = Gtk.VBox()
        vb = Gtk.VBox()
        hb = Gtk.HBox()
        
        heading = Gtk.Label(label="PDFCompress")
        vb.pack_start(heading, True, True, 10)

       
        #btn2 = Gtk.Button(label="Compress PDF")
        #hb.pack_start(btn2, True, True, 5)
        low = Gtk.RadioButton.new_with_label_from_widget(None, "Low Compression")
        vb.pack_start(low, True, True, 5)
        

        medium = Gtk.RadioButton.new_with_label_from_widget(None, "Medium Compression")
        vb.pack_start(medium, True, True, 5)
        

        high = Gtk.RadioButton.new_with_label_from_widget(None, "High Compression")
        vb.pack_start(high, True, True, 5)

        btn1 = Gtk.Button(label="Insert PDF")
        hb.pack_start(btn1, True, True, 5)
        
        btn2 = Gtk.Button(label="Compress PDF")
        hb.pack_start(btn2, True, True, 5)

        btn3 = Gtk.Button(label="Download PDF")
        hb.pack_start(btn3, True, True, 5)


        """
        self.heading = Gtk.Label(label="PDFCompress")
        self.box.pack_start(self.heading, True, True, 0)
        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        """
        #Adding Stuff
        self.add(box)
        box.add(vb)
        box.add(hb)
    """
    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")
    """

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
