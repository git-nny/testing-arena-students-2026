# Test Cases

- funktion parse_time()
    - führende Nullen funktionieren
    - falsche Trennung -> Val Error
    - umgang mit ms wird abgefangen -> Val Error
    - ungang mit Zahlen zw. 0 und 23 bzw. 0 und 59 im korrekten Format
    -> sollte alles Value Error auslösen

- parse_measurements(line)
    - test if value error is called on longer/shorter
    - komma vs. punkt?
    - Datenmodell korrekt? (Umgang mit mehr/weniger als drei Eingaben?)
    - umgang mit negativen Zahlen (bei Temperatur UND Zeit)
    - zahlen dürfen nicht vertauscht sein
    

- filter_by_temperature_regular_values
    - Randconditions testen -> grenzen sind inklusive?
    - Länge der Liste stimmt
    - falsche Reihenfolge von lower/upper -> Value Error

- average tempertautre 
    - Stadtname: Case-sensitiveness testen


"""Starter tests for the weather module.
 
These tests deliberately cover only ordinary examples. T


 

 
# def test_average_temperature_Errors():
#      # len(temperatures) == 0
#     with pytest.raises(ValueError, match="No measurements found for city."):
#         filter_by_temperature(, 7, 0)
#         filter_by_temperature(5, 0, 0)
 
