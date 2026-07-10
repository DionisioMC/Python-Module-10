from collections.abc import Callable


def mage_counter() -> Callable:
    call_count = 0

    def counter() -> int:
        nonlocal call_count
        call_count = call_count + 1
        return call_count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(add: int) -> int:
        nonlocal initial_power
        initial_power = initial_power + add
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable]:
    memory = dict()

    def store(key: str, value: int | str) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter = mage_counter()
    print(counter())
    print(counter())
    accumulator = spell_accumulator(10)
    print(accumulator(20))
    print(accumulator(30))
    factory = enchantment_factory("Fire")
    print(factory("Ball"))
    vault = memory_vault()
    store = vault["store"]
    store("secret", 42)
    print(vault["recall"]("secret"))
    print(vault["recall"]("batata"))
