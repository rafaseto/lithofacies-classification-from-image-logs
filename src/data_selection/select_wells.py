import os

catalog_path = "../../data/catalogs"

for catalog in os.listdir(catalog_path):
    wells_with_agp_and_images = set()
    with open(f"../../data/catalogs/{catalog}", "r", encoding="utf-8", errors="ignore") as file:
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
                
                try:
                    if "parte" in line:
                        well_id = tokens[4] + "/" + tokens[5]
                        wells_with_agp.add(well_id)
                    else:
                        well_id = tokens[3] + "/" + tokens[4]
                        wells_with_agp.add(well_id)
                except:
                    pass

            # Searching for wells with acoustic images
            lower_line = line.lower()
            if ".dlis" in lower_line and ("ubi" in lower_line or "cast" in lower_line):
                # The path of the well is after the blank space
                parts = line.strip().split()

                # Getting the path of the well
                path = parts[1]

                # Splitting the path into its subdirectories
                tokens = path.split("/")

                try:
                    if "parte" in line:
                        well_id = tokens[4] + "/" + tokens[5]
                        wells_with_ubi_or_cast.add(well_id)
                    else:
                        well_id = tokens[3] + "/" + tokens[4]
                        wells_with_ubi_or_cast.add(well_id)
                except:
                    pass

        wells_with_agp_and_images = wells_with_ubi_or_cast.intersection(wells_with_agp)

        with open('selected_wells.txt', 'a') as output_file:
            output_file.write(f"{catalog}:\n")
            for well in sorted(wells_with_agp_and_images):
                output_file.write(f"{well}\n")
            output_file.write("\n\n")