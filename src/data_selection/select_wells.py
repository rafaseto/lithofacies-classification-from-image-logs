import os

# Caminho para a pasta que contém os arquivos catálogo de cada bacia
catalog_path = "../../data/catalogs"

num_wells_with_images = 0

# Iterando sobre cada catálogo da pasta
for catalog in os.listdir(catalog_path):
    wells_with_agp_and_images = set()

    with open(f"../../data/catalogs/{catalog}", "r", encoding="utf-8", errors="ignore") as file:
        # Conjuntos para armazenar os poços com AGP e os poços com perfil de imagem acústica
        wells_with_agp = set()
        wells_with_ubi_or_cast = set()
        
        for line in file:
            
            # Procurando pelo nome AGP na linha atual
            if "/AGP/" in line:
                # O caminho do poço está depois do espaço em branco
                parts = line.strip().split(maxsplit=1)
                
                # Caminho do poço
                path = parts[1]

                # Divide os caminho obtendo seus subdiretórios
                tokens = path.split("/")
                
                try:
                    # Caso a categoria tenha parte1, parte2, etc
                    if "parte" in line:
                        well_id = tokens[4] + "/" + tokens[5]
                        wells_with_agp.add(well_id)
                    # Caso a categoria não esteja subdividida em partes
                    else:
                        well_id = tokens[3] + "/" + tokens[4]
                        wells_with_agp.add(well_id)
                except:
                    pass

            # Caso tenhamos imagem acústica no nome do dlis
            lower_line = line.lower()
            if ".dlis" in lower_line and ("ubi" in lower_line or "cast" in lower_line):
                # O caminho do poço está depois do espaço em branco
                parts = line.strip().split(maxsplit=1)

                # Caminho do poço
                path = parts[1]

                # Divide os caminho obtendo seus subdiretórios
                tokens = path.split("/")

                try:
                    if "parte" in line:
                        well_id = tokens[4] + "/" + tokens[5]
                        wells_with_ubi_or_cast.add(well_id)
                        num_wells_with_images += 1
                    else:
                        well_id = tokens[3] + "/" + tokens[4]
                        wells_with_ubi_or_cast.add(well_id)
                        num_wells_with_images += 1
                except:
                    pass

        # Realiza a interseção dos dois conjuntos para ver quais tem AGP e perfis de imagem
        wells_with_agp_and_images = wells_with_ubi_or_cast.intersection(wells_with_agp)

        # Grava no arquivo de saída
        with open('selected_wells.txt', 'a') as output_file:
            output_file.write(f"{catalog[13:-4]}:\n")
            for well in sorted(wells_with_agp_and_images):
                output_file.write(f"{well}\n")
            output_file.write("\n\n")

# Printando para verificar quantos poços tem perfil de imagem (independente de ter ou nao AGP)
print(f"Number of wells with Acoustic Images: {num_wells_with_images}")