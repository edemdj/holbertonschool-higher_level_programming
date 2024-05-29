#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Sérialiser un dictionnaire Python en XML et le sauvegarder dans le fichier spécifié.
    
    Paramètres:
    dictionary (dict): Le dictionnaire à sérialiser.
    filename (str): Le nom du fichier dans lequel sauvegarder le XML.
    """
    # Créer l'élément racine
    root = ET.Element("data")
    
    # Fonction récursive pour ajouter des éléments
    def add_elements(parent, d):
        for key, value in d.items():
            child = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_elements(child, value)
            else:
                child.text = str(value)
    
    # Ajouter des éléments au document XML
    add_elements(root, dictionary)
    
    # Créer l'arbre et sauvegarder dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Lire des données XML depuis le fichier spécifié et retourner un dictionnaire Python désérialisé.
    
    Paramètres:
    filename (str): Le nom du fichier XML à lire.
    
    Retourne:
    dict: Un dictionnaire Python désérialisé à partir du XML.
    """
    try:
        # Parser le fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Fonction récursive pour convertir les éléments XML en dictionnaire
        def parse_element(element):
            if len(element) > 0:
                return {child.tag: parse_element(child) for child in element}
            else:
                return element.text
        
        # Reconstruire le dictionnaire
        return {root.tag: parse_element(root)}
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")
        return None
