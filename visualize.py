#-*- coding:utf-8 -*-

# Importation des modules
import argparse
import nglview as nv
from typing import Optional


# Fonction principale
def visualize_molecule(
	file_path: str, 
	representation: str = "cartoon", 
	width: int = 800, 
	height: int = 600, 
	export_html: Optional[str] = None
) -> None:
	"""
	Visualise une molécule à partir d'un fichier en utilisant nglview.
	
	Args:
		file_path (str): Chemin vers le fichier contenant la molécule (PDB, MOL2, etc.).
		representation (str): Mode d'affichage de la molécule ("cartoon", "surface", "ball+stick", etc.).
		width (int): Largeur de la fenêtre de visualisation.
		height (int): Hauteur de la fenêtre de visualisation.
		export_html (Optional[str]): Chemin pour exporter le rendu en HTML (facultatif).
	
	Return:
		None
	"""
	# Chargement de la molécule
	try:
		view = nv.show_file(file_path)
	except Exception as e:
		print(f"Erreur lors du chargement du fichier : {e}")
		return

	# Personnalisation de la taille
	view.layout.width = f"{width}px"
	view.layout.height = f"{height}px"

	# Application du mode d'affichage
	try:
		view.clear_representations()  # Supprime les représentations par défaut
		view.add_representation(representation)
	except Exception as e:
		print(f"Erreur lors de l'application de la représentation : {e}")
		return

	# Affichage interactif
	try:
		print("Affichage de la molécule...")
		view.display()
	except Exception as e:
		print(f"Erreur lors de l'affichage : {e}")

	# Export HTML si demandé
	if export_html:
		try:
			view.export_html(export_html, parameters=None, embed=True)
			print(f"Visualisation exportée avec succès dans : {export_html}")
		except Exception as e:
			print(f"Erreur lors de l'exportation HTML : {e}")

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
	# Configuration des arguments du script
	parser = argparse.ArgumentParser(description="Visualisation de molécules avec NGLView.")
	parser.add_argument("file_path", type=str, help="Chemin vers le fichier de molécule (PDB, MOL2, etc.)")
	parser.add_argument("--representation", type=str, default="cartoon", help="Mode d'affichage de la molécule")
	parser.add_argument("--width", type=int, default=800, help="Largeur de la fenêtre de visualisation")
	parser.add_argument("--height", type=int, default=600, help="Hauteur de la fenêtre de visualisation")
	parser.add_argument("--export_html", type=str, default=None, help="Chemin pour exporter la visualisation en HTML")

	args = parser.parse_args()

	# Appel de la fonction principale
	visualize_molecule(
		file_path=args.file_path,
		representation=args.representation,
		width=args.width,
		height=args.height,
		export_html=args.export_html
	)