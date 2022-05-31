from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid")
        grid = Gtk.Grid()
        self.add(grid)
        #Buttons
        """
        btn1 = Gtk.Button(label="1")
        btn2 = Gtk.Button(label="2")
        btn3 = Gtk.Button(label="3")
        btn4 = Gtk.Button(label="4")
        btn5 = Gtk.Button(label="5")
        btn6 = Gtk.Button(label="6")
        grid.add(btn1)
        grid.attach(btn2, 1, 0, 2, 1)
        grid.attach_next_to(btn3, btn1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(btn4, btn3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(btn5, 1, 2, 1, 1)
        grid.attach_next_to(btn6, btn5, Gtk.PositionType.RIGHT, 1, 1)
        """
        low = Gtk.RadioButton.new_with_label_from_widget(None, "Low Compression")
        medium = Gtk.RadioButton.new_with_label_from_widget(None, "Medium Compression")
        high = Gtk.RadioButton.new_with_label_from_widget(None, "High Compression")     
        btn1 = Gtk.Button(label="Insert PDF")
        btn2 = Gtk.Button(label="Compress PDF")
        btn3 = Gtk.Button(label="Download PDF")

        
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()


