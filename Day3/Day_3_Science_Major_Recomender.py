
def major(str):
  print("You are recommended the " + str + " major!")

def main():
  print("Welcome to the Science Major recommender!")
  one_feild = input("Do you like you focus in on one field? Type 'Y' or 'N'")
  if one_feild.lower() == "n":
    flex_or_struct = input("Do you prefer flexibility or structure? F or S")
    if flex_or_struct.lower() == "f":
      major("Integrated Science")
    else:
      major("Combined Major in Science")
  else:
    nature = input("Are you passionate about natural things? Y or N")
    if nature.lower() == "y":
      made_of = input("Are you passionate about what natrure is made of? Y or N")
      if made_of.lower() == "n":
        living = input("Interested in living nature? Y or N")
        if living.lower() == "y":
          water = input("How about nature in water? Y or N")
          if water.lower() == "y":
            only_water = input("Only water? Y or N")
            if only_water.lower() == "y":
              major("Oceanography")
            else:
              major("Earth and Ocean Sciences")
          else:
            plants = input("Interested in plants, animals, or both? P, A, or B")
            if plants.lower() == "p":
              major("Botany")
            elif plants.lower() == "a":
              major("Zoology")
            else:
              major("Environmental Sciences")
        else:
          earth = input("Interested in nature on the Earth? Y or N")
          if earth.lower() == "y":
            mmr = input("Math, Maps, or Rocks? MT, MP, or R")
            if mmr.lower() == "mt":
              major("Geophysics")
            elif mmr.lower() == "mp":
              major("Geographical Sciences")
            else:
              major("Geological Sciences")
          else:
            far = input("How far off the earth? Far or Very far? Type F or VF")
            if far.lower() == "f":
              major("Atmospheric Sciences")
            else:
              major("Astronomy")
      else:
        small = input("Interested in very small things? Y or N")
        if small.lower() == "y":
          immune = input("Interested in the immune system? Y or N")
          if immune.lower() == "y":
            major("Microbiology and Immunology")
          else:
            major("Cellular and Physiological Science")
        else:
          prefer = input("What do you prefer, Chemistry, Technology, Brains, Math, or Other. Type C, T, B, M, or O.")
          if prefer.lower() == "c":
            major("Biochemistry")
          elif prefer.lower() == "t":
            major("Biotechnology")
          elif prefer.lower() == "b":
            major("Neuroscience")
          elif prefer.lower() == "m":
            major("Bio-Physics")
          else:
            major("Biology")
    else:
      math = input("Do you like math? Y or N")
      if math.lower() == "y":
        a_lot = input("Do you like math A LOT? Y or N")
        if a_lot.lower() == "y":
          pure_app = input("Do you prefer pure math or applications? P or A")
          if pure_app.lower() == "p":
            major("Mathematics")
          else:
            major("Physics")
        else:
          code_theory = input("Do you prefer theory or code? T or C")
          if code_theory.lower() == "t":
            major("Statistics")
          else:
            major("Computer Science")
      else:
        brains = input("Do you like brains? Y or N")
        if brains.lower() == "y":
          dead_brains = input("Dead brains? Y or N") 
          if dead_brains.lower() == "y":
            major("Forensic Science")
          else:
            thought_act = input("Thoughts or actions? T or A")
            if thought_act.lower() == "t":
              major("Cognitive Systems")
            else:
              major("Behavioural Neuroscience")
        else:
          money = input("Do you really like money? Y or N")
          if money.lower() == "y":
            major("Pharmacology")
          else:
            major("Chemistry")
  print("Goodbye!!")

main()
