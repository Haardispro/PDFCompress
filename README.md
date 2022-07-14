# PDFCompress

This is a GUI Frontend for the terminal utility called ghostscript. 

![image](image.png)

### How to run this program:

```bash
git clone https://github.com/Haardipro/PDFCompress
```

```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

After that cd into the PDFCompress direcory, then run main.py

```bash
cd PDFCompress/
python3 main.py #this is the first iteration of the app, lots of bugs
python3 new.py #new iteration of the app, works fine
```

### Stuff left to add:

- [x] Name of selected pdf on the insert pdf button or on a different label

- [x] Opening the directory of the compressed file after compression

- [ ] Converting the application to GTK4

### Bugs

- [ ] Sometimes ghostscript makes the file bigger instead of making it smaller(cannot be solved)

- [x] error.py doesn't open in case of an error

- [x] Pressing compress on the same instance of the application results in a lot of issues
