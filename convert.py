import argparse
import logging
import sys
from core.dispatcher import ConversionDispatcher
from core.detect import detect_type
from core.plugins import load_all_plugins

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("conversion.log", mode='a', encoding='utf-8')
        ]
    )

def main():
    setup_logger()
    parser = argparse.ArgumentParser(description="Convertisseur universel de fichiers ultra-sophistiqué")
    parser.add_argument("input", help="Fichier source à convertir")
    parser.add_argument("output", help="Fichier de sortie")
    parser.add_argument("output_format", help="Format de sortie désiré (ex: pdf, txt, png, mp3, zip, etc.)")
    parser.add_argument("--list-formats", action="store_true", help="Lister tous les formats supportés")
    parser.add_argument("--metadata", action="store_true", help="Inclure la conversion des métadonnées si possible")
    args = parser.parse_args()

    load_all_plugins()

    if args.list_formats:
        ConversionDispatcher.list_supported_formats()
        sys.exit(0)

    try:
        mime, description = detect_type(args.input)
        logging.info(f"Type détecté: {mime} ({description})")
        ConversionDispatcher.convert(
            input_path=args.input,
            output_path=args.output,
            output_format=args.output_format,
            convert_metadata=args.metadata
        )
    except Exception as e:
        logging.error(f"Erreur lors de la conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()