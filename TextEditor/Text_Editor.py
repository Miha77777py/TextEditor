"""This is small text editor. I hope, this program will be useful"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
from Скільки_літер import files
import webbrowser


class New_Tkinter:
    """This is code of window"""
    def __init__(self, width, height, title='Text Editor', resizable=(False, False),
                 icon=None):
        self.root = Tk()
        self.root.geometry(f'{width}x{height}+200+200')
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        self.text = ScrolledText(self.root, wrap=WORD, font=('Times New Roman', 11))
        self.variable = IntVar(value=0)
        self.variable2 = IntVar(value=0)
        self.variable3 = IntVar(value=0)

    def run(self):
        """Main btn_and_command. This btn_and_command open the window"""
        self.widget()
        self.root.mainloop()

    def widget(self):
        """This btn_and_command draw widjets (tk)"""
        self.draw_menu()
        self.text.pack()

    @staticmethod
    def more_about_creator():
        """This btn_and_command open website with more information about me"""
        webbrowser.open('https://aboutmiha77777-english.netlify.app/')

    def draw_menu(self):
        """Code of menu bar"""
        menu_bar = Menu(self.root)
        files1 = Menu(menu_bar, tearoff=0)
        information = Menu(menu_bar, tearoff=0)
        color = Menu(menu_bar, tearoff=0)
        bg = Menu(color, tearoff=0)
        fg = Menu(color, tearoff=0)
        fnt = Menu(menu_bar, tearoff=0)

        about = Menu(information, tearoff=0)
        about.add_command(label='About program', command=self.about_program)
        about.add_command(label='About creator', command=self.about_creator)
        about.add_command(label='More about creator', command=self.more_about_creator)

        files1.add_command(label='Open', command=self.file_open)
        files1.add_command(label='Save as', command=self.save_as)
        files1.add_separator()
        files1.add_command(label='Symbols', command=self.letters)
        files1.add_command(label='Delete text', command=self.delete_text)
        files1.add_command(label='Reset all settings', command=self.reset_all_settings)
        files1.add_separator()
        files1.add_command(label='Quit', command=self.root.destroy)

        bg.add_radiobutton(label='White', command=lambda: self.background('white'), variable=self.variable,
                           value=0)
        bg.add_radiobutton(label='Yellow', command=lambda: self.background('yellow'), variable=self.variable,
                           value=1)
        bg.add_radiobutton(label='Cyan', command=lambda: self.background('cyan'), variable=self.variable,
                           value=2)
        bg.add_radiobutton(label='Pink', command=lambda: self.background('pink'), variable=self.variable,
                           value=3)

        fg.add_radiobutton(label='Black', command=lambda: self.foreground('black'), variable=self.variable2, value=0)
        fg.add_radiobutton(label='Blue', command=lambda: self.foreground('blue'), variable=self.variable2, value=1)
        fg.add_radiobutton(label='Red', command=lambda: self.foreground('red'), variable=self.variable2, value=2)
        fg.add_radiobutton(label='Green', command=lambda: self.foreground('green'), variable=self.variable2, value=3)

        fnt.add_radiobutton(label='Times New Roman', font=('Times New Roman', 11), command=lambda:
                            self.font('Times New Roman'),
                            variable=self.variable3, value=0)
        fnt.add_radiobutton(label='Algerian', font=('Algerian', 11), command=lambda: self.font('Algerian'),
                            variable=self.variable3, value=1)
        fnt.add_radiobutton(label='Comic Sans MS', font=('Comic Sans MS', 11), command=lambda:
                            self.font('Comic Sans MS'),
                            variable=self.variable3, value=2)
        fnt.add_radiobutton(label='Forte', font=('Forte', 11), command=lambda: self.font('Forte'),
                            variable=self.variable3, value=3)
        fnt.add_separator()
        fnt.add_command(label='Reset settings', command=self.reset)

        menu_bar.add_cascade(label='File', menu=files1)
        menu_bar.add_cascade(label='Information', menu=information)
        menu_bar.add_cascade(label='Color', menu=color)
        menu_bar.add_cascade(label='Font', menu=fnt)

        color.add_cascade(label='Background', menu=bg)
        color.add_cascade(label='Foreground', menu=fg)
        color.add_separator()
        color.add_command(label='Reset settings', command=self.reset_settings)

        information.add_cascade(label='About...', menu=about)
        self.root.configure(menu=menu_bar)

    def file_open(self):
        """This btn_and_command can open files"""
        self.text.delete("1.0", "10000000000.0")
        file_name = fd.askopenfilename(filetypes=(('Text file', '*.txt'),), defaultextension='*.txt')
        if file_name:
            with open(file_name, 'r') as f:
                self.text.insert(END, f.read())

    def delete_text(self):
        """This btn_and_command delete all text"""
        self.text.delete("1.0", "10000000000.0")

    def background(self, color):
        """This is bg of text field"""
        self.root.configure(bg=color)
        self.text.configure(bg=color)

    def reset(self):
        """This btn_and_command reset font of text"""
        self.text.configure(font=('Times New Roman', 11))
        self.variable3.set(0)

    def font(self, f_o_n_t):
        """This is font of text"""
        self.text.configure(font=(f_o_n_t, 11))
        
    def foreground(self, color):
        """This is fg of text"""
        self.text.configure(foreground=color)

    def reset_settings(self):
        """This btn_and_command reset bg of text"""
        self.text.configure(foreground='black', background='white')
        self.root.configure(bg='white')
        self.variable.set(0)
        self.variable2.set(0)

    def reset_all_settings(self):
        """This btn_and_command reset all settings"""
        self.text.configure(background='white', foreground='black', font=('Times New Roman', 11))
        self.root.configure(bg='white')
        self.variable.set(0)
        self.variable2.set(0)
        self.variable3.set(0)

    def about_program(self):
        """Some information about program"""
        self.text.delete("1.0", "10000000000.0")
        self.text.insert('1.0', '''This program created 13.06.22.This is small text editor. You can write some files, 
save files, open files and count all symbols in your text in few seconds!''')

    def about_creator(self):
        """Some information about me"""
        self.text.delete("1.0", "10000000000.0")
        self.text.insert('1.0', '''Hi! My name is Miha) I`m 11 years old) I`m from Lviv, Ukraine. I really like Python, 
so I did this program) I hope this program will be useful! I wish you have a nice day) Bye-bye!''')

    def save_as(self):
        """This btn_and_command can save files"""
        name = fd.asksaveasfilename(filetypes=(('Text file', '*.txt'),), defaultextension='*.txt')
        if name:
            with open(name, 'w') as w:
                w.write(f'{self.text.get("1.0", "10000000000.0")}')

    def letters(self):
        """This btn_and_command can count letters of text"""
        with open('special.txt', 'w') as special1:
            special1.write(f'{self.text.get("1.0", "10000000000.0")}')
        how_many_letters = files('special.txt')
        if how_many_letters:
            my_messagebox = messagebox.askyesno('Symbols', f'{how_many_letters}\n\nDo you want save result?')
            if my_messagebox:
                self.text.delete("1.0", "10000000000.0")
                self.text.insert('1.0', how_many_letters)
                self.save_as()
        else:
            messagebox.showinfo('Sorry', 'Sorry, I don`t found text(')


a = New_Tkinter(300, 200)
if __name__ == '__main__':
    a.run()
