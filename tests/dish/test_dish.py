from src.models.dish import Dish, Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("Lasanha", 15.5)
    dish1.add_ingredient_dependency(Ingredient('presunto'), 10)
    dish1.add_ingredient_dependency(Ingredient('queijo mussarela'), 15)

    dish2 = Dish("Coxinha", 5.5)
    dish2.add_ingredient_dependency(Ingredient('frango'), 10)

    restrictions = {
        "lasanha": {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED, Restriction.LACTOSE},
        "coxinha": {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED},
    }

    value_error = 'Dish price must be greater then zero.'
    with pytest.raises(ValueError, match=value_error):
        Dish('Nugget', 0)

    type_error = 'Dish price must be float.'
    with pytest.raises(TypeError, match=type_error):
        Dish('Pizza', 'A')

    dish_invalid_name = dish1.name == dish2.name
    assert dish_invalid_name is False

    dish_valid_name = dish1.name == 'Lasanha'
    assert dish_valid_name is True

    dish_equal = dish1 == Dish("Lasanha", 15.5)
    assert dish_equal is True

    dish_different = dish1 == dish2
    assert dish_different is False

    dish_hash_equal = hash(dish1) == hash("Dish('Lasanha', R$15.50)")
    assert dish_hash_equal is True

    dish_hash_different = hash(dish1) == hash(dish2)
    assert dish_hash_different is False

    dish_valid_add_ingredient = dish2.recipe == {Ingredient('frango'): 10}
    assert dish_valid_add_ingredient is True

    dish_invalid_add_ingredient = dish1 == dish2
    assert dish_invalid_add_ingredient is False

    dish_valid_ingredients = dish2.get_ingredients() == {Ingredient('frango')}
    assert dish_valid_ingredients is True

    dish_invalid_ingredients = dish2.get_ingredients() == dish1.get_ingredients()
    assert dish_invalid_ingredients is False

    dish_invalid_restrictions = dish1.get_restrictions() == restrictions['coxinha']
    assert dish_invalid_restrictions is False

    dish_valid_restrictions = dish1.get_restrictions() == restrictions['lasanha']
    assert dish_valid_restrictions is True
