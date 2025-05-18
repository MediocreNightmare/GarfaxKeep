from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class UFOArchipelagoOptions:
    ufo_hard_objectives: UFOHardObjectives


class UFOGame(Game):
    name = "Unidentified Falling Objects"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = False

    options_cls = UFOArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Reach SCORE score in WORLD",
                data={
                    "SCORE": (self.scores, 1),
                    "WORLD": (self.worlds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach SCORE score in WORLD with the MATCHER matcher, SUIT suit and KICK kick",
                data={
                    "SCORE": (self.scores, 1),
                    "WORLD": (self.worlds, 1),
                    "MATCHER": (self.matchers, 1),
                    "SUIT": (self.suits, 1),
                    "KICK": (self.kicks, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Reach LEVEL in WORLD",
                data={
                    "LEVEL": (self.levels, 1),
                    "WORLD": (self.worlds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach LEVEL in WORLD with the MATCHER matcher, SUIT suit and KICK kick",
                data={
                    "LEVEL": (self.levels, 1),
                    "WORLD": (self.worlds, 1),
                    "MATCHER": (self.matchers, 1),
                    "SUIT": (self.suits, 1),
                    "KICK": (self.kicks, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete the CHALLENGE challenge",
                data={
                    "CHALLENGE": (self.challenges, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete the CHALLENGE challenge without taking damage",
                data={
                    "CHALLENGE": (self.challenges, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            )
        ]


    @property
    def ufo_hard_objectives(self) -> bool:
        return bool(self.archipelago_options.ufo_hard_objectives.value)
        

    @functools.cached_property
    def levels_base(self) -> List[str]:
        return [
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
        ]

    @functools.cached_property
    def hard_levels(self) -> List[str]:
        return [
            "Level 7",
            "Level 8",
            "Level 9",
        ]

    def levels(self) -> List[str]:
        levels: List[str] = self.levels_base[:]

    # Check if hard objectives are included, and include them if so
        if self.ufo_hard_objectives:
            levels.extend(self.hard_levels)

        return sorted(levels)


    @staticmethod
    def worlds() -> List[str]:
        return [
            "World 1",
            "World 2",
            "World 3",
            "World 4",
            "World 5",
            "World 6",
        ]


    @staticmethod
    def challenges() -> List[str]:
        return [
            "Tutorial",
            "Armor Tutorial",
            "Score Tutorial",
            "Spikes",
            "TNT",
            "Rockets",
            "Rockets 2",
            "Cannons",
            "Lasers",
            "Fireballs",
            "Phantoms",
            "Bombflys",
            "World 1",
            "World 2",
            "World 3",
            "World 4",
            "World 5",
            "Quad jump",
            "Dash jump",
            "Jetpack",
            "Phantom puzzle",
            "Bullet hell 1",
            "Bullet hell 2",
            "Mothership",
        ]

    @staticmethod
    def matchers() -> List[str]:
        return [
            "Matcher MK1",
            "Laser Matcher",
            "Matcher MK2",
            "Punch Matcher",
            "Big Drill",
            "Rapid Laser",
            "Rocket Matcher",
            "Instant Matcher",
        ]

    @staticmethod
    def suits() -> List[str]:
        return [
            "None",
            "Glide Cape",
            "Quad Jump Wings",
            "Dash Jump Wings",
            "Frog Suit",
            "Rocket Jump",
            "Teleporter",
            "Jetpack",
        ]

    @staticmethod
    def kicks() -> List[str]:
        return [
            "Strong Kick",
            "Projectile Kick",
            "Grapple Hook",
            "Dash Kick",
            "Lift and Throw",
        ]

    @functools.cached_property
    def scores_base(self) -> range:
        return list(range(1000, 20000, 1000))

    @functools.cached_property
    def scores_hard(self) -> range:
        return list(range(21000, 40000, 1000))

    def scores(self) -> List[str]:
        scores: List[str] = self.scores_base[:]

    # Check if hard objectives are included, and include them if so
        if self.ufo_hard_objectives:
            scores.extend(self.scores_hard)

        return sorted(scores)

# Archipelago Options
class UFOHardObjectives(Toggle):
    """
    Indicates whether to include more difficult scores/level objectives for Unidentified Falling Objects.
    """

    display_name = "UFO Harder Score/Level Objectives"