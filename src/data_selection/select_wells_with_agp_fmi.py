import os
from tkinter import Tk, filedialog

def main():
    # Oculta a janela principal do Tkinter
    root = Tk()
    root.withdraw()

    # Seleção do arquivo de catálogo (.txt)
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo .txt de catálogo",
        filetypes=[("Arquivos de Texto", "*.txt")]
    )

    if not file_path:
        print("Nenhum arquivo selecionado. Encerrando.")
        return

    # Contadores e estruturas para armazenar caminhos
    num_fmi_files = 0
    num_agp_files = 0
    agp_paths_by_well = {}
    fmi_paths_by_well = {}

    # Processa o arquivo de catálogo
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            parts = line.strip().split(maxsplit=1)
            if len(parts) < 2:
                continue
            path = parts[1]
            tokens = path.split("/")

            # Determina well_id conforme padrão de diretórios
            try:
                if "parte" in line.lower():
                    well_id = f"{tokens[4]}/{tokens[5]}"
                else:
                    well_id = f"{tokens[3]}/{tokens[4]}"
            except IndexError:
                continue

            lower_line = line.lower()
            # Armazena caminhos AGP
            if "/agp/" in lower_line:
                agp_paths_by_well.setdefault(well_id, []).append(path)
                num_agp_files += 1

            # Armazena caminhos FMI
            if ".dlis" in lower_line and "fmi" in lower_line:
                fmi_paths_by_well.setdefault(well_id, []).append(path)
                num_fmi_files += 1

    # Interseção de wells que têm AGP e FMI
    wells_common = set(agp_paths_by_well.keys()).intersection(fmi_paths_by_well.keys())

    # Define arquivo de saída na mesma pasta do catálogo
    output_file_path = os.path.join(
        os.path.dirname(file_path),
        'selected_wells_AGP_FMI_paths.txt'
    )

    # Grava no arquivo os caminhos completos dos arquivos para cada well
    with open(output_file_path, 'w', encoding="utf-8") as output_file:
        # output_file.write("# Caminhos AGP e FMI para poços selecionados\n")
        for well in sorted(wells_common):
            # output_file.write(f"## Poço: {well}\n")
            # AGP
            for agp_path in agp_paths_by_well[well]:
                output_file.write(f"{agp_path}\n")
            # FMI
            for fmi_path in fmi_paths_by_well[well]:
                output_file.write(f"{fmi_path}\n")
            # output_file.write("\n")

    # Resumo no console
    print(f"Número de arquivos AGP encontrados: {num_agp_files}")
    print(f"Número de arquivos FMI encontrados: {num_fmi_files}")
    print(f"Total de poços com AGP e FMI: {len(wells_common)}")
    print(f"Arquivo de saída com caminhos completos: {output_file_path}")

if __name__ == "__main__":
    main()
