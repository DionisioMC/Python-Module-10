from collections.abc import Callable
from functools import wraps
from typing import Any
from time import time
from random import randint


def fireball(target: str, power: int) -> str:
    return f"Fireball deals {target} {power} damage"


def spell_timer(func: Callable) -> Callable:
    print(f"Calling {func.__name__}...")

    @wraps(func)
    def timer(target: str, power: int) -> str:
        start = time()
        result = func(target, power)
        exec_time = (time() - start)
        print(f"Spell completed in {exec_time:.3f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def validator(target: str, power: int) -> Any:
            if power >= min_power:
                return func(target, power)
            else:
                return "Insufficient power for this spell"
        return validator
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable, target: str, power: int) -> Any:
        for i in range(max_attempts):
            try:
                if randint(0, 20) > 9:
                    return func(target, power)
                else:
                    raise Exception()
            except Exception:
                print(f"Spell failed, retrying... ({i + 1}/{max_attempts})")
        print(f"Spell casting failed after {max_attempts} attempts")
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all([char.isspace() or char.isalpha()
                                   for char in name]):
            return True
        else:
            return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        factory = power_validator(10)
        


if __name__ == "__main__":
    print("Testing spell timer...")
    timer = spell_timer(fireball)
    print(f"Result: {timer('Dragon', 30)}")
    print("Testing power validator...")
    decoratorFactory = power_validator(20)
    fireball_validator = decoratorFactory(fireball)
    print(fireball_validator("Dragon", 10))
    print(fireball_validator("Dragon", 30))
    print("Testing retrying spell...")
    retry = retry_spell(3)
    print(retry(fireball, "Dragon", 10))
    print("Testing MageGuild...")
    mageGuild = MageGuild()
    print(MageGuild.validate_mage_name("Sara"))
    print(MageGuild.validate_mage_name("Ze"))
