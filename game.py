import tkinter as tk
from tkinter import messagebox
from random import randint


class AdivinheONumero:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivinhe o número")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.num_secreto = 0
        self.tentativas_restantes = 0

        self.frame_inicial = tk.Frame(root, bg="#FFF2CC")
        self.frame_dificuldade = tk.Frame(root, bg="#D9EAD3")
        self.frame_jogo = tk.Frame(root, bg="#CFE2F3")

        self.entrada = None
        self.label_tentativas = None

        self.tela_inicial()

    def limpar_frames(self):
        for frame in [self.frame_inicial, self.frame_dificuldade, self.frame_jogo]:
            frame.pack_forget()

    def tela_inicial(self):
        self.limpar_frames()
        for widget in self.frame_inicial.winfo_children():
            widget.destroy()

        self.frame_inicial.pack(expand=True, fill='both')

        titulo = tk.Label(
            self.frame_inicial,
            text="Bem vindo(a)",
            font=("Comic Sans MS", 18, "bold"),
            bg="#FFF2CC",
            fg="#FF5733"
        )
        titulo.pack(pady=30)

        btn_iniciar = tk.Button(
            self.frame_inicial,
            text="Iniciar o Jogo",
            command=self.tela_dificuldade,
            bg="#FFBD59",
            fg="black",
            font=("Comic Sans MS", 12, "bold"),
            width=15
        )
        btn_iniciar.pack()

    def tela_dificuldade(self):
        self.limpar_frames()
        for widget in self.frame_dificuldade.winfo_children():
            widget.destroy()

        self.frame_dificuldade.pack(expand=True, fill='both')

        titulo = tk.Label(
            self.frame_dificuldade,
            text="Escolha a dificuldade",
            font=("Comic Sans MS", 14),
            bg="#D9EAD3",
            fg="#38761D"
        )
        titulo.pack(pady=20)

        btn_facil = tk.Button(
            self.frame_dificuldade,
            text="Fácil (5 tentativas)",
            command=lambda: self.iniciar_jogo(5),
            bg="#B6D7A8",
            font=("Comic Sans MS", 12)
        )
        btn_medio = tk.Button(
            self.frame_dificuldade,
            text="Médio (3 tentativas)",
            command=lambda: self.iniciar_jogo(3),
            bg="#FFE599",
            font=("Comic Sans MS", 12)
        )
        btn_dificil = tk.Button(
            self.frame_dificuldade,
            text="Difícil (1 tentativa)",
            command=lambda: self.iniciar_jogo(1),
            bg="#EA9999",
            font=("Comic Sans MS", 12)
        )

        btn_facil.pack(pady=5)
        btn_medio.pack(pady=5)
        btn_dificil.pack(pady=5)

    def iniciar_jogo(self, tentativas):
        self.num_secreto = randint(1, 10)
        self.tentativas_restantes = tentativas

        self.limpar_frames()
        for widget in self.frame_jogo.winfo_children():
            widget.destroy()

        self.frame_jogo.pack(expand=True, fill='both')

        instrucoes = tk.Label(
            self.frame_jogo,
            text="Adivinhe o número de 1 a 10",
            font=("Comic Sans MS", 12),
            bg="#CFE2F3",
            fg="#3D85C6"
        )
        instrucoes.pack(pady=10)

        self.label_tentativas = tk.Label(
            self.frame_jogo,
            text=f"Tentativas restantes: {self.tentativas_restantes}",
            font=("Comic Sans MS", 11),
            bg="#CFE2F3"
        )
        self.label_tentativas.pack(pady=5)

        self.entrada = tk.Entry(self.frame_jogo, font=("Comic Sans MS", 12))
        self.entrada.pack()
        self.entrada.bind('<Return>', lambda event: self.verificar_palpite())

        btn_enviar = tk.Button(
            self.frame_jogo,
            text="Enviar",
            command=self.verificar_palpite,
            bg="#A4C2F4",
            font=("Comic Sans MS", 12),
            width=10
        )
        btn_enviar.pack(pady=10)

    def verificar_palpite(self):
        palpite = self.entrada.get()

        if not palpite.isdigit():
            messagebox.showwarning(
                "Entrada inválida", "Digite apenas números de 1 a 10.")
            return

        palpite = int(palpite)

        if palpite == self.num_secreto:
            self.exibir_resultado("Você acertou! Parabéns!", True)
        else:
            self.tentativas_restantes -= 1
            if self.tentativas_restantes == 0:
                self.exibir_resultado(
                    f"Você perdeu! O número era {self.num_secreto}.", False)
            else:
                self.label_tentativas.config(
                    text=f"Tentativas restantes: {self.tentativas_restantes}")
                self.entrada.delete(0, tk.END)

    def exibir_resultado(self, mensagem, venceu):
        resposta = messagebox.askquestion(
            "Fim de jogo",
            f"{mensagem}\n\nDeseja jogar novamente?"
        )
        if resposta == 'yes':
            self.tela_dificuldade()
        else:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinheONumero(root)
    root.mainloop()
