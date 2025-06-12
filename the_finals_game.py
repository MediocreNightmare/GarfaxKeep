from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class FinalsArchipelagoOptions:
    finals_include_world_tour: FinalsIncludeWorldTour
    finals_include_specific_equipment: FinalsIncludeSpecificEquipment


class FinalsGame(Game):
    name = "The Finals"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
    ]

    is_adult_only_or_unrated = False

    options_cls = FinalsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="If you receive an elimination amount challenge, complete it in one game",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="If there is an event mode available, play that instead of quickplay if applicable",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = list()

        templates.extend([
            GameObjectiveTemplate(
                label="Win a Quickplay match with the BUILD build",
                data={
                    "BUILD": (self.builds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a game of Team Deathmatch with the BUILD build",
                data={
                    "BUILD": (self.builds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a Quick Cash match with the BUILD build",
                data={
                    "BUILD": (self.builds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get an elimination or revive with a BUILD build gadget",
                data={
                    "BUILD": (self.builds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get ELIMINATIONS eliminations with BUILD build",
                data={
                    "BUILD": (self.builds, 1),
                    "ELIMINATIONS": (self.eliminations_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Revive teammates REVIVES times",
                data={
                    "REVIVES": (self.revives_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get an elimination with an arena carriable",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Start a cashout",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Steal a cashout",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete your daily contracts",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get a non-melee weapon melee elimination",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])

        if self.include_specific_equipment:
            templates.append(
                GameObjectiveTemplate(
                    label="Win a Quickplay match using SPECIALIZATIONLIGHT, WEAPONLIGHT, GADGETLIGHT on the Light build",
                    data={
                        "SPECIALIZATIONLIGHT": (self.specializationslight, 1),
                        "WEAPONLIGHT": (self.weaponslight, 1),
                        "GADGETLIGHT": (self.gadgetslight, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            )

        if self.include_specific_equipment:
            templates.append(
                GameObjectiveTemplate(
                    label="Win a Quickplay match using SPECIALIZATIONMEDIUM, WEAPONMEDIUM, GADGETMEDIUM on the Medium build",
                    data={
                        "SPECIALIZATIONMEDIUM": (self.specializationsmedium, 1),
                        "WEAPONMEDIUM": (self.weaponsmedium, 1),
                        "GADGETMEDIUM": (self.gadgetsmedium, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            )

        if self.include_specific_equipment:
            templates.append(
                GameObjectiveTemplate(
                    label="Win a Quickplay match using SPECIALIZATIONHEAVY, WEAPONHEAVY, GADGETHEAVY on the Heavy build",
                    data={
                        "SPECIALIZATIONHEAVY": (self.specializationsheavy, 1),
                        "WEAPONHEAVY": (self.weaponsheavy, 1),
                        "GADGETHEAVY": (self.gadgetsheavy, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            )

        if self.include_specific_equipment:
            templates.append(
                GameObjectiveTemplate(
                    label="Get ELIMINATIONS eliminations with the WEAPONLIGHT Light weapon",
                    data={
                        "WEAPONLIGHT": (self.weaponslight, 1),
                        "ELIMINATIONS": (self.eliminations_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            )

        if self.include_specific_equipment:
            templates.append(
                GameObjectiveTemplate(
                    label="Get ELIMINATIONS eliminations with the WEAPONMEDIUM Medium weapon",
                    data={
                        "WEAPONMEDIUM": (self.weaponsmedium, 1),
                        "ELIMINATIONS": (self.eliminations_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            )

        if self.include_specific_equipment:
            templates.append(
                GameObjectiveTemplate(
                    label="Get ELIMINATIONS eliminations with the WEAPONHEAVY Heavy weapon",
                    data={
                        "WEAPONHEAVY": (self.weaponsheavy, 1),
                        "ELIMINATIONS": (self.eliminations_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            )

        if self.include_world_tour:
            templates.append(
                GameObjectiveTemplate(
                    label="Win a World Tour",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=3,
                ),
            )

        if self.include_world_tour:
            templates.append(
                GameObjectiveTemplate(
                    label="Reach Round ROUND in World Tour",
                    data={
                        "ROUND": (self.rounds, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            )
            
        if self.include_world_tour:
            templates.append(
                GameObjectiveTemplate(
                    label="Reach 30000 Cash in a single round",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                )
            )

        return templates

    @property
    def include_world_tour(self) -> bool:
        return bool(self.archipelago_options.finals_include_world_tour.value)

    @property
    def include_specific_equipment(self) -> bool:
        return bool(self.archipelago_options.finals_include_specific_equipment.value)

    @staticmethod
    def builds() -> List[str]:
        return [
            "Light",
            "Medium",
            "Heavy",
        ]

    @staticmethod
    def specializationslight() -> List[str]:
        return [
            "Cloaking Device",
            "Grappling Hook",
            "Evasive Dash",
        ]

    @staticmethod
    def weaponslight() -> List[str]:
        return [
            "93R",
            "M11",
            "Recurve Bow",
            "SR-84",
            "Throwing Knives",
            "ARN-220",
            "Dagger",
            "LH1",
            "M26 Matter",
            "SH1900",
            "Sword",
            "V95",
            "XP-54",
        ]

    @staticmethod
    def gadgetslight() -> List[str]:
        return [
            "Breach Charge",
            "Flashbang",
            "Frag Grenade",
            "Goo Grenade",
            "Pyro Grenade",
            "Smoke Grenade",
            "Sonar Grenade",
            "Gas Grenade",
            "Gateway",
            "Glitch Grenade",
            "Gravity Vortex",
            "Nullifier",
            "Thermal Bore",
            "Thermal Vision",
            "Tracking Dart",
            "Vanishing Bomb",
            "H+ Infuser",
        ]

    @staticmethod
    def specializationsmedium() -> List[str]:
        return [
            "Guardian Turret",
            "Healing Beam",
            "Dematerializer",
        ]

    @staticmethod
    def weaponsmedium() -> List[str]:
        return [
            "AKM",
            "CB-01 Repeater",
            "FAMAS",
            "PIKE-556",
            "R .357",
            "Cerberus 12GA",
            "CL-40",
            "Dual Blades",
            "FCAR",
            "Model 1887",
            "Riot Shield",
        ]

    @staticmethod
    def gadgetsmedium() -> List[str]:
        return [
            "Defibrillator",
            "Explosive Mine",
            "Flashbang",
            "Frag Grenade",
            "Gas Mine",
            "Glitch Trap",
            "Goo Grenade",
            "Jump Pad",
            "Pyro Grenade",
            "Smoke Grenade",
            "APS Turret",
            "Data Reshaper",
            "Gas Grenade",
            "Proximity Sensor",
            "Zipline",
            "Breach Drill",
        ]

    @staticmethod
    def specializationsheavy() -> List[str]:
        return [
            "Charge 'N' Slam",
            "Winch Claw",
            "Goo Gun",
            "Mesh Shield",
        ]

    @staticmethod
    def weaponsheavy() -> List[str]:
        return [
            "Flamethrower",
            "Lewis Gun",
            "M60",
            "Sledgehammer",
            ".50 Akimbo",
            "KS-23",
            "M134 Minigun",
            "MGL32",
            "SA1216",
            "Shak-50",
            "Spear",
        ]

    @staticmethod
    def gadgetsheavy() -> List[str]:
        return [
            "Barricade",
            "Explosive Mine",
            "Flashbang",
            "Frag Grenade",
            "Goo Grenade",
            "Pyro Grenade",
            "RPG-7",
            "Smoke Grenade",
            "Anti-Gravity Cube",
            "C4",
            "Dome Shield",
            "Gas Grenade",
            "Lockbolt",
            "Proximity Sensor",
            "Pyro Mine",
            "Healing Emitter",
        ]

    @staticmethod
    def rounds() -> List[str]:
        return [
            "Two",
            "Three",
        ]

    @staticmethod
    def eliminations_range() -> range:
        return range(10, 20)

    @staticmethod
    def revives_range() -> range:
        return range(5, 10)

# Archipelago Options
class FinalsIncludeWorldTour(Toggle):
    """
    Indicates whether to include World Tour objectives in The Finals.
    """

    display_name = "Finals World Tour"

class FinalsIncludeSpecificEquipment(Toggle):
    """
    Indicates whether to include specific equipment objectives for The Finals.
    If you set this option and don't have everything unlocked, replace what you are missing with whatever you would like.
    """

    display_name = "Finals Include Specific Equipment"
