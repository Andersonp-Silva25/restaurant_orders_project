from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1.
def test_ingredient():
    ingredient1 = Ingredient('carne')
    ingredient2 = Ingredient('salmão')
    restrictions = {
        "carne": {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED},
        "salmão": {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
        },
    }

    hash_is_true = hash(ingredient1) == hash('carne')
    assert hash_is_true is True

    hash_is_false = hash(ingredient1) == hash(ingredient2)
    assert hash_is_false is False

    ingedient_diferent = ingredient1 == ingredient2
    assert ingedient_diferent is False

    ingredient_equal = ingredient1 == Ingredient('carne')
    assert ingredient_equal is True

    ingredient_valid_name = ingredient1.name == 'carne'
    assert ingredient_valid_name is True

    ingredient_invalid_name = ingredient1.name == ingredient2.name
    assert ingredient_invalid_name is False
    
    ingredient_invalid_repr = repr(ingredient1) == repr(ingredient2)
    assert ingredient_invalid_repr is False

    ingredient_valid_repr = repr(ingredient1) == "Ingredient('carne')"
    assert ingredient_valid_repr is True

    ingredient_invalid_restrictions = ingredient1.restrictions == ingredient2.restrictions
    assert ingredient_invalid_restrictions is False

    ingredient_valid_restrictions = ingredient1.restrictions == restrictions['carne']
    assert ingredient_valid_restrictions is True
