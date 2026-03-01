#!/usr/bin/env python3


def main() -> None:

    def artifact_sorter(artifacts: list[dict]) -> list[dict]:
        sorted_list = sorted(
            artifacts, key=lambda item: item['power'], reverse=True)
        return sorted_list

    def power_filter(mages: list[dict], min_power: int) -> list[dict]:
        filtered_list = list(
            filter(lambda item: item['power'] >= min_power, mages))
        return filtered_list

    def spell_transformer(spells: list[str]) -> list[str]:
        mapped_list = list(map(lambda x: f"* {x} *", spells))
        return mapped_list

    def mage_stats(mages: list[dict]) -> dict:
        stats = {}
        max_mage = max(mages, key=lambda item: item['power'])
        min_mage = min(mages, key=lambda item: item['power'])
        total_power = sum(map(lambda item: item['power'], mages))
        avg_power = round(total_power / len(mages), 2)
        stats['max_power'] = max_mage['power']
        stats['min_power'] = min_mage['power']
        stats['avg_power'] = avg_power
        return stats

    artifacts = [
        {'name': 'Light Prism', 'power': 94, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 93, 'type': 'accessory'},
        {'name': 'Wind Cloak', 'power': 81, 'type': 'accessory'},
        {'name': 'Storm Crown', 'power': 114, 'type': 'relic'}
    ]

    mages = [
        {'name': 'River', 'power': 99, 'element': 'shadow'},
        {'name': 'Kai', 'power': 67, 'element': 'lightning'},
        {'name': 'Jordan', 'power': 79, 'element': 'light'},
        {'name': 'Ember', 'power': 71, 'element': 'wind'}
    ]

    spells = ['flash', 'blizzard', 'fireball', 'meteor']

    print("\nTesting artifact sorter...")

    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) comes before "
          f"{sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")

    filtered_mages = power_filter(mages, 75)
    print("Mages with power over 75 are:")
    for mage in filtered_mages:
        print(f"- {mage['name']}")

    print("\nTesting spell transformer...")

    mapped_spells = spell_transformer(spells)
    for spell in mapped_spells:
        print(spell, end=" ")
    print("\n")

    print("Testing mage statistics...")

    stats = mage_stats(mages)
    print(f"Higher power level: {stats['max_power']}")
    print(f"Lower power level: {stats['min_power']}")
    print(f"Average power level: {stats['avg_power']}")


if __name__ == "__main__":
    main()
