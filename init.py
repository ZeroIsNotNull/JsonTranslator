import argparse
from json_translator import JsonTranslator

def main():
        parser = argparse.ArgumentParser(description="Read Params now...")
        parser.add_argument("--from_language", type=str, required=True, help="Define the source language (e.g. de, nl, en)")
        parser.add_argument("--to_language", type=str, required=True, help="Define the target language (e.g. de, nl, en)")
        parser.add_argument("--input_path", type=str, required=True, help="Path to an existing Json File, which you want to translate (e.g. ./folder/snippets.json)")
        parser.add_argument("--output_path", type=str, required=True, help="Path of the output file, that will be generated and saved (e.g. ./folder/translated.json)")
        parser.add_argument("--unflatten", type=str, required=True, help="If you want to convert the json file in an unflatted state (true / false => Default is true) ")

        args = parser.parse_args()
        json_translator = JsonTranslator(args.from_language, args.to_language, args.input_path, args.output_path, args.unflatten)
        json_translator.translate()
         
if __name__ == "__main__":
    main()