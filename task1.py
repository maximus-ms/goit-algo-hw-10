import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

L = pulp.LpVariable("L", lowBound=0, cat="Integer")  # Lemonade
F = pulp.LpVariable("F", lowBound=0, cat="Integer")  # Fruit Juice

model += L + F, "Production"

model += 2 * L + F <= 100  # Limits for "Water"
model += L <= 50  # Limits for "Sugar"
model += L <= 30  # Limits for "Lemon Juice"
model += 2 * F <= 40  # Limits for "Fruit Puree"
model.solve()

print('Production of "Lemonade":', L.varValue)
print('Production of "Fruit Juice":', F.varValue)
print('Total production :', L.varValue + F.varValue)
