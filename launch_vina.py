# -*- coding:utf-8 -*-

# Importation des modules
import argparse
from vina import Vina # type: ignore
from typing import Tuple

def read_box_file(file_path: str) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    """
    Lit les paramètres de la boîte depuis un fichier et extrait le centre et la taille.

    Args:
        file_path (str): Chemin vers le fichier contenant les paramètres de la boîte.

    Returns:
        tuple[tuple[float, float, float], tuple[float, float, float]]: 
        Une paire contenant le centre (x, y, z) et la taille (x, y, z) de la boîte.

    """
    # Initialisation du dictionnaire
    box_params = {}

    # Ouverture du fichier
    with open(file_path, 'r') as f:
        # Lire chaque ligne du fichier et extraire les paramètres clés/valeurs
        for line in f:
            key, value = line.strip().split('=')
            box_params[key.strip()] = float(value.strip())

    # Extraire les coordonnées du centre de la boîte
    center = (box_params["center_x"], box_params["center_y"], box_params["center_z"])

    # Extraire les dimensions de la boîte
    size = (box_params["size_x"], box_params["size_y"], box_params["size_z"])

    return center, size

def main():
    """
    Fonction principale pour exécuter le docking basé sur les arguments de ligne de commande.
    """
    # Configurer le parser pour les arguments de ligne de commande
    parser = argparse.ArgumentParser(description="Docking tool based on Vina.")
    parser.add_argument("--sf_name", choices=["vina", "ad4"], default="vina", help="Fonction de score à utiliser : 'vina' ou 'ad4' (par défaut : 'vina').")
    parser.add_argument("--ligand", required=True, help="Chemin vers le fichier ligand au format PDBQT.")
    parser.add_argument("--output", required=True, help="Chemin pour sauvegarder les résultats du docking au format PDBQT.")
    parser.add_argument("--exhaustiveness", type=int, default=8, help="Exhaustivité de la recherche globale (par défaut : 8).")
    parser.add_argument("--num_poses", type=int, default=20, help="Nombre de poses à tester et sauvegarder (par défaut : 20).")
    parser.add_argument("--box", help="Chemin vers le fichier de configuration de la boîte (obligatoire pour le mode 'vina').")
    parser.add_argument("--receptor", help="Chemin vers le fichier récepteur au format PDBQT (obligatoire pour le mode 'vina').")
    parser.add_argument("--maps_prefix", help="Préfixe pour les fichiers de cartes pré-calculées (obligatoire pour le mode 'ad4').")

    # Récupérer les arguments
    args = parser.parse_args()

    # Validation des arguments en fonction du mode sélectionné
    if args.sf_name == "vina":
        if not args.receptor:
            raise ValueError("L'argument --receptor est requis pour le mode 'vina'.")
        if not args.box:
            raise ValueError("L'argument --box est requis pour le mode 'vina'.")
    elif args.sf_name == "ad4":
        if not args.maps_prefix:
            raise ValueError("L'argument --maps_prefix est requis pour le mode 'ad4'.")
        if args.receptor:
            print("Attention : L'argument --receptor est ignoré en mode 'ad4'.")
        if args.box:
            print("Attention : L'argument --box est ignoré en mode 'ad4'.")

    # Initialiser l'objet Vina
    docking_object = Vina(sf_name=args.sf_name)

    if args.sf_name == "vina":
        # Configuration spécifique au mode 'vina'
        docking_object.set_receptor(args.receptor)
        center, box_size = read_box_file(args.box)
        docking_object.compute_vina_maps(center=center, box_size=box_size)
    elif args.sf_name == "ad4":
        # Charger les cartes pré-calculées pour le mode 'ad4'
        docking_object.load_maps(map_prefix_filename=args.maps_prefix)

    # Charger le ligand pour le docking
    docking_object.set_ligand_from_file(args.ligand)

    # Exécuter le docking avec les paramètres spécifiés
    docking_object.dock(exhaustiveness=args.exhaustiveness, n_poses=args.num_poses)

    # Sauvegarder les résultats
    docking_object.write_poses(args.output, n_poses=args.num_poses, overwrite=True)

    # Afficher un message de confirmation
    print(f"Docking terminé avec la fonction de score '{args.sf_name}' utilisant {args.num_poses} pose(s). Résultats sauvegardés dans {args.output}.")

if __name__ == "__main__":
    main()