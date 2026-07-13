from collections.abc import Callable
from functools import wraps
from typing import Any
from time import time
from random import randint


def fireball(power: int) -> str:
    return f"Fireball cast with {power} power"


def spell_timer(func: Callable) -> Callable:
    print(f"Calling {func.__name__}...")

    @wraps(func)
    def timer(power: int) -> str:
        start = time()
        result = func(power)
        exec_time = (time() - start)
        print(f"Spell completed in {exec_time:.3f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def validator(power: int) -> Any:
            if power >= min_power:
                return func(power)
            else:
                return "Insufficient power for this spell"
        return validator
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable, power: int) -> Any:
        for i in range(max_attempts):
            try:
                if randint(0, 20) > 9:
                    return func(power)
                else:
                    raise Exception()
            except Exception:
                print(f"Spell failed, retrying... ({i + 1}/{max_attempts})")
        print(f"Spell casting failed after {max_attempts} attempts")
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all([char.isalpha() or char.isspace()
                                   for char in name]):
            return True
        else:
            return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        def cast(power: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        factory = power_validator(10)
        validator = factory(cast)
        return validator(power)


if __name__ == "__main__":
    print("Testing spell timer...")
    timer = spell_timer(fireball)
    print(f"Result: {timer(30)}")
    print("Testing power validator...")
    decoratorFactory = power_validator(20)
    fireball_validator = decoratorFactory(fireball)
    print(fireball_validator(10))
    print(fireball_validator(30))
    print("Testing retrying spell...")
    retry = retry_spell(3)
    print(retry(fireball, 10))
    print("Testing MageGuild...")
    mageGuild = MageGuild()
    print(MageGuild.validate_mage_name("Sara"))
    print(MageGuild.validate_mage_name("Ze"))
    print(mageGuild.cast_spell("fireball", 15))
    print(mageGuild.cast_spell("fireball", 5))
