# One entry per A2A skill, served on the agent card. `tags` / `examples` let the
# BFA rank the skill in /resolve straight from the card — no self-registration.
# Tuples: (id, name, description, tags, examples).
SKILLS = [
    ("inspect_consumption", "Inspect consumption", "Reports total energy consumption and top consumers",
     ["energy", "consumption"],
     ["quanto estou gastando de energia?", "como está o consumo?", "energia da casa"]),
    ("identify_critical_devices", "Identify critical devices",
     "Lists currently-on devices that must not be turned off",
     ["energy", "critical"], ["quais aparelhos não posso desligar?"]),
]
