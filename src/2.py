

def explore_wonder(wonder):
  if wonder == "black hole":
    return "The event horizon of a black hole is the point of no return, beyond which anything that enters cannot escape. The laws of physics as we know them break down at such massive distances and velocities."
  elif wonder == "galaxy":
    return "Galaxies are vast, star-filled hubs of activity in the universe. They are the building blocks of our cosmic neighborhoods."
  elif wonder == "planet":
    return "Planets are celestial bodies that orbit around stars and have conditions suitable for life to exist. Earth is a fascinating example of a planet, with its diverse ecosystems and unique biosphere."
  elif wonder == "universe":
    return "The universe is vast and complex beyond comprehension. It has billions of galaxies, each with trillions of stars and countless planets that may or may not support life."
  else:
    raise ValueError("Invalid value for wonder")