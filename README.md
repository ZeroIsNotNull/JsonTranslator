# JsonTranslator

## What is it for?
Use this Python Script to translate values of a Json-File.
The data structure will remain untouched. All values are translated in your target language.
The application uses the DeepTranslator Module.
It is needed to be installed before starting the application.
pip install -U deep-translator

## Start the application it with 4 Params
After installation just call init.py with some parameters.
For example:
python init.py --from_language nl --to_language en --input_path snippets.json --output_path translated.json
Parameters: --from_language => define the source language
            --to_language => define the target language
            --input_path => source Json-File (eg "./source/snippets.json") you wish to translate
            --output_path => source Json-File (eg "./traget/translated.json") you wish to translate


I added an example snippets.json, which you can use for your trials.