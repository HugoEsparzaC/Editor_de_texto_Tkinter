import tkinter as tk
class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de Texto')
        self.iconbitmap('texteditor.ico')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        self.archivo = None
        self.archivo_abierto = False

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()