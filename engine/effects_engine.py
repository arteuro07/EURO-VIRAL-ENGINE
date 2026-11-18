EFFECTS = {
    "HOOK": {
        "name": "Accroche",
        "instructions": "Zoom progressif et texte animé"
    },
    "ZOOM": {
        "name": "Zoom dynamique",
        "instructions": "Zoom avant avec accélération"
    },
    "VELOCITY": {
        "name": "Velocity",
        "instructions": "Ralenti puis accélération sur le rythme"
    },
    "FLASH_ZOOM": {
        "name": "Flash Zoom",
        "instructions": "Flash blanc court et zoom avant"
    },
    "CINEMATIC_END": {
        "name": "Final cinématique",
        "instructions": "Zoom arrière et titre final"
    }
}

TRANSITIONS = {
    "NONE": "Coupe directe",
    "FLASH": "Flash blanc",
    "SHAKE": "Secousse dynamique",
    "BLUR": "Flou directionnel",
    "ZOOM_OUT": "Zoom arrière"
}

def describe_effect(effect):
    return EFFECTS.get(effect, {
        "name": effect,
        "instructions": "Effet à configurer"
    })

def describe_transition(transition):
    return TRANSITIONS.get(transition, "Transition à configurer")
