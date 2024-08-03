maximumMovements = 10

mapping = {
	"Up": "U",
	"Down": "D",
	"Left": "L",
	"Right": "R",
	"Wait": "W",
	"Attack": "A",
	"Swing": "A",
	"Blast": "A",
	"Punch": "A"
}

reverseMapping = {
		"U": "Up",
	"D": "Down",
	"L": "Left",
	"R": "Right",
	"W": "Wait",
	"A": "Attack",
}

formattedMapping = "{\n"

for k in mapping:
	formattedMapping += f'"{k}": "{mapping[k]}"\n'

formattedMapping += "}"

systemPrompt = f"You are an interpreter for a video game character's actions that occasionally likes to mess with the user. Your task is to convert the user's description of movements and actions into a list of actions based on the provided mapping. Only respond with the characters defined in the mapping and limit the response to a maximum of {maximumMovements} characters."

characterPrompt = f"""{systemPrompt}

Mapping:
{formattedMapping}

Description:
"""
