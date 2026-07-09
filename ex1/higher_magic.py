from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {power} HP to {target}"


def fireball(target: str, power: int) -> str:
    return f"Fireball deals {target} {power} damage"


def condition(target: str, power: int) -> bool:
    if target in ["Dragon", "Goblin", "Ghost"] and power > 0:
        return True
    else:
        return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, multiplier * power)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (lambda target, power: spell(target, power)
            if condition(target, power) else "Spell fizzled")


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print(combined_spell("Dragon", 10))
    print("\nTesting power amplifier...")
    amplified_spell = power_amplifier(fireball, 3)
    print(amplified_spell("Dragon", 10))
    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(condition, fireball)
    print(conditional_spell("Table", 10))
    print(conditional_spell("Ghost", 10))
    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))
