"""
************************************************************************
*      Script d'extraction et de mise en forme			      *      des données de localisation d'un fichier KML
*      Récupére la première paire de coordonnées d'une balise 
*      "coordinates" et le formate dans une fichier texte au format 
*      'lat, long' 
*
***********************************************************************
"""
from lxml import etree

tree = etree.parse("data.xml")
for user in tree.xpath("/Document/Placemark/LineString/coordinates"):
    
    fichier = open("dataloc.txt", "a")
    fichier.write("\n"+user.text)
    fichier.close()
  
file = open('dataloc.txt', "r")
line = file.readline()
while line:
    
    splt = line.split(",0 ")
    line = file.readline()
    splt2 = splt[0].split(',')
    if len(splt2) > 1 :
      print(splt2)
      fileclear = open('donnerclear.txt', "a")
      data=splt2[1]
      data=data+", "
      data=data+splt2[0]
      data=data+",\n"
      fileclear.write(data)
      fileclear.close()
file.close()


