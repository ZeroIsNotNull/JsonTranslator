# JsonTranslator

## What is it for?
Use this Python Script to translate values of a Json-File.
The data structure will remain untouched. All values are translated in your target language.
The application uses the DeepTranslator Module.
It is needed to be installed before starting the application.
pip install -U deep-translator

## Start the application it with 5 Params
After installation just call init.py with some parameters.
For example:
python3 init.py --from_language de --to_language en --input_path snippets.json --output_path translated.json --unflattes true
Parameters: 
           ```markdown
            --from_language => define the source language
            --to_language => define the target language
            --input_path => source Json-File (eg "./source/snippets.json") you wish to translate
            --output_path => source Json-File (eg "./traget/translated.json") you wish to translate
            --unflatten => If you want to convert the json file in an unflatted state (true / false => Default is true)
           ```


I added an example snippets.json-example, which you can use for your trials. Just remove "-example" from filename.