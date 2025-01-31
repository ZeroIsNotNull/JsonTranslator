import json
from deep_translator import GoogleTranslator

class JsonTranslator:

    def __init__(self, from_language: str, to_language: str, input_path: str, output_path: str):
        self.from_language = from_language
        self.to_language = to_language
        self.input_path = input_path
        self.output_path = output_path
        print(f"Class initialized with: {self.input_path} will be translated from {self.from_language} to {self.to_language} and then saved in {self.output_path}")

    def translate(self): 
        with open(self.input_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        flat_data = self.flatten_json(data)
        chunk_size = 4500
        chunks = []
        chunk = {}
        char_count = 0

        for key, value in flat_data.items():
            if value is None:
                continue
            char_count += len(value)
            if char_count > chunk_size:
                chunks.append(chunk)
                chunk = {}
                char_count = len(value)
            chunk[key] = value
        if chunk:
            chunks.append(chunk)

        translated_flat_data = {}
        for chunk in chunks:
            translated_chunk = self.translate_chunk(chunk, self.from_language, self.to_language)
            translated_flat_data.update(translated_chunk)

        translated_data = self.unflatten_json(translated_flat_data)

        with open(self.output_path, "w", encoding="utf-8") as file:
            json.dump(translated_data, file, ensure_ascii=False, indent=4)
        
        print(f"Übersetzungen gespeichert: {self.output_path}")


    def flatten_json(self, y):
        out = {}

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '.')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '.')
                    i += 1
            else:
                out[name[:-1]] = x

        flatten(y)
        return out

    def unflatten_json(self, d):
        result_dict = {}
        for k, v in d.items():
            keys = k.split('.')
            d = result_dict
            for key in keys[:-1]:
                d = d.setdefault(key, {})
            d[keys[-1]] = v
        return result_dict

    def translate_chunk(self, chunk, source_lang, target_lang):
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_chunk = {}
        for key, value in chunk.items():
            translated_chunk[key] = translator.translate(value)
        return translated_chunk
