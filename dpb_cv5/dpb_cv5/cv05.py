from init import collection
import datetime
import pymongo

#'''
#DPB - 5. Cvičení

#Implementujte jednotlivé body pomocí PyMongo knihovny - rozhraní je téměř stejné jako v Mongo shellu.
#Před testováním Vašich řešení si nezapomeňte zapnout Mongo v Dockeru.

#Pro pomoc je možné např. použít https://www.w3schools.com/python/python_mongodb_getstarted.asp

#Funkce find vrací kurzor - pro vypsání výsledku je potřeba pomocí foru iterovat nad kurzorem:

#cursor = collection.find(...)
#for restaurant in cursor:
#    print(restaurant) # případně print(restaurant['name'])

#Všechny výsledky limitujte na 10 záznamů. Nepoužívejte české názvy proměnných!
#'''


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')

if __name__ == "__main__":
    # 1. Vypsání všech restaurací 
    print_delimiter(1)
    for x in collection.find({"grades.score": {"$gt": 80}}):
        print(x)
    # 2. Vypsání všech restaurací - pouze názvů, abecedně seřazených
    print_delimiter(2)
    #for x in collection.find({}, {"_id": 0, "name": 1}).sort("name"):
    #    print(x)
    # 3. Vypsání pouze 10 záznamů z předchozího dotazu
    print_delimiter(3)
    for x in collection.find({}, {"_id": 0, "name": 1}).sort("name").limit(10):
        print(x)
    # 4. Zobrazte dalších 10 záznamů
    print_delimiter(4)
    for x in collection.find({}, {"_id": 0, "name": 1}).sort("name").skip(10).limit(10):
        print(x)
    # 5. #Vypsání restaurací ve čtvrti Bronx (čtvrť = borough)
    print_delimiter(5)
    for x in collection.find({"borough": "Bronx"}, {"_id": 0, "name": 1}).limit(10):
        print(x)
    # 6. Vypsání restaurací, jejichž název začíná na písmeno M
    print_delimiter(6)
    for x in collection.find({"name": {"$regex": "^M"}}, {"_id": 0, "name": 1}).limit(10):
        print(x)
    # 7. Vypsání restaurací, které mají skóre větší než 80
    print_delimiter(7)
    for x in collection.find({"grades.score": {"$gt": 80}}, {"_id": 0, "name": 1}).limit(10):
        print(x)
    # 8. Vypsání restaurací, které mají skóre mezi 80 a 90
    print_delimiter(8)
    for x in collection.find({"grades": {"$elemMatch": {"score": {"$gt": 80, "$lt": 90}}}}).limit(10):
        print(x)
    #'''
    #Bonusové úlohy:
    #'''

    # 9. Vypsání všech restaurací, které mají skóre mezi 80 a 90 a zároveň nevaří americkou (American) kuchyni
    print_delimiter(9)
    for x in collection.find({"$and": [{"grades.score": {"$gt": 80}}, {"grades.score": {"$lt": 90}}, {"cuisine": {"$ne": "American "}}]}, {"_id": 0, "name": 1}).limit(10):
        print(x)
    # 10. Vypsání všech restaurací, které mají alespoň osm hodnocení
    print_delimiter(10)
    for x in collection.find({"grades.score": {"$gt": {"$size":8}}}, {"_id": 0, "name": 1}).limit(10):
        print(x)
    print("test")
    # 11. Vypsání všech restaurací, které mají alespoň jedno hodnocení z roku 2014 
    print_delimiter(11)
    for x in collection.find({"$and": [{"grades.date": {"$lt": datetime.datetime(2015, 1, 1, 0, 0, 0)}}, {"grades.date": {"$gte": datetime.datetime(2014, 1, 1, 0, 0, 0)}}]}, {"_id": 0, "name": 1}).limit(10):
        print(x)
    #'''
    #V této části budete opět vytvářet vlastní restauraci.

    #Řešení:
    #Vytvořte si vaši restauraci pomocí slovníku a poté ji vložte do DB.
    #restaurant = {
    #    ...
    #}
    #'''

    # 12. Uložte novou restauraci (stačí vyplnit název a adresu)
    print_delimiter(12)
    x = collection.insert_one({ "name": "Mala Lod", "address": "adresa 123"})
    # 13. Vypište svoji restauraci
    print_delimiter(13)
    for x in collection.find({"name": "Mala Lod"}):
        print(x)
    # 14. Aktualizujte svoji restauraci - změňte libovolně název
    print_delimiter(14)
    x= collection.update_one({ "name": "Mala Lod"}, {"$set": { "name": "Velka Lod"}})
    for x in collection.find({"name": "Velka Lod"}):
        print(x)
    # 15. Smažte svoji restauraci
    # 15.1 pomocí id (delete_one)
    # 15.2 pomocí prvního nebo druhého názvu (delete_many, využití or)
    print_delimiter(15)
    x = collection.delete_one({"name": "Velka Lod"})
    for x in collection.find({"name": "Velka Lod"}):
        print(x)

    #'''
    #Poslední částí tohoto cvičení je vytvoření jednoduchého indexu.

    #Použijte např. 3. úlohu s vyhledáváním čtvrtě Bronx. První použijte Váš již vytvořený dotaz a na výsledek použijte:

    #cursor.explain()['executionStats'] - výsledek si vypište na výstup a všimněte si položky 'totalDocsExamined'

    #Poté vytvořte index na 'borough', zopakujte dotaz a porovnejte hodnoty 'totalDocsExamined'.

    #S řešením pomůže https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.create_index
    #'''
    print_delimiter(11)
    x = collection.find({"borough": "Bronx"}, {"_id": 0, "name": 1}).explain()["executionStats"]
    print(x)
    print("3772")
    i = collection.create_index([("borough", pymongo.DESCENDING)])
    print(i)
    x = collection.find({"borough": "Bronx"}, {"_id": 0, "name": 1}).explain()["executionStats"]
    print(x)
    print("309")