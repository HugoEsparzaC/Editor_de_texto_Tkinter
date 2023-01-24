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
        self._crear_componentes()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir')
        boton_guardar = tk.Button(frame_botones, text='Guardar')
        boton_guardar_como = tk.Button(frame_botones, text='Guardar como...')
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        boton_guardar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        frame_botones.grid(row=0, column=0, sticky='ns')
        self.campo_texto.grid(row=0, column=1, sticky='nswe')

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()