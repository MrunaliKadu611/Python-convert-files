from json2html import*

datastore = open('mrunali.json', 'r')

json2html.convert(json= datastore)

#  table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\""