wohnort = "Aarberg"
wohnort2 = "Bern"

print("BASIC")
print("------------------")

if wohnort == "Aarberg":
    print("Ich wohne in " + wohnort)
else:
    print("Ich wohne nicht in " + wohnort2)


if wohnort2 == "Aarberg":
    print("Ich wohne in: " + wohnort2)
else:
    print("Ich wohne nicht in:  " + wohnort2)

print(" ")
print("EXTENDED")
print("------------------")

# Erweitert:
orte = [
    "Aarberg",
    "Bern",
    "Zürich",
    "Basel",
    "Luzern",
    "St. Gallen",
    "Genf",
    "Lausanne",
    "Winterthur",
    "Lugano",
]
wohnort = "Aarberg"

for ort in orte:
    if wohnort == ort:
        print("Ich wohne in " + ort)
    else:
        print("Ich wohne nicht in " + ort)
