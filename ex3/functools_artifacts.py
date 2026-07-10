from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    reduced = 0
    if len(spells) == 0:
        print("Spells list is empty")
        return 0
    elif operation == "add":
        reduced = reduce(lambda spell1, spell2: add(spell1, spell2), spells)
    elif operation == "multiply":
        reduced = reduce(lambda spell1, spell2: mul(spell1, spell2), spells)
    elif operation == "max":
        reduced = reduce((lambda spell1, spell2: max(spell1, spell2)), spells)
    elif operation == "min":
        reduced = reduce((lambda spell1, spell2: min(spell1, spell2)), spells)
    else:
        print("Operation not supported")
        return 0
    return reduced


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {"fire": partial(base_enchantment, 50, "fire"),
            "ice": partial(base_enchantment, 50, "ice"),
            "light": partial(base_enchantment, 50, "light")}


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(arg: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def _(arg: int) -> str:
        message = "The spell fizzled out"
        if arg > 0:
            message = f"Damage spell: {arg} damage"
        return message

    @spell.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell.register
    def _(arg: list):
        return f"Multi-cast: {len(arg)} spells"
    return spell


if __name__ == "__main__":
    spells = [5, 10, 15]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    print("\nTesting memoized fibonacci...")
    print(memoized_fibonacci(0))
    print(memoized_fibonacci(1))
    print(memoized_fibonacci(10))
    print(memoized_fibonacci(15))
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher("fireball"))
    print(dispatcher(10))
    print(dispatcher([1, 2, 3]))
