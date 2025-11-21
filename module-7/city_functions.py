def city_country(city, country, population=None, language=None):
    text = f"{city.title()}, {country.title()}"

    if population:
        text += f" - population {population}"

    if language:
        text += f", {language.title()}"

    return text


# Final required calls (3 calls)
print(city_country("santiago", "chile"))
print(city_country("seattle", "united states", 750000))
print(city_country("dubai", "uae", 3300000, "arabic"))







