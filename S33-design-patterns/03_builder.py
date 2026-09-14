'''BUILDER - creational pattern.

Problem:  an object has many optional parts, and a constructor with ten
          parameters is impossible to read.
Solution: build it step by step, one method per part.

The trick that makes it pleasant: every method returns `self`, so the calls can
be CHAINED.
'''


class Pizza:
    'The object we want to build.'

    def __init__(self) -> None:
        self.size: str | None = None
        self.cheese: bool = False
        self.pepperoni: bool = False
        self.mushrooms: bool = False

    def __str__(self) -> str:
        toppings = []
        if self.cheese:
            toppings.append('cheese')
        if self.pepperoni:
            toppings.append('pepperoni')
        if self.mushrooms:
            toppings.append('mushrooms')
        return f'Pizza(size={self.size}, toppings={toppings})'


class PizzaBuilder:
    'Builds a Pizza one step at a time.'

    def __init__(self) -> None:
        self.pizza = Pizza()

    def set_size(self, size: str) -> 'PizzaBuilder':
        self.pizza.size = size
        return self                # returning self is what allows chaining

    def add_cheese(self) -> 'PizzaBuilder':
        self.pizza.cheese = True
        return self

    def add_pepperoni(self) -> 'PizzaBuilder':
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self) -> 'PizzaBuilder':
        self.pizza.mushrooms = True
        return self

    def build(self) -> Pizza:
        'Return the finished object.'
        if self.pizza.size is None:
            raise ValueError('a pizza needs a size')
        return self.pizza


if __name__ == '__main__':
    # Everything on one line:
    pizza = PizzaBuilder().set_size('large').add_cheese().add_pepperoni().build()
    print(pizza)

    # In two steps:
    builder = PizzaBuilder().set_size('small').add_mushrooms()
    print(builder.build())

    # Spread over several lines - the most readable form:
    pizza = (
        PizzaBuilder()
        .set_size('large')
        .add_cheese()
        .add_pepperoni()
        .add_mushrooms()
        .build()
    )
    print(pizza)

    try:
        PizzaBuilder().add_cheese().build()
    except ValueError as e:
        print('Refused:', e)
