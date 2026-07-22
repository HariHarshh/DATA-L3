country_code = {'INDIA' : '0091',
                'AUSTRALIA' : '0025',
                'NEPAL' : '00977',
                'PAKISTAN' : '0092'
}

print("Country code for INDIA  -")
print(country_code.get('INDIA', 'NOT FOUND'))

print("Country code for JAPAN  -")
print(country_code.get('JAPAN', 'NOT FOUND'))