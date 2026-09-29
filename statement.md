# Project Statement: Interactive Command-Line Game Engine

## Problem Statement
Building reliable, interactive console utilities requires structured data validation routines and clean modular design. This project addresses the challenge of building a state-controlled Rock-Paper-Scissors game engine that handles malformed string entries, processes non-integer configurations, and uses deterministic randomization structures without crashing.

## Scope of the Project
- Complete terminal execution mapping with 0 GUI requirements.
- Modular architectural pattern dividing core settings, input handlers, tracking loops, and logical scoring matrices across 5 dedicated script modules.
- Strict data parsing mechanisms preventing incorrect loop steps on crash inputs.

## Target Users
- Students evaluating basic game theory and conditional control mappings.
- Evaluators testing cross-module state interaction patterns in Python.

## High-Level Features
- Dynamic match-length adjustment safely handling exception states.
- Clean execution breakdown isolating random generator logic from verification steps.
- Active score dashboards printing summaries after each individual game round.
