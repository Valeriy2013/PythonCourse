list_lang = ['C#', 'C++', 'PHP', 'Python']


def get_languages(start_letter, lang_list):
    result = []
    for lang in lang_list:
        if lang[0].lower() == start_letter.lower():
            result.append(lang)
    return result


languages = get_languages('P', list_lang)
print(languages)
