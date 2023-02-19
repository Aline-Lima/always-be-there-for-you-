# Author: Aline Botti
# GitHub username: Aline_Lima
# Date: 02/07/2023
# Description: NobelData.py collects data from the file nobels.jason

import json

class NobelData:
     """reads a JSON file containing data on Nobel Prizes"""
     def __init__(self):
         self._categories = ["chemistry", "economics", "literature", "peace", "physics", "medicine"]

     def search_nobel(self, year, category):
          """a method named search_nobel that takes as parameters a year and a category, and returns a sorted list (in normal English dictionary order) of the surnames for the winner(s) in that category for that year (up to three people can share the prize). The year will be a string (e.g. "1975"), not a number. The categories are: "chemistry", "economics", "literature", "peace", "physics", and "medicine"."""
          data = {}
          with open("nobels.json") as infile:
            data = json.load(infile)


          search_nobel = []
          for entry in data["prizes"]:
            if entry["year"] == year and entry["category"] == category:
              for person in entry["laureates"]:
                search_nobel.append(person["surname"])

          search_nobel.sort()
          return search_nobel

def main():
  nd = NobelData()
  print(nd.search_nobel("1956", "chemistry"))

main()
