#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """covert a dictionnary to an xml file"""
    # crreate the root element
    root = ET.Element("data")
    
    def add_elements(parent, d):
        for key, value in d.items():
            child = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_elements(child, value)
            else:
                child.text = str(value)
    
    add_elements(root, dictionary)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """convert an xml file to a dictionnary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        def parse_element(element):
            if len(element) > 0:
                return {child.tag: parse_element(child) for child in element}
            else:
                return element.text
        
        return {root.tag: parse_element(root)}
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")
        return None
