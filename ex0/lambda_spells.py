def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    return {"max_power": max_power,
            "min_power": min_power,
            "avg_power": sum(map(lambda mage: mage["power"], mages))
            / len(mages)}


if __name__ == "__main__":
    artifacts = [{"name": "Orb", "power": 85, "type": "Crystal"},
                 {"name": "Staff", "power": 92, "type": "Fire"}]
    mages = [{"name": "Gandalf", "power": 95, "element": "Light"},
             {"name": "Sauron", "power": 72, "element": "Dark"}]
    spells = ["fireball", "heal", "shield"]
    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifacts))
    print("\nTesting power filter...")
    print(power_filter(mages, 80))
    print("\nTesting spell transformer...")
    print(spell_transformer(spells))
    print("\nTesting mage stats...")
    print(mage_stats(mages))
