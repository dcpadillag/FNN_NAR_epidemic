import matplotlib.pyplot as plt
from matplotlib import rc

def graficar_loss_desde_txt(nombre_archivo, titulo="Curva de pérdida", label="FNN", color='royalblue'):
    """
    Lee un archivo de texto con líneas tipo 'Epoch N, Loss: X' y grafica loss vs epoch.
    """
    rc('font', **{'serif': ['Computer Modern']})
    rc('text', usetex=True)
    rc('legend', fontsize=15)
    rc('xtick', labelsize=15)
    rc('ytick', labelsize=15)
    epochs = []
    losses = []

    with open(nombre_archivo, 'r') as f:
        for linea in f:
            if "Epoch" in linea and "Loss" in linea:
                partes = linea.strip().split(',')
                epoca = int(partes[0].split()[1])
                loss = float(partes[1].split()[1])
                epochs.append(epoca)
                losses.append(loss)

    plt.figure(figsize=(8,5))
    plt.semilogy(epochs, losses, 'o-', label=titulo, color=color)
    plt.xlabel("Época",fontsize = 20)
    plt.ylabel("Pérdida (Loss)",fontsize = 20)
    plt.legend()
    plt.savefig(titulo+'.png', bbox_inches='tight')
    plt.show()

graficar_loss_desde_txt("data_loss/nar-colombia.txt", titulo="NAR - Colombia")

