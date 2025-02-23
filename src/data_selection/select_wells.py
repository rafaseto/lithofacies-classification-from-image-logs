# Abrindo o arquivo Catalogo.txt e buscando linhas com a pasta AGP
with open("md5_Catalogo_Bacia_do_Reconcavo.txt", "r", encoding="utf-8", errors="ignore") as file:
    wells_with_agp = set()
    wells_with_ubi_or_cast = set()
    
    for line in file:
        
        # Searching for wells with AGP
        if "/AGP/" in line:
            # The path of the well is after the blank space
            parts = line.strip().split()
               
            # Getting the path of the well
            path = parts[1]

            # Splitting the path into its subdirectories
            tokens = path.split("/")
                
            well_id = tokens[4] + "/" + tokens[5]
            wells_with_agp.add(well_id)

        # Searching for wells with acoustic images
        lower_line = line.lower()
        if ".dlis" in lower_line and ("ubi" in lower_line or "cast" in lower_line):
            # The path of the well is after the blank space
            parts = line.strip().split()

            # Getting the path of the well
            path = parts[1]

            # Splitting the path into its subdirectories
            tokens = path.split("/")

            well_id = tokens[4] + "/" + tokens[5]
            wells_with_ubi_or_cast.add(well_id)

wells_with_agp_and_images = wells_with_ubi_or_cast.intersection(wells_with_agp)

print("Poços que possuem a pasta AGP:")
for well in sorted(wells_with_agp):
    print(well)

print("")
print("")

print("Poços que possuem UBI ou CAST:")
for well in sorted(wells_with_ubi_or_cast):
    print(well)

print("")
print("")

print("Poços que possuem AGP e (UBI ou CAST):")
for well in sorted(wells_with_agp_and_images):
    print(well)