import numpy as np
import matplotlib.pyplot as plt

colors = {
    "RB": "#1E90FF",  # Royal Blue
    "B": "#0000FF",   # Blue
    "CW": "#FFFFFF",  # Cold White
    "FS": "#FFD700",  # Full Spectrum
    "G": "#00FF00",   # Green
    "R": "#FF0000"    # Red
}

# Cria a matriz 8x14
new_grid = np.array([
    ["RB", "RB", "FS", "CW", "RB", "RB", "B", "FS", "RB", "RB", "B", "CW", "RB", "RB"],
    ["RB", "G",  "RB", "RB", "B", "G", "R", "RB", "B", "G", "R", "RB", "B", "RB"],
    ["B",  "RB", "R", "B",  "CW", "RB", "RB", "B",  "FS", "RB", "RB", "B", "CW", "RB"],
    ["RB", "RB", "B", "FS", "RB", "RB", "B", "CW", "RB", "RB", "B", "FS", "RB", "RB"],
    ["B",  "CW", "RB", "G", "B", "FS", "RB", "RB", "B", "CW", "R", "RB", "B", "FS"],
    ["RB", "R", "B", "CW", "RB", "R",  "B", "FS", "RB", "RB", "B", "CW", "RB", "R"],
    ["RB", "B",  "FS", "RB", "RB", "B", "CW", "G", "RB", "B", "FS", "RB", "G", "B"],
    ["G", "RB", "RB", "B",  "FS", "RB", "RB", "B",  "RB", "RB", "RB", "B",  "FS", "RB"]
])

# Conta a quantidade de cada tipo de LED
unique, counts = np.unique(new_grid, return_counts=True)
led_counts = dict(zip(unique, counts))

# Exibe a quantidade de cada tipo de LED
for led, count in led_counts.items():
    print(f"{led}: {count}")

# Função para criar e salvar uma imagem de uma matriz
def plot_matrix(matrix, filename):
    fig, ax = plt.subplots(figsize=(7, 4))
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            led_type = matrix[i, j]
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=colors[led_type]))
            ax.text(j + 0.5, i + 0.5, led_type, color="black", ha='center', va='center', fontsize=8)
    
    # Configurações da plotagem
    ax.set_xlim(0, matrix.shape[1])
    ax.set_ylim(0, matrix.shape[0])
    ax.set_xticks(np.arange(matrix.shape[1]) + 0.5)
    ax.set_yticks(np.arange(matrix.shape[0]) + 0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    
    plt.gca().invert_yaxis()
    plt.title(f"Distribuição dos LEDs na Matriz {matrix.shape[0]}x{matrix.shape[1]}")
    plt.savefig(filename)
    plt.close()

# Divide a matriz 8x14 em quatro matrizes 4x7
matrices_4x7 = [
    new_grid[:4, :7],
    new_grid[:4, 7:],
    new_grid[4:, :7],
    new_grid[4:, 7:]
]

# Salva cada uma das quatro matrizes como uma imagem
for idx, matrix in enumerate(matrices_4x7):
    plot_matrix(matrix, f"matriz_4x7_{idx+1}.png")

print("Imagens salvas com sucesso.")
