#!/usr/bin/python

# Created by: Joao Paulo Paiva

output = open("drive-links-li.txt", "w");

with open("drive-links.txt", "r") as f:
	for link in f:
		imageId = link.split("/")[5]
		output.write("\t\t\t\t\t\t<li class=\"mix one\">\n\t\t\t\t\t\t\t<a href=\"#\" data-reveal-id=\"crowncap-modal\">\n\t\t\t\t\t\t\t\t<div class=\"thumbnail\" style=\"background-image: url('https://drive.google.com/thumbnail?authuser=0&sz=w160&id=" + imageId + "');\"></div>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</li>\n")
