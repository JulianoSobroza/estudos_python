 #MINIBKUPER

import os

import subprocess

import tkinter as tk

from tkinter import filedialog, messagebox


class App:

  def __init__(self, master):

    self.master = master

    master.title("Cópia de dados")


    # Define as pastas de origem e destino

    self.origem = ""

    self.destino = ""


    # Cria o botão "Selecionar Origem"

    self.button_origem = tk.Button(master, text="Selecionar Origem", command=self.select_origem)

    self.button_origem.pack()


    # Cria o botão "Selecionar Destino"

    self.button_destino = tk.Button(master, text="Selecionar Destino", command=self.select_destino)

    self.button_destino.pack()


    # Cria o botão "Copiar"

    self.button_copiar = tk.Button(master, text="Copiar", command=self.copiar)

    self.button_copiar.pack()


  def select_origem(self):

    self.origem = filedialog.askdirectory()


  def select_destino(self):

    self.destino = filedialog.askdirectory()


  def copiar(self):

    if not self.origem:

      messagebox.showwarning("Aviso", "Selecione uma pasta de origem.")

      return

    if not self.destino:

      messagebox.showwarning("Aviso", "Selecione uma pasta de destino.")

      return

    try:

      # Copia a pasta A para o destino

      subprocess.check_call(['rsync', '-a', '--info=progress2', os.path.join(self.origem, 'A'), self.destino])

      # Copia a pasta B para o destino

      subprocess.check_call(['rsync', '-a', '--info=progress2', os.path.join(self.origem, 'B'), self.destino])

      messagebox.showinfo("Sucesso", "Cópia concluída com sucesso!")

    except subprocess.CalledProcessError as e:

      messagebox.showerror("Erro", f"Ocorreu um erro ao copiar os dados: {e}")


root = tk.Tk()

app = App(root)

root.mainloop() 