from classificator.categories_classificator import product_classificator

product = ["Alnatura Bio Baked Beans 360G", ["Startseite","Lebensmittel","Konserven"]]
abc = product_classificator(product[0], product[1])
print(abc)