# GoITNeo Algo HW-10

## Task 1. Production Optimization
The company produces two types of beverages: "Lemonade" and "Fruit Juice." Different ingredients and limited equipment are used in the production of these beverages. The task is to maximize production while considering the limited resources.
Task conditions:
 - Resource:
    - 100 units of "Water"
    - 50 units of "Sugar"
    - 30 units of "Lemon Juice"
    - 40 units of "Fruit Puree"

 - Production of one unit of "Lemonade" requires:
    - 2 units of "Water"
    - 1 unit of "Sugar"
    - 1 unit of "Lemon Juice"

 - Production of one unit of "Fruit Juice" requires:
    - 2 units of "Fruit Puree"
    - 1 unit of "Water"

Using PuLP, create a model that determines how much "Lemonade" and "Fruit Juice" need to be produced to maximize the total quantity of products while adhering to resource constraints. Write a program that maximizes the total quantity of produced products, considering the limitations on resource quantities.

### Solution
We need to import module ```pulp```, create maximize model and configure it.
```python
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
```
We have a result:
```
Production of "Lemonade": 30.0
Production of "Fruit Juice": 20.0
Total production : 50.0
```
### Conclusions
Module ```PuLP``` is a great tool to solve tasks with linear dependencies.

## Task 2. Definite Integral Computation
Calculate the value of the integral of the function using the Monte Carlo method, in other words, find the area under this graph.
Verify the accuracy of the calculations to confirm the precision of the Monte Carlo method by comparing the obtained result with analytical calculations or the result of executing the quad function. Write conclusions.

*N.P. You can choose any function.*
